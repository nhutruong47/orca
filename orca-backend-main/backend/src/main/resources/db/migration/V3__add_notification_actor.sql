ALTER TABLE notifications
    ADD COLUMN IF NOT EXISTS actor_id UUID;

CREATE INDEX IF NOT EXISTS idx_notifications_chat_conversation
    ON notifications (user_id, task_id, actor_id, is_read)
    WHERE type = 'CHAT_MESSAGE';
