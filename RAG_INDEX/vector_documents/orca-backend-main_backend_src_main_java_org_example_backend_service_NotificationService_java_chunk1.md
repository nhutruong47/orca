# Knowledge Document: NotificationService.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/NotificationService.java",
  "language": "java",
  "module": "service",
  "business_domain": "notification",
  "tags": [
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: notification

## Source Code Chunk
```java
      return notifRepo.findByUserIdOrderByCreatedAtDesc(userId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public long getUnreadCount(UUID userId) {
        return notifRepo.countByUserIdAndIsReadFalse(userId);
    }

    public void markAsRead(UUID notificationId) {
        notifRepo.findById(notificationId).ifPresent(n -> {
            n.setIsRead(true);
            notifRepo.save(n);
        });
    }

    public void markAllRead(UUID userId) {
        List<Notification> unread = notifRepo.findByUserIdOrderByCreatedAtDesc(userId)
                .stream().filter(n -> !n.getIsRead()).collect(Collectors.toList());
        unread.forEach(n -> n.setIsRead(true));
        notifRepo.saveAll(unread);
    }

    private NotificationDTO toDTO(Notification n) {
        NotificationDTO dto = new NotificationDTO();
        dto.setId(n.getId().toString());
        dto.setTitle(n.getTitle());
        dto.setMessage(n.getMessage());
        dto.setType(n.getType());
        dto.setTaskId(n.getTaskId() != null ? n.getTaskId().toString() : null);
        dto.setRead(n.getIsRead());
        dto.setCreatedAt(n.getCreatedAt());
        return dto;
    }
}

```
