BEGIN;

DELETE FROM system_logs
WHERE (action_type = 'PAYMENT_COMPLETED' AND target_id IN (SELECT id::text FROM payment_transactions))
   OR (action_type = 'TEAM_CREATED' AND target_id IN (SELECT id::text FROM teams))
   OR (action_type = 'COST_RECORDED' AND target_id IN (
       SELECT id::text FROM costs WHERE created_by = 'orca_infrastructure_seed_202608'
   ));

INSERT INTO system_logs (id, actor_id, actor_name, action_type, target_id, details, created_at)
SELECT
    gen_random_uuid(),
    payment.user_id,
    COALESCE(NULLIF(account.full_name, ''), account.username),
    'PAYMENT_COMPLETED',
    payment.id::text,
    'Thanh toán gói ' || UPPER(payment.plan_id) || ' · ' ||
        to_char(payment.amount, 'FM999G999G999') || ' VND · ' || payment.txn_ref,
    COALESCE(payment.paid_at, payment.created_at)
FROM payment_transactions payment
JOIN users account ON account.id = payment.user_id
WHERE payment.status = 'PAID';

INSERT INTO system_logs (id, actor_id, actor_name, action_type, target_id, details, created_at)
SELECT
    gen_random_uuid(),
    team.owner_id,
    COALESCE(NULLIF(owner_account.full_name, ''), owner_account.username),
    'TEAM_CREATED',
    team.id::text,
    'Tạo doanh nghiệp ' || team.name,
    team.created_at
FROM teams team
JOIN users owner_account ON owner_account.id = team.owner_id;

INSERT INTO system_logs (id, actor_id, actor_name, action_type, target_id, details, created_at)
SELECT
    gen_random_uuid(),
    admin_account.id,
    COALESCE(NULLIF(admin_account.full_name, ''), admin_account.username),
    'COST_RECORDED',
    cost.id::text,
    cost.name || ' · ' || to_char(cost.amount, 'FM999G999G999') || ' VND',
    COALESCE(cost.date, cost.created_at)
FROM costs cost
CROSS JOIN LATERAL (
    SELECT id, full_name, username
    FROM users
    WHERE role = 'ADMIN'
    ORDER BY created_at NULLS LAST
    LIMIT 1
) admin_account
WHERE cost.created_by = 'orca_infrastructure_seed_202608';

COMMIT;
