# Knowledge Document: ChatController.java (Chunk 3/3)

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
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: notification, authentication, security, chat

## Source Code Chunk
```java
ationService.createAndSend(
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
        return ResponseEntity.ok(presenceService.getOnlineUserIds());
    }
}

```
