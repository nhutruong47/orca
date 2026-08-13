package org.example.backend.entity;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.util.UUID;

@Entity
@Table(name = "payroll_items", uniqueConstraints =
        @UniqueConstraint(name = "uk_payroll_item_run_user", columnNames = {"payroll_run_id", "user_id"}))
public class PayrollItem {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "payroll_run_id", nullable = false)
    private PayrollRun payrollRun;
    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;
    @Column(name = "member_name_snapshot", nullable = false)
    private String memberNameSnapshot;
    @Column(name = "regular_hours", nullable = false, precision = 10, scale = 2)
    private BigDecimal regularHours = BigDecimal.ZERO;
    @Column(name = "overtime_hours", nullable = false, precision = 10, scale = 2)
    private BigDecimal overtimeHours = BigDecimal.ZERO;
    @Column(name = "attendance_days", nullable = false)
    private Integer attendanceDays = 0;
    @Column(name = "late_days", nullable = false)
    private Integer lateDays = 0;
    @Column(name = "missing_checkout_days", nullable = false)
    private Integer missingCheckoutDays = 0;
    @Column(name = "total_tasks", nullable = false)
    private Integer totalTasks = 0;
    @Column(name = "completed_tasks", nullable = false)
    private Integer completedTasks = 0;
    @Column(name = "hourly_rate_vnd", nullable = false)
    private Long hourlyRateVnd = 0L;
    @Column(name = "overtime_multiplier", nullable = false, precision = 4, scale = 2)
    private BigDecimal overtimeMultiplier = new BigDecimal("1.50");
    @Column(name = "regular_pay_vnd", nullable = false)
    private Long regularPayVnd = 0L;
    @Column(name = "overtime_pay_vnd", nullable = false)
    private Long overtimePayVnd = 0L;
    @Column(name = "allowance_vnd", nullable = false)
    private Long allowanceVnd = 0L;
    @Column(name = "deduction_vnd", nullable = false)
    private Long deductionVnd = 0L;
    @Column(name = "advance_vnd", nullable = false)
    private Long advanceVnd = 0L;
    @Column(name = "net_pay_vnd", nullable = false)
    private Long netPayVnd = 0L;
    @Column(columnDefinition = "TEXT")
    private String note;

    public UUID getId() { return id; }
    public PayrollRun getPayrollRun() { return payrollRun; }
    public void setPayrollRun(PayrollRun payrollRun) { this.payrollRun = payrollRun; }
    public User getUser() { return user; }
    public void setUser(User user) { this.user = user; }
    public String getMemberNameSnapshot() { return memberNameSnapshot; }
    public void setMemberNameSnapshot(String memberNameSnapshot) { this.memberNameSnapshot = memberNameSnapshot; }
    public BigDecimal getRegularHours() { return regularHours; }
    public void setRegularHours(BigDecimal regularHours) { this.regularHours = regularHours; }
    public BigDecimal getOvertimeHours() { return overtimeHours; }
    public void setOvertimeHours(BigDecimal overtimeHours) { this.overtimeHours = overtimeHours; }
    public Integer getAttendanceDays() { return attendanceDays; }
    public void setAttendanceDays(Integer attendanceDays) { this.attendanceDays = attendanceDays; }
    public Integer getLateDays() { return lateDays; }
    public void setLateDays(Integer lateDays) { this.lateDays = lateDays; }
    public Integer getMissingCheckoutDays() { return missingCheckoutDays; }
    public void setMissingCheckoutDays(Integer missingCheckoutDays) { this.missingCheckoutDays = missingCheckoutDays; }
    public Integer getTotalTasks() { return totalTasks; }
    public void setTotalTasks(Integer totalTasks) { this.totalTasks = totalTasks; }
    public Integer getCompletedTasks() { return completedTasks; }
    public void setCompletedTasks(Integer completedTasks) { this.completedTasks = completedTasks; }
    public Long getHourlyRateVnd() { return hourlyRateVnd; }
    public void setHourlyRateVnd(Long hourlyRateVnd) { this.hourlyRateVnd = hourlyRateVnd; }
    public BigDecimal getOvertimeMultiplier() { return overtimeMultiplier; }
    public void setOvertimeMultiplier(BigDecimal overtimeMultiplier) { this.overtimeMultiplier = overtimeMultiplier; }
    public Long getRegularPayVnd() { return regularPayVnd; }
    public void setRegularPayVnd(Long regularPayVnd) { this.regularPayVnd = regularPayVnd; }
    public Long getOvertimePayVnd() { return overtimePayVnd; }
    public void setOvertimePayVnd(Long overtimePayVnd) { this.overtimePayVnd = overtimePayVnd; }
    public Long getAllowanceVnd() { return allowanceVnd; }
    public void setAllowanceVnd(Long allowanceVnd) { this.allowanceVnd = allowanceVnd; }
    public Long getDeductionVnd() { return deductionVnd; }
    public void setDeductionVnd(Long deductionVnd) { this.deductionVnd = deductionVnd; }
    public Long getAdvanceVnd() { return advanceVnd; }
    public void setAdvanceVnd(Long advanceVnd) { this.advanceVnd = advanceVnd; }
    public Long getNetPayVnd() { return netPayVnd; }
    public void setNetPayVnd(Long netPayVnd) { this.netPayVnd = netPayVnd; }
    public String getNote() { return note; }
    public void setNote(String note) { this.note = note; }
}
