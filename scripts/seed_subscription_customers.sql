BEGIN;

WITH customer_data(username, full_name, email, plan_id, created_at, expires_at) AS (
    VALUES
        ('nguyen.hoang.phuc', 'Nguyễn Hoàng Phúc', 'phuc@minhsoncoffee.vn', 'plus', TIMESTAMP '2026-08-01 08:30:00', NULL::timestamp),
        ('tran.mai.anh', 'Trần Mai Anh', 'mai.anh@dalatbrew.vn', 'plus', TIMESTAMP '2026-08-02 09:10:00', NULL::timestamp),
        ('le.duc.khanh', 'Lê Đức Khánh', 'khanh@caonguyenroastery.vn', 'enterprise', TIMESTAMP '2026-08-04 10:20:00', TIMESTAMP '2026-09-04 10:20:00'),
        ('pham.ngoc.han', 'Phạm Ngọc Hân', 'han@maycoffee.vn', 'plus', TIMESTAMP '2026-08-05 13:15:00', NULL::timestamp),
        ('vo.thanh.dat', 'Võ Thành Đạt', 'dat@phuongnamcoffee.vn', 'plus', TIMESTAMP '2026-08-07 08:45:00', NULL::timestamp),
        ('bui.thu.ha', 'Bùi Thu Hà', 'ha@anlaccoffee.vn', 'enterprise', TIMESTAMP '2026-08-08 14:00:00', TIMESTAMP '2026-09-08 14:00:00'),
        ('dang.quoc.huy', 'Đặng Quốc Huy', 'huy@banmebeans.vn', 'plus', TIMESTAMP '2026-08-09 09:25:00', NULL::timestamp)
)
INSERT INTO users (
    id, ai_plan, ai_plan_expires_at, ai_trial_start_date, ai_usage_count,
    cancelled_orders, chip_id, completed_orders, created_at, email,
    full_name, locked, password, role, total_orders, username
)
SELECT
    gen_random_uuid(), customer.plan_id, customer.expires_at, NULL, 0,
    0, gen_random_uuid()::text, 0, customer.created_at, customer.email,
    customer.full_name, FALSE,
    (SELECT password FROM users WHERE username = 'nguyen.minh.hai'),
    'MEMBER', 0, customer.username
FROM customer_data customer
ON CONFLICT (username) DO UPDATE
SET full_name = EXCLUDED.full_name,
    email = EXCLUDED.email,
    ai_plan = EXCLUDED.ai_plan,
    ai_plan_expires_at = EXCLUDED.ai_plan_expires_at,
    ai_usage_count = 0,
    locked = FALSE;

WITH payment_data(
    username, txn_ref, plan_id, amount, bank_code, payment_method,
    vnp_transaction_no, created_at, paid_at
) AS (
    VALUES
        ('nguyen.hoang.phuc', 'ORCA-PAY-260802-1001', 'plus', 129000::bigint, 'VCB', 'VNPAY', '14862001', TIMESTAMP '2026-08-02 10:02:00', TIMESTAMP '2026-08-02 10:05:00'),
        ('tran.mai.anh', 'ORCA-PAY-260803-1002', 'plus', 129000::bigint, 'MB', 'VNPAY', '14863002', TIMESTAMP '2026-08-03 14:18:00', TIMESTAMP '2026-08-03 14:21:00'),
        ('le.duc.khanh', 'ORCA-PAY-260805-1003', 'enterprise', 249000::bigint, 'TCB', 'PAYOS', '14865003', TIMESTAMP '2026-08-05 09:42:00', TIMESTAMP '2026-08-05 09:46:00'),
        ('pham.ngoc.han', 'ORCA-PAY-260806-1004', 'plus', 129000::bigint, 'ACB', 'VNPAY', '14866004', TIMESTAMP '2026-08-06 16:07:00', TIMESTAMP '2026-08-06 16:10:00'),
        ('vo.thanh.dat', 'ORCA-PAY-260808-1005', 'plus', 129000::bigint, 'BIDV', 'VNPAY', '14868005', TIMESTAMP '2026-08-08 11:25:00', TIMESTAMP '2026-08-08 11:29:00'),
        ('bui.thu.ha', 'ORCA-PAY-260809-1006', 'enterprise', 249000::bigint, 'VIB', 'PAYOS', '14869006', TIMESTAMP '2026-08-09 15:33:00', TIMESTAMP '2026-08-09 15:37:00'),
        ('dang.quoc.huy', 'ORCA-PAY-260810-1007', 'plus', 129000::bigint, 'NCB', 'VNPAY', '14861007', TIMESTAMP '2026-08-10 08:52:00', TIMESTAMP '2026-08-10 08:56:00')
)
INSERT INTO payment_transactions (
    id, amount, bank_code, created_at, paid_at, payment_method, plan_id,
    status, txn_ref, vnp_response_code, vnp_transaction_no,
    vnp_transaction_status, user_id
)
SELECT
    gen_random_uuid(), payment.amount, payment.bank_code, payment.created_at,
    payment.paid_at, payment.payment_method, payment.plan_id, 'PAID',
    payment.txn_ref, '00', payment.vnp_transaction_no, '00', user_account.id
FROM payment_data payment
JOIN users user_account ON user_account.username = payment.username
ON CONFLICT (txn_ref) DO UPDATE
SET amount = EXCLUDED.amount,
    bank_code = EXCLUDED.bank_code,
    paid_at = EXCLUDED.paid_at,
    payment_method = EXCLUDED.payment_method,
    plan_id = EXCLUDED.plan_id,
    status = 'PAID',
    vnp_response_code = '00',
    vnp_transaction_no = EXCLUDED.vnp_transaction_no,
    vnp_transaction_status = '00',
    user_id = EXCLUDED.user_id;

COMMIT;
