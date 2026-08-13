package org.example.backend.service;

import org.example.backend.repository.NotificationRepository;
import org.example.backend.repository.UserRepository;
import org.junit.jupiter.api.Test;
import org.springframework.messaging.simp.SimpMessagingTemplate;

import java.util.UUID;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

class NotificationServiceChatTest {

    @Test
    void markGroupConversationUsesNullActorQuery() {
        NotificationRepository repository = mock(NotificationRepository.class);
        NotificationService service = new NotificationService(
                repository, mock(SimpMessagingTemplate.class), mock(UserRepository.class));
        UUID userId = UUID.randomUUID();
        UUID teamId = UUID.randomUUID();
        when(repository.markGroupChatRead(userId, teamId)).thenReturn(4);

        assertEquals(4, service.markChatConversationRead(userId, teamId, null));
        verify(repository).markGroupChatRead(userId, teamId);
        verify(repository, never()).markDirectChatRead(any(), any(), any());
    }

    @Test
    void markDirectConversationUsesActorQuery() {
        NotificationRepository repository = mock(NotificationRepository.class);
        NotificationService service = new NotificationService(
                repository, mock(SimpMessagingTemplate.class), mock(UserRepository.class));
        UUID userId = UUID.randomUUID();
        UUID teamId = UUID.randomUUID();
        UUID actorId = UUID.randomUUID();
        when(repository.markDirectChatRead(userId, teamId, actorId)).thenReturn(2);

        assertEquals(2, service.markChatConversationRead(userId, teamId, actorId));
        verify(repository).markDirectChatRead(userId, teamId, actorId);
        verify(repository, never()).markGroupChatRead(any(), any());
    }
}
