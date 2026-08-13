package org.example.backend.repository;

import org.example.backend.entity.Notification;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.UUID;

public interface NotificationRepository extends JpaRepository<Notification, UUID> {
    List<Notification> findByUserIdOrderByCreatedAtDesc(UUID userId);
    long countByUserIdAndIsReadFalse(UUID userId);

    @Modifying(clearAutomatically = true, flushAutomatically = true)
    @Query("UPDATE Notification n SET n.isRead = true " +
           "WHERE n.user.id = :userId AND n.type = 'CHAT_MESSAGE' " +
           "AND n.taskId = :teamId AND n.actorId IS NULL AND n.isRead = false")
    int markGroupChatRead(@Param("userId") UUID userId, @Param("teamId") UUID teamId);

    @Modifying(clearAutomatically = true, flushAutomatically = true)
    @Query("UPDATE Notification n SET n.isRead = true " +
           "WHERE n.user.id = :userId AND n.type = 'CHAT_MESSAGE' " +
           "AND n.taskId = :teamId AND n.actorId = :actorId AND n.isRead = false")
    int markDirectChatRead(
            @Param("userId") UUID userId,
            @Param("teamId") UUID teamId,
            @Param("actorId") UUID actorId);
}
