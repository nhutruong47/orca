\set ON_ERROR_STOP on

BEGIN;

-- Mẻ đã hoàn thành trong tuần chấm công 03–07/08/2026.
UPDATE goals
SET title = 'Mẻ rang Arabica 03–07/08/2026',
    status = 'DONE',
    created_at = TIMESTAMP '2026-08-03 08:00:00',
    deadline = TIMESTAMP '2026-08-07 17:00:00',
    total_tasks = 4,
    completed_tasks = 4
WHERE id = 'aa8b1197-3c3f-4dd9-89c3-644f7b794c83';

UPDATE tasks
SET status = 'COMPLETED',
    acceptance_status = 'ACCEPTED',
    completion_percentage = 100,
    actual_workload = workload,
    actual_output = 120,
    created_at = CASE id
        WHEN '3a24353f-13b3-442a-a601-0cc081d7ca64' THEN TIMESTAMP '2026-08-03 08:15:00'
        WHEN 'bd9f6655-98ba-492d-a56b-6262c098bcae' THEN TIMESTAMP '2026-08-04 08:00:00'
        WHEN 'a3fe5a87-82f5-4ee0-8749-618abd1e5f99' THEN TIMESTAMP '2026-08-06 09:00:00'
        WHEN '51bcac75-36bc-407b-a1ee-3df02fb76f79' THEN TIMESTAMP '2026-08-07 08:00:00'
        ELSE created_at
    END,
    deadline = CASE id
        WHEN '3a24353f-13b3-442a-a601-0cc081d7ca64' THEN TIMESTAMP '2026-08-03 17:00:00'
        WHEN 'bd9f6655-98ba-492d-a56b-6262c098bcae' THEN TIMESTAMP '2026-08-05 17:00:00'
        WHEN 'a3fe5a87-82f5-4ee0-8749-618abd1e5f99' THEN TIMESTAMP '2026-08-06 17:00:00'
        WHEN '51bcac75-36bc-407b-a1ee-3df02fb76f79' THEN TIMESTAMP '2026-08-07 17:00:00'
        ELSE deadline
    END
WHERE goal_id = 'aa8b1197-3c3f-4dd9-89c3-644f7b794c83';

-- Mẻ đang thực hiện: nguyên liệu đã chuẩn bị, công đoạn rang đạt 67%.
UPDATE goals
SET title = 'Mẻ rang Arabica 13–14/08/2026',
    status = 'IN_PROGRESS',
    deadline = TIMESTAMP '2026-08-14 17:00:00',
    total_tasks = 4,
    completed_tasks = 1
WHERE id = '470b3c0d-b013-40b8-a44b-1a10862ebf32';

UPDATE tasks
SET status = 'COMPLETED',
    acceptance_status = 'ACCEPTED',
    completion_percentage = 100,
    actual_workload = workload,
    actual_output = 120,
    deadline = TIMESTAMP '2026-08-13 10:00:00'
WHERE id = '200548d7-fdd3-43a3-850d-8257fa0b4537';

UPDATE tasks
SET status = 'IN_PROGRESS',
    acceptance_status = 'ACCEPTED',
    completion_percentage = 67,
    actual_workload = 2.7,
    actual_output = 80,
    deadline = TIMESTAMP '2026-08-14 14:00:00'
WHERE id = 'c0294e04-3c5d-4776-b0fa-d07001014a3e';

UPDATE tasks
SET status = 'READY',
    acceptance_status = 'WAITING',
    completion_percentage = 0,
    actual_workload = NULL,
    actual_output = 0,
    deadline = CASE id
        WHEN 'dda14343-dc6b-4c30-a2e6-08edbad8829b' THEN TIMESTAMP '2026-08-14 15:30:00'
        WHEN '1ec1d276-c53f-4a7d-ae8d-16db40438c7b' THEN TIMESTAMP '2026-08-14 17:00:00'
        ELSE deadline
    END
WHERE id IN (
    'dda14343-dc6b-4c30-a2e6-08edbad8829b',
    '1ec1d276-c53f-4a7d-ae8d-16db40438c7b'
);

-- Mẻ kế tiếp giữ ở trạng thái kế hoạch, chưa ghi nhận sản lượng hay giờ thực tế.
UPDATE goals
SET title = 'Kế hoạch rang Arabica 16/08/2026',
    status = 'PENDING',
    deadline = TIMESTAMP '2026-08-16 17:00:00',
    total_tasks = 4,
    completed_tasks = 0
WHERE id = '8e51a38b-c824-4ea2-9f0f-2553b5d1e611';

UPDATE tasks
SET status = 'READY',
    acceptance_status = 'WAITING',
    completion_percentage = 0,
    actual_workload = NULL,
    actual_output = 0,
    deadline = TIMESTAMP '2026-08-16 17:00:00'
WHERE goal_id = '8e51a38b-c824-4ea2-9f0f-2553b5d1e611';

COMMIT;

SELECT
    g.title,
    g.status,
    g.completed_tasks || '/' || g.total_tasks AS progress,
    count(*) FILTER (WHERE t.status = 'COMPLETED') AS completed,
    count(*) FILTER (WHERE t.status = 'IN_PROGRESS') AS in_progress,
    count(*) FILTER (WHERE t.status = 'READY') AS ready
FROM goals g
JOIN tasks t ON t.goal_id = g.id
WHERE g.id IN (
    'aa8b1197-3c3f-4dd9-89c3-644f7b794c83',
    '470b3c0d-b013-40b8-a44b-1a10862ebf32',
    '8e51a38b-c824-4ea2-9f0f-2553b5d1e611'
)
GROUP BY g.id
ORDER BY g.created_at;
