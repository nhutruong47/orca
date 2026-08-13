CREATE TABLE IF NOT EXISTS payroll_profiles (
    id UUID PRIMARY KEY,
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    hourly_rate_vnd BIGINT NOT NULL DEFAULT 50000,
    overtime_multiplier NUMERIC(4,2) NOT NULL DEFAULT 1.50,
    updated_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_payroll_profile_team_user UNIQUE (team_id, user_id),
    CONSTRAINT ck_payroll_profile_rate CHECK (hourly_rate_vnd >= 1000),
    CONSTRAINT ck_payroll_profile_ot CHECK (overtime_multiplier BETWEEN 1.00 AND 3.00)
);

CREATE TABLE IF NOT EXISTS payroll_runs (
    id UUID PRIMARY KEY,
    version BIGINT,
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    period_year INTEGER NOT NULL,
    period_month INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'DRAFT',
    regular_hours NUMERIC(10,2) NOT NULL DEFAULT 0,
    overtime_hours NUMERIC(10,2) NOT NULL DEFAULT 0,
    gross_pay_vnd BIGINT NOT NULL DEFAULT 0,
    allowance_vnd BIGINT NOT NULL DEFAULT 0,
    deduction_vnd BIGINT NOT NULL DEFAULT 0,
    advance_vnd BIGINT NOT NULL DEFAULT 0,
    net_pay_vnd BIGINT NOT NULL DEFAULT 0,
    finalized_by UUID REFERENCES users(id) ON DELETE SET NULL,
    finalized_at TIMESTAMP,
    paid_by UUID REFERENCES users(id) ON DELETE SET NULL,
    paid_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uk_payroll_run_team_period UNIQUE (team_id, period_year, period_month),
    CONSTRAINT ck_payroll_run_month CHECK (period_month BETWEEN 1 AND 12),
    CONSTRAINT ck_payroll_run_status CHECK (status IN ('DRAFT', 'CALCULATED', 'APPROVED', 'PAID'))
);

CREATE TABLE IF NOT EXISTS payroll_items (
    id UUID PRIMARY KEY,
    payroll_run_id UUID NOT NULL REFERENCES payroll_runs(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    member_name_snapshot VARCHAR(255) NOT NULL,
    regular_hours NUMERIC(10,2) NOT NULL DEFAULT 0,
    overtime_hours NUMERIC(10,2) NOT NULL DEFAULT 0,
    attendance_days INTEGER NOT NULL DEFAULT 0,
    late_days INTEGER NOT NULL DEFAULT 0,
    missing_checkout_days INTEGER NOT NULL DEFAULT 0,
    total_tasks INTEGER NOT NULL DEFAULT 0,
    completed_tasks INTEGER NOT NULL DEFAULT 0,
    hourly_rate_vnd BIGINT NOT NULL DEFAULT 0,
    overtime_multiplier NUMERIC(4,2) NOT NULL DEFAULT 1.50,
    regular_pay_vnd BIGINT NOT NULL DEFAULT 0,
    overtime_pay_vnd BIGINT NOT NULL DEFAULT 0,
    allowance_vnd BIGINT NOT NULL DEFAULT 0,
    deduction_vnd BIGINT NOT NULL DEFAULT 0,
    advance_vnd BIGINT NOT NULL DEFAULT 0,
    net_pay_vnd BIGINT NOT NULL DEFAULT 0,
    note TEXT,
    CONSTRAINT uk_payroll_item_run_user UNIQUE (payroll_run_id, user_id)
);

CREATE TABLE IF NOT EXISTS payroll_audit_logs (
    id UUID PRIMARY KEY,
    payroll_run_id UUID NOT NULL REFERENCES payroll_runs(id) ON DELETE CASCADE,
    actor_id UUID NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    action VARCHAR(50) NOT NULL,
    details TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_payroll_runs_team_period ON payroll_runs(team_id, period_year, period_month);
CREATE INDEX IF NOT EXISTS idx_payroll_items_run ON payroll_items(payroll_run_id);
CREATE INDEX IF NOT EXISTS idx_payroll_audit_run ON payroll_audit_logs(payroll_run_id, created_at DESC);
