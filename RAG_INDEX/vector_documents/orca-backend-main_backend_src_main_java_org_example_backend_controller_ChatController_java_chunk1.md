# Knowledge Document: ChatController.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, authentication, security, chat

## Source Code Chunk
```java
teamId}/chat/dm-previews")
    public ResponseEntity<List<ChatMessageDTO>> getDmPreviews(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        return ResponseEntity.ok(chatService.getLastDmMessages(teamId, currentUser.getId()));
    }

    /** Send a message (group or DM) — also broadcasts via WebSocket */
    @PostMapping("/teams/{teamId}/chat")
    public ResponseEntity<ChatMessageDTO> sendMessage(
            @PathVariable UUID teamId,
            @RequestBody Map<String, String> body,
            @AuthenticationPrincipal User currentUser) {
        String content = body.get("content");
        String recipientIdStr = body.get("recipientId");

        if (content == null || content.isBlank()) {
            return ResponseEntity.badRequest().build();
        }

        UUID recipientId = null;
        if (recipientIdStr != null && !recipientIdStr.isBlank()) {
            recipientId = UUID.fromString(recipientIdStr);
        }

        ChatMessageDTO saved = chatService.sendMessage(teamId, currentUser, recipientId, content);

        // Broadcast via WebSocket
        if (recipientId == null) {
            // Group message → broadcast to /topic/team/{teamId}
            messagingTemplate.convertAndSend("/topic/team/" + teamId, saved);
        } else {
            // DM → broadcast to both sender and recipient private channels
            messagingTemplate.convertAndSend("/topic/dm/" + teamId + "/" + currentUser.getId() + "/" + recipientId, saved);
            messagingTemplate.convertAndSend("/topic/dm/" + teamId + "/" + recipientId + "/" + currentUser.getId(), saved);

            // Send DM notification to recipient
            String senderName = currentUser.getFullName() != null ? currentUser.getFullName() : currentUser.getUsername();
            String preview = content.length() > 50 ? content.substring(0, 50) + "..." : content;
            notificationService.createAndSend(
                    recipientId,
                    "Tin nhắn mới từ " + senderName,
                    preview,
                    "CHAT_MESSAGE",
                    null
            );
        }

        return ResponseEntity.ok(saved);
    }

    /** Get online users */
    @GetMapping("/presence/online")
    public ResponseEntity<Set<String>> getOnlineUsers() {

```
