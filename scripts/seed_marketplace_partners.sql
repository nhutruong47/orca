\set ON_ERROR_STOP on

BEGIN;

DO $$
BEGIN
    IF (
        SELECT count(*)
        FROM users
        WHERE username IN (
            'nguyen.hoang.phuc', 'tran.mai.anh', 'le.duc.khanh',
            'pham.ngoc.han', 'vo.thanh.dat', 'bui.thu.ha', 'dang.quoc.huy'
        )
    ) <> 7 THEN
        RAISE EXCEPTION 'Missing one or more marketplace owner accounts';
    END IF;
END $$;

WITH partner_data (
    id, username, name, description, created_at, specialty, region,
    capacity_value, capacity_unit, image_url, image_gallery,
    business_license, business_address, website_url, facebook_url,
    certificates, completed_orders, cancelled_orders, total_orders,
    on_time_orders, late_orders, total_ratings, sum_ratings, invite_code,
    moq, lead_time, years_in_operation, status_badge, employee_count,
    factory_size, service_cost, metadata
) AS (
    VALUES
    (
        'a1000000-0000-4000-8000-000000000001'::uuid,
        'nguyen.hoang.phuc',
        'Công ty Cà phê Minh Sơn',
        'Đơn vị thu mua, sơ chế và phân loại cà phê nhân tại Bảo Lộc; phù hợp các đơn nguyên liệu theo lô nhỏ và vừa.',
        '2026-08-01 08:45:00'::timestamp,
        'Cung ứng cà phê nhân, Sơ chế, Phân loại hạt',
        'Bảo Lộc, Lâm Đồng',
        1800.0, 'kg/tháng',
        'https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1200&q=85',
        '["https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=1200&q=85","https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=1200&q=85"]',
        'MS-CF-2021-018', '128 Nguyễn Văn Cừ, Bảo Lộc, Lâm Đồng',
        'https://minhsoncoffee.vn', 'https://facebook.com/minhsoncoffee',
        'VietGAP, 4C',
        27, 2, 29, 25, 2, 18, 84.6, 'MS2026', '60 kg', '3 - 5 ngày', 5,
        'Receiving Orders', 12, '420 m²', 16500.0,
        '{"capabilitiesMock":{"services":["Cung ứng cà phê nhân","Sơ chế","Phân loại hạt"],"coffeeTypes":["Arabica","Robusta","Catimor"],"packagingFormats":["Bao đay 60 kg","Bao GrainPro 30 kg"]},"equipmentMock":{"roasters":[],"packaging":["Máy đóng bao định lượng"],"grinders":[],"qc":["Máy đo độ ẩm","Sàng phân loại"]}}'
    ),
    (
        'a1000000-0000-4000-8000-000000000002'::uuid,
        'tran.mai.anh',
        'Đà Lạt Brew Lab',
        'Xưởng rang mẻ nhỏ chuyên cà phê đặc sản Cầu Đất, phát triển profile rang và kiểm soát chất lượng theo từng lô.',
        '2026-08-02 09:25:00'::timestamp,
        'Rang cà phê, Kiểm soát chất lượng, Cupping',
        'Đà Lạt, Lâm Đồng',
        1200.0, 'kg/tháng',
        'https://images.unsplash.com/photo-1514432324607-a09d9b4aefda?w=1200&q=85',
        '["https://images.unsplash.com/photo-1514432324607-a09d9b4aefda?w=1200&q=85","https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=1200&q=85"]',
        'DL-BL-2022-026', '42 Trần Hưng Đạo, Đà Lạt, Lâm Đồng',
        'https://dalatbrew.vn', 'https://facebook.com/dalatbrewlab',
        'HACCP, SCA Roasting',
        39, 2, 41, 37, 2, 24, 115.2, 'DL2026', '30 kg', '4 - 7 ngày', 4,
        'Receiving Orders', 10, '350 m²', 24000.0,
        '{"capabilitiesMock":{"services":["Rang cà phê","Phát triển profile rang","Cupping"],"coffeeTypes":["Arabica Cầu Đất","Catimor","Typica"],"packagingFormats":["Túi van 250 g","Túi van 500 g","Túi 1 kg"]},"equipmentMock":{"roasters":["Giesen W15","Probat P12"],"packaging":["Máy hàn miệng túi"],"grinders":["Ditting 807"],"qc":["Máy đo màu rang","Bộ cupping SCA"]}}'
    ),
    (
        'a1000000-0000-4000-8000-000000000003'::uuid,
        'le.duc.khanh',
        'Cao Nguyên Roastery',
        'Xưởng rang quy mô vừa nhận gia công OEM, phối trộn và đóng gói cho quán cà phê, văn phòng và chuỗi bán lẻ.',
        '2026-08-04 10:35:00'::timestamp,
        'Rang cà phê, Gia công OEM, Phối trộn, Đóng gói',
        'Buôn Ma Thuột, Đắk Lắk',
        3000.0, 'kg/tháng',
        'https://images.unsplash.com/photo-1498804103079-a6351b050096?w=1200&q=85',
        '["https://images.unsplash.com/photo-1498804103079-a6351b050096?w=1200&q=85","https://images.unsplash.com/photo-1587293852726-70cdb56c2866?w=1200&q=85"]',
        'CNR-2020-041', '75 Nguyễn Chí Thanh, Buôn Ma Thuột, Đắk Lắk',
        'https://caonguyenroastery.vn', 'https://facebook.com/caonguyenroastery',
        'HACCP, ISO 22000',
        51, 4, 55, 48, 3, 31, 142.6, 'CN2026', '100 kg', '5 - 8 ngày', 6,
        'Receiving Orders', 24, '780 m²', 21500.0,
        '{"capabilitiesMock":{"services":["Rang cà phê","Gia công OEM","Phối trộn","Đóng gói"],"coffeeTypes":["Robusta Fine","Arabica","Culi","House Blend"],"packagingFormats":["Túi 250 g","Túi 500 g","Túi 1 kg","Drip bag"]},"equipmentMock":{"roasters":["Loring S35","Toper 15 kg"],"packaging":["Dây chuyền định lượng bán tự động","Máy in date"],"grinders":["Mahlkönig DK27"],"qc":["Máy đo độ ẩm","Máy đo màu rang"]}}'
    ),
    (
        'a1000000-0000-4000-8000-000000000004'::uuid,
        'pham.ngoc.han',
        'Mây Coffee Studio',
        'Studio cà phê tập trung vào sản phẩm nhãn riêng, thiết kế blend và đóng gói linh hoạt cho thương hiệu mới.',
        '2026-08-05 13:30:00'::timestamp,
        'Gia công OEM, Đóng gói, Phát triển sản phẩm',
        'Thủ Đức, TP. Hồ Chí Minh',
        800.0, 'kg/tháng',
        'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=1200&q=85',
        '["https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=1200&q=85","https://images.unsplash.com/photo-1512568400610-62da28bc8a13?w=1200&q=85"]',
        'MCS-2023-012', '18 Đường số 8, Thủ Đức, TP. Hồ Chí Minh',
        'https://maycoffee.vn', 'https://facebook.com/maycoffeestudio',
        'HACCP',
        18, 1, 19, 17, 1, 14, 63.0, 'MY2026', '25 kg', '5 - 7 ngày', 3,
        'Nearly Full', 9, '280 m²', 28000.0,
        '{"capabilitiesMock":{"services":["Gia công OEM","Đóng gói","Phát triển sản phẩm"],"coffeeTypes":["Arabica","Robusta","House Blend"],"packagingFormats":["Túi van 250 g","Hộp quà","Drip bag"]},"equipmentMock":{"roasters":["Roaster 10 kg"],"packaging":["Máy đóng gói drip bag","Máy dán nhãn"],"grinders":["Máy xay công nghiệp 15 kg/h"],"qc":["Bộ cupping"]}}'
    ),
    (
        'a1000000-0000-4000-8000-000000000005'::uuid,
        'vo.thanh.dat',
        'Phương Nam Coffee Works',
        'Đơn vị gia công trọn gói từ rang, xay đến đóng gói; ưu tiên đơn hàng định kỳ cho nhà hàng và văn phòng.',
        '2026-08-07 09:00:00'::timestamp,
        'Gia công OEM, Rang cà phê, Xay cà phê, Đóng gói',
        'Thuận An, Bình Dương',
        2200.0, 'kg/tháng',
        'https://images.unsplash.com/photo-1504630083234-14187a9df0f5?w=1200&q=85',
        '["https://images.unsplash.com/photo-1504630083234-14187a9df0f5?w=1200&q=85","https://images.unsplash.com/photo-1497515114889-1c06568a37b8?w=1200&q=85"]',
        'PNC-2021-034', '31 Đại lộ Bình Dương, Thuận An, Bình Dương',
        'https://phuongnamcoffee.vn', 'https://facebook.com/phuongnamcoffeeworks',
        'ISO 22000, HACCP',
        34, 2, 36, 32, 2, 21, 96.6, 'PN2026', '80 kg', '5 - 9 ngày', 5,
        'Receiving Orders', 18, '620 m²', 22500.0,
        '{"capabilitiesMock":{"services":["Gia công OEM","Rang cà phê","Xay cà phê","Đóng gói"],"coffeeTypes":["Robusta","Arabica","Culi","Espresso Blend"],"packagingFormats":["Túi 500 g","Túi 1 kg","Túi 5 kg"]},"equipmentMock":{"roasters":["Roaster 30 kg","Roaster 15 kg"],"packaging":["Máy định lượng","Máy hàn liên tục"],"grinders":["Máy xay công nghiệp 40 kg/h"],"qc":["Máy đo độ ẩm","Máy đo màu"]}}'
    ),
    (
        'a1000000-0000-4000-8000-000000000006'::uuid,
        'bui.thu.ha',
        'An Lạc Coffee Packaging',
        'Xưởng chuyên đóng gói cà phê, dán nhãn và hoàn thiện hộp quà; hỗ trợ số lượng tối thiểu thấp cho doanh nghiệp nhỏ.',
        '2026-08-08 14:15:00'::timestamp,
        'Đóng gói, Bao bì, Dán nhãn',
        'Quận 12, TP. Hồ Chí Minh',
        1500.0, 'kg/tháng',
        'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&q=85',
        '["https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&q=85","https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=1200&q=85"]',
        'ALP-2022-022', '96 Hà Huy Giáp, Quận 12, TP. Hồ Chí Minh',
        'https://anlaccoffee.vn', 'https://facebook.com/anlaccoffeepackaging',
        'HACCP, Bao bì an toàn thực phẩm',
        23, 1, 24, 22, 1, 16, 73.6, 'AL2026', '20 kg', '3 - 6 ngày', 4,
        'Receiving Orders', 15, '460 m²', 9500.0,
        '{"capabilitiesMock":{"services":["Đóng gói","Bao bì","Dán nhãn"],"coffeeTypes":["Cà phê hạt","Cà phê bột","Drip coffee"],"packagingFormats":["Túi van 250 g","Túi 500 g","Hộp 10 gói","Hộp quà"]},"equipmentMock":{"roasters":[],"packaging":["Máy đóng gói tự động","Máy in date","Máy dán nhãn"],"grinders":[],"qc":["Cân kiểm tra"]}}'
    ),
    (
        'a1000000-0000-4000-8000-000000000007'::uuid,
        'dang.quoc.huy',
        'Ban Mê Beans',
        'Nhà cung ứng cà phê nhân Robusta và Culi từ vùng Buôn Ma Thuột, có dịch vụ sàng lọc và phối trộn theo yêu cầu.',
        '2026-08-09 09:40:00'::timestamp,
        'Cung ứng cà phê nhân, Phân loại hạt, Phối trộn',
        'Buôn Ma Thuột, Đắk Lắk',
        2500.0, 'kg/tháng',
        'https://images.unsplash.com/photo-1524350876685-274059332603?w=1200&q=85',
        '["https://images.unsplash.com/photo-1524350876685-274059332603?w=1200&q=85","https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=1200&q=85"]',
        'BMB-2020-039', '16 Y Ngông, Buôn Ma Thuột, Đắk Lắk',
        'https://banmebeans.vn', 'https://facebook.com/banmebeans',
        '4C, VietGAP',
        31, 2, 33, 29, 2, 19, 89.3, 'BM2026', '60 kg', '3 - 5 ngày', 6,
        'Receiving Orders', 14, '520 m²', 14500.0,
        '{"capabilitiesMock":{"services":["Cung ứng cà phê nhân","Phân loại hạt","Phối trộn"],"coffeeTypes":["Robusta Fine","Culi Robusta","Robusta Honey"],"packagingFormats":["Bao đay 60 kg","Bao GrainPro 30 kg"]},"equipmentMock":{"roasters":[],"packaging":["Máy đóng bao"],"grinders":[],"qc":["Máy đo độ ẩm","Sàng kích thước","Máy phân loại màu"]}}'
    )
)
INSERT INTO teams (
    id, name, description, created_at, is_published, is_verified,
    specialty, capacity, region, factory_type, capacity_value, capacity_unit,
    factory_image_url, factory_images, verification_status, business_license,
    business_address, website_url, facebook_url, certification_document,
    certificates, verification_reject_reason, completed_orders, cancelled_orders,
    total_orders, on_time_orders, late_orders, total_ratings, sum_ratings,
    invite_code, moq, lead_time, years_in_operation, status_badge, employee_count,
    factory_size, metadata, rating, review_count, service_cost, version, owner_id
)
SELECT
    p.id, p.name, p.description, p.created_at, true, false,
    p.specialty, p.capacity_value::text, p.region, 'roastery',
    p.capacity_value, p.capacity_unit, p.image_url, p.image_gallery,
    'PENDING', 'HỒ SƠ MINH HỌA - KHÔNG CÓ GIÁ TRỊ PHÁP LÝ',
    p.region || ' (dữ liệu minh họa)', NULL,
    NULL, NULL, NULL, NULL,
    p.completed_orders, p.cancelled_orders, p.total_orders, p.on_time_orders,
    p.late_orders, p.total_ratings, p.sum_ratings, p.invite_code, p.moq,
    p.lead_time, p.years_in_operation, p.status_badge, p.employee_count,
    p.factory_size, p.metadata, round((p.sum_ratings / p.total_ratings)::numeric, 1),
    p.total_ratings, p.service_cost, 0, u.id
FROM partner_data p
JOIN users u ON u.username = p.username
ON CONFLICT (id) DO UPDATE SET
    name = EXCLUDED.name,
    description = EXCLUDED.description,
    is_published = EXCLUDED.is_published,
    is_verified = EXCLUDED.is_verified,
    specialty = EXCLUDED.specialty,
    capacity = EXCLUDED.capacity,
    region = EXCLUDED.region,
    factory_type = EXCLUDED.factory_type,
    capacity_value = EXCLUDED.capacity_value,
    capacity_unit = EXCLUDED.capacity_unit,
    factory_image_url = EXCLUDED.factory_image_url,
    factory_images = EXCLUDED.factory_images,
    verification_status = EXCLUDED.verification_status,
    business_license = EXCLUDED.business_license,
    business_address = EXCLUDED.business_address,
    website_url = EXCLUDED.website_url,
    facebook_url = EXCLUDED.facebook_url,
    certification_document = EXCLUDED.certification_document,
    certificates = EXCLUDED.certificates,
    completed_orders = EXCLUDED.completed_orders,
    cancelled_orders = EXCLUDED.cancelled_orders,
    total_orders = EXCLUDED.total_orders,
    on_time_orders = EXCLUDED.on_time_orders,
    late_orders = EXCLUDED.late_orders,
    total_ratings = EXCLUDED.total_ratings,
    sum_ratings = EXCLUDED.sum_ratings,
    invite_code = EXCLUDED.invite_code,
    moq = EXCLUDED.moq,
    lead_time = EXCLUDED.lead_time,
    years_in_operation = EXCLUDED.years_in_operation,
    status_badge = EXCLUDED.status_badge,
    employee_count = EXCLUDED.employee_count,
    factory_size = EXCLUDED.factory_size,
    metadata = EXCLUDED.metadata,
    rating = EXCLUDED.rating,
    review_count = EXCLUDED.review_count,
    service_cost = EXCLUDED.service_cost,
    owner_id = EXCLUDED.owner_id;

WITH memberships (id, team_id, username) AS (
    VALUES
        ('b1000000-0000-4000-8000-000000000001'::uuid, 'a1000000-0000-4000-8000-000000000001'::uuid, 'nguyen.hoang.phuc'),
        ('b1000000-0000-4000-8000-000000000002'::uuid, 'a1000000-0000-4000-8000-000000000002'::uuid, 'tran.mai.anh'),
        ('b1000000-0000-4000-8000-000000000003'::uuid, 'a1000000-0000-4000-8000-000000000003'::uuid, 'le.duc.khanh'),
        ('b1000000-0000-4000-8000-000000000004'::uuid, 'a1000000-0000-4000-8000-000000000004'::uuid, 'pham.ngoc.han'),
        ('b1000000-0000-4000-8000-000000000005'::uuid, 'a1000000-0000-4000-8000-000000000005'::uuid, 'vo.thanh.dat'),
        ('b1000000-0000-4000-8000-000000000006'::uuid, 'a1000000-0000-4000-8000-000000000006'::uuid, 'bui.thu.ha'),
        ('b1000000-0000-4000-8000-000000000007'::uuid, 'a1000000-0000-4000-8000-000000000007'::uuid, 'dang.quoc.huy')
)
INSERT INTO team_members (id, group_role, joined_at, team_id, user_id)
SELECT m.id, 'ADMIN', t.created_at, m.team_id, u.id
FROM memberships m
JOIN users u ON u.username = m.username
JOIN teams t ON t.id = m.team_id
ON CONFLICT (team_id, user_id) DO UPDATE SET group_role = 'ADMIN';

WITH product_data (
    id, team_id, product_type, product_state, quantity, unit,
    low_stock_threshold, price, description, image_url, origin,
    roast_level, processing, taste_notes
) AS (
    VALUES
    ('c1000000-0000-4000-8000-000000000001'::uuid, 'a1000000-0000-4000-8000-000000000001'::uuid, 'Arabica Cầu Đất', 'GREEN', 420.0, 'kg', 80.0, '178.000 đ/kg', 'Arabica nhân xanh tuyển lựa, độ ẩm 11–12%.', 'https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=900&q=85', 'Cầu Đất, Lâm Đồng', NULL, 'Washed', 'Cam vàng, mật ong, trà đen'),
    ('c1000000-0000-4000-8000-000000000002'::uuid, 'a1000000-0000-4000-8000-000000000001'::uuid, 'Robusta Honey Bảo Lộc', 'GREEN', 680.0, 'kg', 120.0, '112.000 đ/kg', 'Robusta Honey sàng 18, phù hợp espresso blend.', 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=900&q=85', 'Bảo Lộc, Lâm Đồng', NULL, 'Honey', 'Cacao, hạt dẻ, mật mía'),
    ('c1000000-0000-4000-8000-000000000003'::uuid, 'a1000000-0000-4000-8000-000000000002'::uuid, 'Arabica Đà Lạt Light Roast', 'ROASTED', 145.0, 'kg', 35.0, '285.000 đ/kg', 'Mẻ rang sáng dành cho pour-over và batch brew.', 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefda?w=900&q=85', 'Đà Lạt, Lâm Đồng', 'Light', 'Washed', 'Hoa trắng, cam, caramel'),
    ('c1000000-0000-4000-8000-000000000004'::uuid, 'a1000000-0000-4000-8000-000000000002'::uuid, 'Espresso Đà Lạt Blend', 'PACKAGED', 96.0, 'kg', 24.0, '245.000 đ/kg', 'Blend cân bằng cho máy espresso, đóng túi van 1 kg.', 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=900&q=85', 'Lâm Đồng', 'Medium', 'Blend', 'Chocolate, hạnh nhân, caramel'),
    ('c1000000-0000-4000-8000-000000000005'::uuid, 'a1000000-0000-4000-8000-000000000003'::uuid, 'House Blend Cao Nguyên', 'ROASTED', 310.0, 'kg', 60.0, '198.000 đ/kg', 'Blend Arabica–Robusta ổn định cho quán cà phê.', 'https://images.unsplash.com/photo-1498804103079-a6351b050096?w=900&q=85', 'Đắk Lắk & Lâm Đồng', 'Medium Dark', 'Blend', 'Cacao, caramel, hậu vị đậm'),
    ('c1000000-0000-4000-8000-000000000006'::uuid, 'a1000000-0000-4000-8000-000000000003'::uuid, 'Robusta Fine Buôn Ma Thuột', 'GROUND', 260.0, 'kg', 50.0, '165.000 đ/kg', 'Cà phê xay theo cỡ pha phin hoặc espresso.', 'https://images.unsplash.com/photo-1587293852726-70cdb56c2866?w=900&q=85', 'Buôn Ma Thuột, Đắk Lắk', 'Medium Dark', 'Natural', 'Chocolate đen, hạt rang, mật mía'),
    ('c1000000-0000-4000-8000-000000000007'::uuid, 'a1000000-0000-4000-8000-000000000004'::uuid, 'Mây Signature Blend', 'PACKAGED', 78.0, 'kg', 20.0, '235.000 đ/kg', 'Sản phẩm nhãn riêng đóng túi 250 g hoặc 500 g.', 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=900&q=85', 'Việt Nam', 'Medium', 'Blend', 'Caramel, cacao, trái cây khô'),
    ('c1000000-0000-4000-8000-000000000008'::uuid, 'a1000000-0000-4000-8000-000000000004'::uuid, 'Drip Coffee Arabica', 'PACKAGED', 42.0, 'kg', 12.0, '145.000 đ/hộp', 'Hộp 10 gói drip coffee dành cho quà tặng doanh nghiệp.', 'https://images.unsplash.com/photo-1512568400610-62da28bc8a13?w=900&q=85', 'Lâm Đồng', 'Medium Light', 'Washed', 'Cam, mật ong, chocolate sữa'),
    ('c1000000-0000-4000-8000-000000000009'::uuid, 'a1000000-0000-4000-8000-000000000005'::uuid, 'Phương Nam Office Blend', 'PACKAGED', 190.0, 'kg', 40.0, '185.000 đ/kg', 'Blend đậm vừa dành cho máy pha văn phòng.', 'https://images.unsplash.com/photo-1504630083234-14187a9df0f5?w=900&q=85', 'Việt Nam', 'Medium Dark', 'Blend', 'Cacao, hạt dẻ, caramel'),
    ('c1000000-0000-4000-8000-000000000010'::uuid, 'a1000000-0000-4000-8000-000000000005'::uuid, 'Culi Robusta Rang Đậm', 'ROASTED', 230.0, 'kg', 45.0, '172.000 đ/kg', 'Culi Robusta rang đậm cho pha phin truyền thống.', 'https://images.unsplash.com/photo-1497515114889-1c06568a37b8?w=900&q=85', 'Đắk Lắk', 'Dark', 'Natural', 'Chocolate đen, khói nhẹ, hậu vị dài'),
    ('c1000000-0000-4000-8000-000000000011'::uuid, 'a1000000-0000-4000-8000-000000000006'::uuid, 'Arabica Túi Van 250 g', 'PACKAGED', 120.0, 'kg', 25.0, 'Theo hợp đồng', 'Dịch vụ hoàn thiện túi van, tem nhãn và in ngày sản xuất.', 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=900&q=85', 'Theo nguyên liệu khách hàng', NULL, 'Đóng gói', 'Theo sản phẩm'),
    ('c1000000-0000-4000-8000-000000000012'::uuid, 'a1000000-0000-4000-8000-000000000006'::uuid, 'Drip Coffee Hộp 10 Gói', 'PACKAGED', 85.0, 'kg', 18.0, 'Theo hợp đồng', 'Đóng gói drip bag và hoàn thiện hộp bán lẻ.', 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=900&q=85', 'Theo nguyên liệu khách hàng', NULL, 'Đóng gói', 'Theo sản phẩm'),
    ('c1000000-0000-4000-8000-000000000013'::uuid, 'a1000000-0000-4000-8000-000000000007'::uuid, 'Robusta Fine Sàng 18', 'GREEN', 760.0, 'kg', 150.0, '108.000 đ/kg', 'Robusta nhân xanh sàng 18, tỷ lệ lỗi thấp.', 'https://images.unsplash.com/photo-1524350876685-274059332603?w=900&q=85', 'Buôn Ma Thuột, Đắk Lắk', NULL, 'Natural', 'Cacao, hạt dẻ, mật mía'),
    ('c1000000-0000-4000-8000-000000000014'::uuid, 'a1000000-0000-4000-8000-000000000007'::uuid, 'Culi Robusta Tuyển', 'GREEN', 390.0, 'kg', 80.0, '126.000 đ/kg', 'Culi tuyển đồng đều, phù hợp phối trộn cà phê phin.', 'https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=900&q=85', 'Buôn Ma Thuột, Đắk Lắk', NULL, 'Natural', 'Chocolate đen, gia vị, hậu vị mạnh')
)
INSERT INTO inventory_items (
    id, team_id, product_type, product_state, quantity, unit,
    low_stock_threshold, price, description, image_url, origin, roast_level,
    processing, taste_notes, is_featured, last_updated, version
)
SELECT
    id, team_id, product_type, product_state, quantity, unit,
    low_stock_threshold, price, description, image_url, origin, roast_level,
    processing, taste_notes, true, now(), 0
FROM product_data
ON CONFLICT (team_id, product_type, product_state) DO UPDATE SET
    quantity = EXCLUDED.quantity,
    unit = EXCLUDED.unit,
    low_stock_threshold = EXCLUDED.low_stock_threshold,
    price = EXCLUDED.price,
    description = EXCLUDED.description,
    image_url = EXCLUDED.image_url,
    origin = EXCLUDED.origin,
    roast_level = EXCLUDED.roast_level,
    processing = EXCLUDED.processing,
    taste_notes = EXCLUDED.taste_notes,
    is_featured = true,
    last_updated = now();

COMMIT;

SELECT
    t.name,
    u.username AS owner,
    t.region,
    t.specialty,
    t.capacity_value || ' ' || t.capacity_unit AS capacity,
    t.is_published,
    count(i.id) FILTER (WHERE i.is_featured) AS featured_products
FROM teams t
JOIN users u ON u.id = t.owner_id
LEFT JOIN inventory_items i ON i.team_id = t.id
WHERE t.id::text LIKE 'a1000000-0000-4000-8000-%'
GROUP BY t.id, u.username
ORDER BY t.created_at;
