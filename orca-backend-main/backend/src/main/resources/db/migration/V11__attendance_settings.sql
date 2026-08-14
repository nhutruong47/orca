CREATE TABLE IF NOT EXISTS attendance_settings (
    id UUID PRIMARY KEY,
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    work_start_time TIME NOT NULL DEFAULT '09:00:00',
    work_end_time TIME NOT NULL DEFAULT '17:30:00',
    standard_hours NUMERIC(4, 2) NOT NULL DEFAULT 7.50,
    CONSTRAINT uk_attendance_settings_team UNIQUE (team_id),
    CONSTRAINT ck_attendance_settings_hours CHECK (standard_hours > 0 AND standard_hours <= 24),
    CONSTRAINT ck_attendance_settings_window CHECK (work_end_time > work_start_time)
);

INSERT INTO attendance_settings (id, team_id, work_start_time, work_end_time, standard_hours)
SELECT gen_random_uuid(), t.id, '09:00:00', '17:30:00', 7.50
FROM teams t
WHERE NOT EXISTS (
    SELECT 1 FROM attendance_settings s WHERE s.team_id = t.id
);

ALTER TABLE attendances
    ADD COLUMN IF NOT EXISTS standard_hours_snapshot NUMERIC(4, 2);

-- Existing rows keep their already calculated values. New rows always receive a snapshot at check-in.
