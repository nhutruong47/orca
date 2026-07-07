# Knowledge Document: ChatService.java (Chunk 2/2)

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
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: chat

## Source Code Chunk
```java
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
        dto.setId(m.getId().toString());
        dto.setTeamId(m.getTeam().getId().toString());
        dto.setSenderId(m.getSender().getId().toString());
        dto.setSenderName(m.getSender().getFullName() != null ? m.getSender().getFullName() : m.getSender().getUsername());
        if (m.getRecipient() != null) {
            dto.setRecipientId(m.getRecipient().getId().toString());
            dto.setRecipientName(m.getRecipient().getFullName() != null ? m.getRecipient().getFullName() : m.getRecipient().getUsername());
        }
        dto.setContent(m.getContent());
        dto.setCreatedAt(m.getCreatedAt());
        return dto;
    }
}

```
