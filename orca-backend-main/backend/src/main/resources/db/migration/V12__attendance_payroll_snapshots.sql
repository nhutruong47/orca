ALTER TABLE attendance_settings
    ADD COLUMN IF NOT EXISTS hourly_rate_vnd BIGINT NOT NULL DEFAULT 50000,
    ADD COLUMN IF NOT EXISTS overtime_multiplier NUMERIC(4, 2) NOT NULL DEFAULT 1.50;

ALTER TABLE attendances
    ADD COLUMN IF NOT EXISTS hourly_rate_vnd_snapshot BIGINT,
    ADD COLUMN IF NOT EXISTS overtime_multiplier_snapshot NUMERIC(4, 2);

UPDATE attendances a
SET hourly_rate_vnd_snapshot = s.hourly_rate_vnd,
    overtime_multiplier_snapshot = s.overtime_multiplier
FROM attendance_settings s
WHERE s.team_id = a.team_id
  AND (a.hourly_rate_vnd_snapshot IS NULL OR a.overtime_multiplier_snapshot IS NULL);

UPDATE attendances
SET hourly_rate_vnd_snapshot = COALESCE(hourly_rate_vnd_snapshot, 50000),
    overtime_multiplier_snapshot = COALESCE(overtime_multiplier_snapshot, 1.50);

ALTER TABLE attendances
    ALTER COLUMN hourly_rate_vnd_snapshot SET DEFAULT 50000,
    ALTER COLUMN overtime_multiplier_snapshot SET DEFAULT 1.50;

ALTER TABLE payroll_attendance_lines
    ADD COLUMN IF NOT EXISTS hourly_rate_vnd BIGINT,
    ADD COLUMN IF NOT EXISTS overtime_multiplier NUMERIC(4, 2),
    ADD COLUMN IF NOT EXISTS regular_pay_vnd BIGINT,
    ADD COLUMN IF NOT EXISTS overtime_pay_vnd BIGINT;

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'ck_attendance_settings_hourly_rate') THEN
        ALTER TABLE attendance_settings
            ADD CONSTRAINT ck_attendance_settings_hourly_rate
                CHECK (hourly_rate_vnd BETWEEN 1000 AND 10000000);
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = 'ck_attendance_settings_ot_multiplier') THEN
        ALTER TABLE attendance_settings
            ADD CONSTRAINT ck_attendance_settings_ot_multiplier
                CHECK (overtime_multiplier BETWEEN 1.00 AND 3.00);
    END IF;
END $$;
