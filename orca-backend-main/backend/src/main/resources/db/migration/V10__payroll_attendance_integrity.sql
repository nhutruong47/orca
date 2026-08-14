-- The current attendance policy allows one recorded shift per employee, workshop and day.
-- Service-level checks provide friendly errors; these indexes close concurrent-request gaps.
CREATE UNIQUE INDEX IF NOT EXISTS uk_attendance_user_team_day
    ON attendances(user_id, team_id, attendance_date);

CREATE UNIQUE INDEX IF NOT EXISTS uk_payroll_attendance_source
    ON payroll_attendance_lines(payroll_item_id, source_attendance_id)
    WHERE source_attendance_id IS NOT NULL;
