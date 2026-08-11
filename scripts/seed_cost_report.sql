BEGIN;

DELETE FROM costs
WHERE created_by IN ('demo_cost_seed_an_phu', 'orca_infrastructure_seed_202608');

DELETE FROM cost_categories category
WHERE NOT EXISTS (
    SELECT 1
    FROM costs cost
    WHERE cost.category_id = category.id
)
AND category.name NOT IN (
    'Máy chủ & lưu trữ',
    'Cơ sở dữ liệu',
    'AI API',
    'Email & thông báo',
    'Tên miền & bảo mật',
    'Giám sát hệ thống'
);

INSERT INTO cost_categories (id, created_at, description, name, status)
SELECT gen_random_uuid(), NOW(), source.description, source.name, 'ACTIVE'
FROM (
    VALUES
        ('Máy chủ & lưu trữ', 'Máy chủ ứng dụng, CDN và lưu trữ tệp'),
        ('Cơ sở dữ liệu', 'PostgreSQL, sao lưu và khôi phục dữ liệu'),
        ('AI API', 'Dịch vụ AI hỗ trợ lập kế hoạch và điều phối'),
        ('Email & thông báo', 'Email giao dịch và thông báo hệ thống'),
        ('Tên miền & bảo mật', 'Tên miền, SSL và các dịch vụ bảo mật'),
        ('Giám sát hệ thống', 'Theo dõi lỗi, hiệu năng và nhật ký vận hành')
) AS source(name, description)
ON CONFLICT (name) DO UPDATE
SET description = EXCLUDED.description,
    status = 'ACTIVE';

WITH infrastructure_costs(category_name, name, amount, paid_at, payer, description) AS (
    VALUES
        ('Máy chủ & lưu trữ', 'Máy chủ ứng dụng ORCA tháng 08/2026', 300000::numeric, TIMESTAMP '2026-08-02 09:00:00', 'Administrator', 'Máy chủ chạy frontend, backend và dịch vụ API của ORCA'),
        ('Cơ sở dữ liệu', 'PostgreSQL và sao lưu dữ liệu', 180000::numeric, TIMESTAMP '2026-08-03 09:00:00', 'Administrator', 'Cơ sở dữ liệu chính và bản sao lưu định kỳ'),
        ('AI API', 'Hạn mức AI hỗ trợ điều phối', 220000::numeric, TIMESTAMP '2026-08-05 09:00:00', 'Administrator', 'Chi phí gọi mô hình AI cho tính năng trợ lý và lập kế hoạch'),
        ('Email & thông báo', 'Email giao dịch và thông báo', 120000::numeric, TIMESTAMP '2026-08-07 09:00:00', 'Administrator', 'Email xác thực, thông báo tài khoản và trạng thái thanh toán'),
        ('Tên miền & bảo mật', 'Tên miền, SSL và bảo mật cơ bản', 100000::numeric, TIMESTAMP '2026-08-09 09:00:00', 'Administrator', 'Phân bổ tên miền, chứng chỉ SSL và bảo vệ truy cập'),
        ('Giám sát hệ thống', 'Theo dõi lỗi và nhật ký ứng dụng', 80000::numeric, TIMESTAMP '2026-08-10 09:00:00', 'Administrator', 'Giám sát uptime, lỗi backend và hiệu năng hệ thống'),
        ('Máy chủ & lưu trữ', 'CDN và lưu trữ tệp phát sinh', 50000::numeric, TIMESTAMP '2026-08-11 16:30:00', 'Administrator', 'Băng thông CDN và lưu trữ hình ảnh phát sinh trong ngày')
)
INSERT INTO costs (
    id, amount, created_at, created_by, currency, date, description,
    name, payer, status, category_id
)
SELECT
    gen_random_uuid(), current_cost.amount, NOW(), 'orca_infrastructure_seed_202608',
    'VND', current_cost.paid_at, current_cost.description, current_cost.name,
    current_cost.payer, 'PAID', category.id
FROM infrastructure_costs current_cost
JOIN cost_categories category ON category.name = current_cost.category_name;

COMMIT;
