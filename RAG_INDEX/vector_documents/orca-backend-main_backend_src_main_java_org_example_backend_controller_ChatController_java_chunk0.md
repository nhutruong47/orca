# Knowledge Document: ChatController.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ChatController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "notification",
  "tags": [
    "notification",
    "authentication",
    "security",
    "chat"
  ],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, authentication, security, chat

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.ChatMessageDTO;
import org.example.backend.entity.User;
import org.example.backend.service.ChatService;
import org.example.backend.service.NotificationService;
import org.example.backend.service.PresenceService;
import org.springframework.http.ResponseEntity;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/api")
public class ChatController {

    private final ChatService chatService;
    private final SimpMessagingTemplate messagingTemplate;
    private final PresenceService presenceService;
    private final NotificationService notificationService;

    public ChatController(ChatService chatService, SimpMessagingTemplate messagingTemplate,
                          PresenceService presenceService, NotificationService notificationService) {
        this.chatService = chatService;
        this.messagingTemplate = messagingTemplate;
        this.presenceService = presenceService;
        this.notificationService = notificationService;
    }

    /** Get group chat messages */
    @GetMapping("/teams/{teamId}/chat")
    public ResponseEntity<List<ChatMessageDTO>> getGroupMessages(@PathVariable UUID teamId) {
        return ResponseEntity.ok(chatService.getGroupMessages(teamId));
    }

    /** Get DM with a specific user */
    @GetMapping("/teams/{teamId}/chat/dm/{userId}")
    public ResponseEntity<List<ChatMessageDTO>> getDirectMessages(
            @PathVariable UUID teamId,
            @PathVariable UUID userId,
            @AuthenticationPrincipal User currentUser) {
        return ResponseEntity.ok(chatService.getDirectMessages(teamId, currentUser.getId(), userId));
    }

    /** Get last DM message for each contact */
    @GetMapping("/teams/{teamId}/chat/dm-previews")
    public ResponseEntity<List<ChatMessageDTO>> getDmPreviews(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        return ResponseEntity.ok(chatService.getLastDmMessages(teamId, currentUser.getId()));
    }

    /** Send a message (group or DM) — also broadcasts via WebSocket */
    @PostMapping("/teams/{teamId}/chat")

```
