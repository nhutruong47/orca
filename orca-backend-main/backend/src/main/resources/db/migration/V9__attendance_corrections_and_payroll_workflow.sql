CREATE TABLE IF NOT EXISTS attendance_corrections (
    id UUID PRIMARY KEY,
    attendance_id UUID NOT NULL REFERENCES attendances(id) ON DELETE CASCADE,
    actor_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    old_check_in_time TIMESTAMP,
    old_check_out_time TIMESTAMP,
    new_check_in_time TIMESTAMP NOT NULL,
    new_check_out_time TIMESTAMP NOT NULL,
    reason VARCHAR(500) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_attendance_corrections_record
    ON attendance_corrections(attendance_id, created_at DESC);

CREATE UNIQUE INDEX IF NOT EXISTS uk_attendance_open_shift
    ON attendances(user_id, team_id) WHERE check_out_time IS NULL;

ALTER TABLE payroll_runs DROP CONSTRAINT IF EXISTS ck_payroll_run_status;
UPDATE payroll_runs SET status = 'APPROVED' WHERE status = 'FINALIZED';
ALTER TABLE payroll_runs ADD CONSTRAINT ck_payroll_run_status
    CHECK (status IN ('DRAFT', 'CALCULATED', 'APPROVED', 'PAID'));
