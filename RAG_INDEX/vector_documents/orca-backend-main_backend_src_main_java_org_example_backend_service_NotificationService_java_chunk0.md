# Knowledge Document: NotificationService.java (Chunk 1/2)

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
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: notification

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.NotificationDTO;
import org.example.backend.entity.Notification;
import org.example.backend.entity.User;
import org.example.backend.repository.NotificationRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class NotificationService {

    private final NotificationRepository notifRepo;
    private final SimpMessagingTemplate messagingTemplate;
    private final UserRepository userRepo;

    public NotificationService(NotificationRepository notifRepo, SimpMessagingTemplate messagingTemplate, UserRepository userRepo) {
        this.notifRepo = notifRepo;
        this.messagingTemplate = messagingTemplate;
        this.userRepo = userRepo;
    }

    /** Create and broadcast a notification */
    public NotificationDTO createAndSend(User user, String title, String message, String type, UUID taskId) {
        Notification n = new Notification();
        n.setUser(user);
        n.setTitle(title);
        n.setMessage(message);
        n.setType(type);
        n.setTaskId(taskId);
        n.setIsRead(false);
        Notification saved = notifRepo.save(n);

        NotificationDTO dto = toDTO(saved);
        // Broadcast via WebSocket
        messagingTemplate.convertAndSend("/topic/user/" + user.getId() + "/notifications", dto);
        return dto;
    }

    /** Overload accepting userId as UUID */
    public NotificationDTO createAndSend(UUID userId, String title, String message, String type, UUID taskId) {
        User user = userRepo.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found: " + userId));
        return createAndSend(user, title, message, type, taskId);
    }

    public List<NotificationDTO> getByUser(UUID userId) {
        return notifRepo.findByUserIdOrderByCreatedAtDesc(userId)
                .stream().map(this::toDTO).collect(Collectors.toList());
    }

    public long getUnreadCount(UUID userId) {
        return notifRepo.countByUserIdAndIsReadFalse(userId);
    }

    public void markAsRead(UUID notificationId) {
        notifRepo.findById(notificationId).ifPresent(n -> {
            n.setIsRead(true);

```
