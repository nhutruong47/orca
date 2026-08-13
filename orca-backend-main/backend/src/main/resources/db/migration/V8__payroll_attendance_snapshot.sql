CREATE TABLE IF NOT EXISTS payroll_attendance_lines (
    id UUID PRIMARY KEY,
    payroll_item_id UUID NOT NULL REFERENCES payroll_items(id) ON DELETE CASCADE,
    source_attendance_id UUID,
    attendance_date DATE NOT NULL,
    check_in_time TIMESTAMP,
    check_out_time TIMESTAMP,
    regular_hours NUMERIC(10,2) NOT NULL DEFAULT 0,
    overtime_hours NUMERIC(10,2) NOT NULL DEFAULT 0,
    attendance_status VARCHAR(30),
    shift_type VARCHAR(20),
    production_stage VARCHAR(50),
    payable BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE INDEX IF NOT EXISTS idx_payroll_attendance_item_date
    ON payroll_attendance_lines(payroll_item_id, attendance_date, check_in_time);
