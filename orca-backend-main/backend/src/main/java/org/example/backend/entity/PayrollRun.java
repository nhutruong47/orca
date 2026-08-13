package org.example.backend.entity;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "payroll_runs", uniqueConstraints =
        @UniqueConstraint(name = "uk_payroll_run_team_period", columnNames = {"team_id", "period_year", "period_month"}))
public class PayrollRun {
    public enum Status { DRAFT, CALCULATED, APPROVED, PAID }

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @Version
    private Long version;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "team_id", nullable = false)
    private Team team;

    @Column(name = "period_year", nullable = false)
    private Integer year;

    @Column(name = "period_month", nullable = false)
    private Integer month;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false, length = 20)
    private Status status = Status.DRAFT;

    @Column(name = "regular_hours", nullable = false, precision = 10, scale = 2)
    private BigDecimal regularHours = BigDecimal.ZERO;
    @Column(name = "overtime_hours", nullable = false, precision = 10, scale = 2)
    private BigDecimal overtimeHours = BigDecimal.ZERO;
    @Column(name = "gross_pay_vnd", nullable = false)
    private Long grossPayVnd = 0L;
    @Column(name = "allowance_vnd", nullable = false)
    private Long allowanceVnd = 0L;
    @Column(name = "deduction_vnd", nullable = false)
    private Long deductionVnd = 0L;
    @Column(name = "advance_vnd", nullable = false)
    private Long advanceVnd = 0L;
    @Column(name = "net_pay_vnd", nullable = false)
    private Long netPayVnd = 0L;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "finalized_by")
    private User finalizedBy;
    @Column(name = "finalized_at")
    private LocalDateTime finalizedAt;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "paid_by")
    private User paidBy;
    @Column(name = "paid_at")
    private LocalDateTime paidAt;
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;
    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;

    @PrePersist void onCreate() { createdAt = LocalDateTime.now(); updatedAt = createdAt; }
    @PreUpdate void onUpdate() { updatedAt = LocalDateTime.now(); }

    public UUID getId() { return id; }
    public Team getTeam() { return team; }
    public void setTeam(Team team) { this.team = team; }
    public Integer getYear() { return year; }
    public void setYear(Integer year) { this.year = year; }
    public Integer getMonth() { return month; }
    public void setMonth(Integer month) { this.month = month; }
    public Status getStatus() { return status; }
    public void setStatus(Status status) { this.status = status; }
    public BigDecimal getRegularHours() { return regularHours; }
    public void setRegularHours(BigDecimal regularHours) { this.regularHours = regularHours; }
    public BigDecimal getOvertimeHours() { return overtimeHours; }
    public void setOvertimeHours(BigDecimal overtimeHours) { this.overtimeHours = overtimeHours; }
    public Long getGrossPayVnd() { return grossPayVnd; }
    public void setGrossPayVnd(Long grossPayVnd) { this.grossPayVnd = grossPayVnd; }
    public Long getAllowanceVnd() { return allowanceVnd; }
    public void setAllowanceVnd(Long allowanceVnd) { this.allowanceVnd = allowanceVnd; }
    public Long getDeductionVnd() { return deductionVnd; }
    public void setDeductionVnd(Long deductionVnd) { this.deductionVnd = deductionVnd; }
    public Long getAdvanceVnd() { return advanceVnd; }
    public void setAdvanceVnd(Long advanceVnd) { this.advanceVnd = advanceVnd; }
    public Long getNetPayVnd() { return netPayVnd; }
    public void setNetPayVnd(Long netPayVnd) { this.netPayVnd = netPayVnd; }
    public User getFinalizedBy() { return finalizedBy; }
    public void setFinalizedBy(User finalizedBy) { this.finalizedBy = finalizedBy; }
    public LocalDateTime getFinalizedAt() { return finalizedAt; }
    public void setFinalizedAt(LocalDateTime finalizedAt) { this.finalizedAt = finalizedAt; }
    public User getPaidBy() { return paidBy; }
    public void setPaidBy(User paidBy) { this.paidBy = paidBy; }
    public LocalDateTime getPaidAt() { return paidAt; }
    public void setPaidAt(LocalDateTime paidAt) { this.paidAt = paidAt; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
}
