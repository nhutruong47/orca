package org.example.backend.controller;

import org.example.backend.dto.ChatMessageDTO;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.ChatService;
import org.example.backend.service.NotificationService;
import org.example.backend.service.PresenceService;
import org.springframework.http.ResponseEntity;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import java.util.UUID;

@RestController
@RequestMapping("/api")
public class ChatController {

    private final ChatService chatService;
    private final SimpMessagingTemplate messagingTemplate;
    private final PresenceService presenceService;
    private final NotificationService notificationService;
    private final AccessControlService accessControlService;
    private final TeamMemberRepository teamMemberRepository;
    private final TeamRepository teamRepository;

    public ChatController(
            ChatService chatService,
            SimpMessagingTemplate messagingTemplate,
            PresenceService presenceService,
            NotificationService notificationService,
            AccessControlService accessControlService,
            TeamMemberRepository teamMemberRepository,
            TeamRepository teamRepository) {
        this.chatService = chatService;
        this.messagingTemplate = messagingTemplate;
        this.presenceService = presenceService;
        this.notificationService = notificationService;
        this.accessControlService = accessControlService;
        this.teamMemberRepository = teamMemberRepository;
        this.teamRepository = teamRepository;
    }

    @GetMapping("/teams/{teamId}/chat")
    public ResponseEntity<?> getGroupMessages(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        try {
            accessControlService.validateTeamAccess(currentUser.getId(), teamId);
            notificationService.markChatConversationRead(currentUser.getId(), teamId, null);
            return ResponseEntity.ok(chatService.getGroupMessages(teamId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/teams/{teamId}/chat/dm/{userId}")
    public ResponseEntity<?> getDirectMessages(
            @PathVariable UUID teamId,
            @PathVariable UUID userId,
            @AuthenticationPrincipal User currentUser) {
        try {
            accessControlService.validateTeamAccess(currentUser.getId(), teamId);
            notificationService.markChatConversationRead(currentUser.getId(), teamId, userId);
            return ResponseEntity.ok(chatService.getDirectMessages(teamId, currentUser.getId(), userId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/teams/{teamId}/chat/dm-previews")
    public ResponseEntity<?> getDmPreviews(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        try {
            accessControlService.validateTeamAccess(currentUser.getId(), teamId);
            return ResponseEntity.ok(chatService.getLastDmMessages(teamId, currentUser.getId()));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/teams/{teamId}/chat")
    public ResponseEntity<?> sendMessage(
            @PathVariable UUID teamId,
            @RequestBody Map<String, String> body,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.validateTeamAccess(currentUser.getId(), teamId);
        String content = body.get("content");
        String recipientIdStr = body.get("recipientId");
        String attachmentUrl = body.get("attachmentUrl");
        String attachmentName = body.get("attachmentName");
        String attachmentType = body.get("attachmentType");

        if ((content == null || content.isBlank()) && (attachmentUrl == null || attachmentUrl.isBlank())) {
            return ResponseEntity.badRequest().body(Map.of("error", "Tin nhắn không được để trống"));
        }

        UUID recipientId = null;
        if (recipientIdStr != null && !recipientIdStr.isBlank()) {
            recipientId = UUID.fromString(recipientIdStr);
        }

        ChatMessageDTO saved = chatService.sendMessage(
                teamId, currentUser, recipientId, content,
                attachmentUrl, attachmentName, attachmentType);
        String senderName = currentUser.getFullName() != null
                ? currentUser.getFullName()
                : currentUser.getUsername();
        String preview = buildPreview(content);

        if (recipientId == null) {
            Team team = teamRepository.findById(teamId)
                    .orElseThrow(() -> new RuntimeException("Team not found"));
            Map<UUID, User> recipients = new LinkedHashMap<>();
            teamMemberRepository.findByTeamId(teamId).forEach(member ->
                    recipients.put(member.getUser().getId(), member.getUser()));
            if (team.getOwner() != null) {
                recipients.put(team.getOwner().getId(), team.getOwner());
            }
            recipients.remove(currentUser.getId());

            for (User recipient : recipients.values()) {
                notificationService.createAndSend(
                        recipient,
                        "Tin nhắn mới trong " + team.getName(),
                        senderName + ": " + preview,
                        "CHAT_MESSAGE",
                        teamId,
                        null);
            }
            messagingTemplate.convertAndSend("/topic/team/" + teamId, saved);
        } else {
            notificationService.createAndSend(
                    recipientId,
                    "Tin nhắn mới từ " + senderName,
                    preview,
                    "CHAT_MESSAGE",
                    teamId,
                    currentUser.getId());
            messagingTemplate.convertAndSend(
                    "/topic/dm/" + teamId + "/" + currentUser.getId() + "/" + recipientId, saved);
            messagingTemplate.convertAndSend(
                    "/topic/dm/" + teamId + "/" + recipientId + "/" + currentUser.getId(), saved);
        }

        return ResponseEntity.ok(saved);
    }

    @PatchMapping("/teams/{teamId}/chat/read")
    public ResponseEntity<?> markConversationRead(
            @PathVariable UUID teamId,
            @RequestBody Map<String, String> body,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.validateTeamAccess(currentUser.getId(), teamId);
        String conversationType = body.getOrDefault("conversationType", "GROUP");
        UUID actorId = null;

        if ("DIRECT".equalsIgnoreCase(conversationType)) {
            String otherUserId = body.get("otherUserId");
            if (otherUserId == null || otherUserId.isBlank()) {
                return ResponseEntity.badRequest().body(Map.of("error", "Thiếu người dùng của cuộc trò chuyện"));
            }
            actorId = UUID.fromString(otherUserId);
            UUID directActorId = actorId;
            boolean actorBelongsToTeam = teamMemberRepository.existsByTeamIdAndUserId(teamId, actorId)
                    || teamRepository.findById(teamId)
                            .map(team -> team.getOwner() != null
                                    && directActorId.equals(team.getOwner().getId()))
                            .orElse(false);
            if (!actorBelongsToTeam) {
                return ResponseEntity.badRequest().body(Map.of("error", "Người dùng không thuộc xưởng"));
            }
        }

        int updated = notificationService.markChatConversationRead(
                currentUser.getId(), teamId, actorId);
        return ResponseEntity.ok(Map.of("updated", updated));
    }

    @GetMapping("/presence/online")
    public ResponseEntity<Set<String>> getOnlineUsers() {
        return ResponseEntity.ok(presenceService.getOnlineUserIds());
    }

    private String buildPreview(String content) {
        if (content == null || content.isBlank()) {
            return "Đã gửi một tệp đính kèm";
        }
        return content.length() > 50 ? content.substring(0, 50) + "..." : content;
    }
}
