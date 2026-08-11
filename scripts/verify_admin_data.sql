SELECT 'users' AS dataset, COUNT(*)::bigint AS records, NULL::numeric AS total_amount FROM users
UNION ALL
SELECT 'teams', COUNT(*)::bigint, NULL::numeric FROM teams
UNION ALL
SELECT 'team_members', COUNT(*)::bigint, NULL::numeric FROM team_members
UNION ALL
SELECT 'subscription_plans', COUNT(*)::bigint, NULL::numeric FROM subscription_plans
UNION ALL
SELECT 'paid_payments', COUNT(*)::bigint, COALESCE(SUM(amount), 0)::numeric FROM payment_transactions WHERE status = 'PAID'
UNION ALL
SELECT 'active_costs', COUNT(*)::bigint, COALESCE(SUM(amount), 0)::numeric FROM costs WHERE status <> 'CANCELLED'
UNION ALL
SELECT 'system_logs', COUNT(*)::bigint, NULL::numeric FROM system_logs
ORDER BY dataset;

SELECT 'orphan_payment_users' AS integrity_check, COUNT(*) AS violations
FROM payment_transactions payment
LEFT JOIN users account ON account.id = payment.user_id
WHERE account.id IS NULL
UNION ALL
SELECT 'orphan_team_members', COUNT(*)
FROM team_members member
LEFT JOIN teams team ON team.id = member.team_id
LEFT JOIN users account ON account.id = member.user_id
WHERE team.id IS NULL OR account.id IS NULL
UNION ALL
SELECT 'duplicate_team_members', COUNT(*)
FROM (
    SELECT team_id, user_id
    FROM team_members
    GROUP BY team_id, user_id
    HAVING COUNT(*) > 1
) duplicate
UNION ALL
SELECT 'team_owner_not_member', COUNT(*)
FROM teams team
LEFT JOIN team_members member
    ON member.team_id = team.id AND member.user_id = team.owner_id
WHERE member.id IS NULL
UNION ALL
SELECT 'orphan_cost_categories', COUNT(*)
FROM costs cost
LEFT JOIN cost_categories category ON category.id = cost.category_id
WHERE category.id IS NULL
UNION ALL
SELECT 'paid_plan_user_mismatch', COUNT(*)
FROM payment_transactions payment
JOIN users account ON account.id = payment.user_id
WHERE payment.status = 'PAID'
  AND LOWER(COALESCE(account.ai_plan, 'free')) <> LOWER(payment.plan_id);
