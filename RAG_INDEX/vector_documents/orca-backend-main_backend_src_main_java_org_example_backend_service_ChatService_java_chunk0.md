# Knowledge Document: ChatService.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/ChatService.java",
  "language": "java",
  "module": "service",
  "business_domain": "chat",
  "tags": [
    "chat"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: chat

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.ChatMessageDTO;
import org.example.backend.entity.ChatMessage;
import org.example.backend.entity.User;
import org.example.backend.repository.ChatMessageRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class ChatService {

    private final ChatMessageRepository chatRepo;
    private final TeamRepository teamRepo;
    private final UserRepository userRepo;

    public ChatService(ChatMessageRepository chatRepo, TeamRepository teamRepo, UserRepository userRepo) {
        this.chatRepo = chatRepo;
        this.teamRepo = teamRepo;
        this.userRepo = userRepo;
    }

    /** Get group chat messages */
    public List<ChatMessageDTO> getGroupMessages(UUID teamId) {
        return chatRepo.findByTeamIdAndRecipientIsNullOrderByCreatedAtAsc(teamId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    /** Get direct messages between two users */
    public List<ChatMessageDTO> getDirectMessages(UUID teamId, UUID userId1, UUID userId2) {
        return chatRepo.findDirectMessages(teamId, userId1, userId2)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    /** Get last DM message per contact (for DM preview list) */
    public List<ChatMessageDTO> getLastDmMessages(UUID teamId, UUID userId) {
        return chatRepo.findLastDmMessages(teamId, userId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    /** Send a message (group or DM) */
    public ChatMessageDTO sendMessage(UUID teamId, User sender, UUID recipientId, String content) {
        ChatMessage msg = new ChatMessage();
        msg.setTeam(teamRepo.findById(teamId).orElseThrow(() -> new RuntimeException("Team not found")));
        msg.setSender(sender);

        if (recipientId != null) {
            msg.setRecipient(userRepo.findById(recipientId)
                    .orElseThrow(() -> new RuntimeException("Recipient not found")));
        }

        msg.setContent(content);
        return toDTO(chatRepo.save(msg));
    }

    private ChatMessageDTO toDTO(ChatMessage m) {
        ChatMessageDTO dto = new ChatMessageDTO();

```
