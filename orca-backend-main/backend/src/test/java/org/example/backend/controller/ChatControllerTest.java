package org.example.backend.controller;

import org.example.backend.dto.ChatMessageDTO;
import org.example.backend.entity.Team;
import org.example.backend.entity.TeamMember;
import org.example.backend.entity.User;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.ChatService;
import org.example.backend.service.NotificationService;
import org.example.backend.service.PresenceService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.messaging.simp.SimpMessagingTemplate;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.*;
import static org.mockito.Mockito.*;

class ChatControllerTest {

    private ChatService chatService;
    private SimpMessagingTemplate messagingTemplate;
    private NotificationService notificationService;
    private AccessControlService accessControlService;
    private TeamMemberRepository teamMemberRepository;
    private TeamRepository teamRepository;
    private ChatController controller;

    @BeforeEach
    void setUp() {
        chatService = mock(ChatService.class);
        messagingTemplate = mock(SimpMessagingTemplate.class);
        notificationService = mock(NotificationService.class);
        accessControlService = mock(AccessControlService.class);
        teamMemberRepository = mock(TeamMemberRepository.class);
        teamRepository = mock(TeamRepository.class);
        controller = new ChatController(
                chatService,
                messagingTemplate,
                mock(PresenceService.class),
                notificationService,
                accessControlService,
                teamMemberRepository,
                teamRepository);
    }

    @Test
    void groupMessageCreatesPersistentNotificationForEveryOtherMember() {
        UUID teamId = UUID.randomUUID();
        User sender = user("sender");
        User firstRecipient = user("first");
        User secondRecipient = user("second");
        Team team = new Team();
        team.setId(teamId);
        team.setName("Xưởng An Phú");
        team.setOwner(firstRecipient);

        when(teamRepository.findById(teamId)).thenReturn(Optional.of(team));
        when(teamMemberRepository.findByTeamId(teamId)).thenReturn(List.of(
                member(team, sender), member(team, firstRecipient), member(team, secondRecipient)));
        when(chatService.sendMessage(eq(teamId), eq(sender), isNull(), eq("Xin chào"),
                isNull(), isNull(), isNull())).thenReturn(new ChatMessageDTO());

        var response = controller.sendMessage(teamId, Map.of("content", "Xin chào"), sender);

        assertEquals(200, response.getStatusCode().value());
        verify(notificationService).createAndSend(
                eq(firstRecipient), contains("Xưởng An Phú"), contains("Xin chào"),
                eq("CHAT_MESSAGE"), eq(teamId), isNull());
        verify(notificationService).createAndSend(
                eq(secondRecipient), contains("Xưởng An Phú"), contains("Xin chào"),
                eq("CHAT_MESSAGE"), eq(teamId), isNull());
        verify(notificationService, never()).createAndSend(
                eq(sender), anyString(), anyString(), anyString(), any(), any());
        verify(messagingTemplate).convertAndSend(eq("/topic/team/" + teamId), any(ChatMessageDTO.class));
    }

    @Test
    void directMessageStoresSenderAsConversationActor() {
        UUID teamId = UUID.randomUUID();
        User sender = user("sender");
        User recipient = user("recipient");
        when(chatService.sendMessage(eq(teamId), eq(sender), eq(recipient.getId()), eq("Chào riêng"),
                isNull(), isNull(), isNull())).thenReturn(new ChatMessageDTO());

        var response = controller.sendMessage(teamId, Map.of(
                "content", "Chào riêng",
                "recipientId", recipient.getId().toString()), sender);

        assertEquals(200, response.getStatusCode().value());
        verify(notificationService).createAndSend(
                eq(recipient.getId()), contains("sender"), eq("Chào riêng"),
                eq("CHAT_MESSAGE"), eq(teamId), eq(sender.getId()));
    }

    @Test
    void openingGroupConversationMarksOnlyThatConversationRead() {
        UUID teamId = UUID.randomUUID();
        User user = user("reader");
        when(notificationService.markChatConversationRead(user.getId(), teamId, null)).thenReturn(3);

        var response = controller.markConversationRead(
                teamId, Map.of("conversationType", "GROUP"), user);

        assertEquals(200, response.getStatusCode().value());
        verify(notificationService).markChatConversationRead(user.getId(), teamId, null);
    }

    private User user(String username) {
        User user = new User();
        user.setId(UUID.randomUUID());
        user.setUsername(username);
        user.setFullName(username);
        return user;
    }

    private TeamMember member(Team team, User user) {
        TeamMember member = new TeamMember();
        member.setTeam(team);
        member.setUser(user);
        return member;
    }
}
