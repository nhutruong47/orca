package org.example.backend.entity;

import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "payroll_attendance_lines",
        indexes = @Index(name = "idx_payroll_attendance_item_date", columnList = "payroll_item_id, attendance_date"),
        uniqueConstraints = @UniqueConstraint(name = "uk_payroll_attendance_source", columnNames = {"payroll_item_id", "source_attendance_id"}))
public class PayrollAttendanceLine {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "payroll_item_id", nullable = false)
    private PayrollItem payrollItem;

    @Column(name = "source_attendance_id")
    private UUID sourceAttendanceId;
    @Column(name = "attendance_date", nullable = false)
    private LocalDate attendanceDate;
    @Column(name = "check_in_time")
    private LocalDateTime checkInTime;
    @Column(name = "check_out_time")
    private LocalDateTime checkOutTime;
    @Column(name = "regular_hours", nullable = false, precision = 10, scale = 2)
    private BigDecimal regularHours = BigDecimal.ZERO;
    @Column(name = "overtime_hours", nullable = false, precision = 10, scale = 2)
    private BigDecimal overtimeHours = BigDecimal.ZERO;
    @Column(name = "hourly_rate_vnd")
    private Long hourlyRateVnd;
    @Column(name = "overtime_multiplier", precision = 4, scale = 2)
    private BigDecimal overtimeMultiplier;
    @Column(name = "regular_pay_vnd")
    private Long regularPayVnd;
    @Column(name = "overtime_pay_vnd")
    private Long overtimePayVnd;
    @Column(name = "attendance_status", length = 30)
    private String attendanceStatus;
    @Column(name = "shift_type", length = 20)
    private String shiftType;
    @Column(name = "production_stage", length = 50)
    private String productionStage;
    @Column(name = "payable", nullable = false)
    private boolean payable;

    public UUID getId() { return id; }
    public PayrollItem getPayrollItem() { return payrollItem; }
    public void setPayrollItem(PayrollItem payrollItem) { this.payrollItem = payrollItem; }
    public UUID getSourceAttendanceId() { return sourceAttendanceId; }
    public void setSourceAttendanceId(UUID sourceAttendanceId) { this.sourceAttendanceId = sourceAttendanceId; }
    public LocalDate getAttendanceDate() { return attendanceDate; }
    public void setAttendanceDate(LocalDate attendanceDate) { this.attendanceDate = attendanceDate; }
    public LocalDateTime getCheckInTime() { return checkInTime; }
    public void setCheckInTime(LocalDateTime checkInTime) { this.checkInTime = checkInTime; }
    public LocalDateTime getCheckOutTime() { return checkOutTime; }
    public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }
    public BigDecimal getRegularHours() { return regularHours; }
    public void setRegularHours(BigDecimal regularHours) { this.regularHours = regularHours; }
    public BigDecimal getOvertimeHours() { return overtimeHours; }
    public void setOvertimeHours(BigDecimal overtimeHours) { this.overtimeHours = overtimeHours; }
    public Long getHourlyRateVnd() { return hourlyRateVnd; }
    public void setHourlyRateVnd(Long hourlyRateVnd) { this.hourlyRateVnd = hourlyRateVnd; }
    public BigDecimal getOvertimeMultiplier() { return overtimeMultiplier; }
    public void setOvertimeMultiplier(BigDecimal overtimeMultiplier) { this.overtimeMultiplier = overtimeMultiplier; }
    public Long getRegularPayVnd() { return regularPayVnd; }
    public void setRegularPayVnd(Long regularPayVnd) { this.regularPayVnd = regularPayVnd; }
    public Long getOvertimePayVnd() { return overtimePayVnd; }
    public void setOvertimePayVnd(Long overtimePayVnd) { this.overtimePayVnd = overtimePayVnd; }
    public String getAttendanceStatus() { return attendanceStatus; }
    public void setAttendanceStatus(String attendanceStatus) { this.attendanceStatus = attendanceStatus; }
    public String getShiftType() { return shiftType; }
    public void setShiftType(String shiftType) { this.shiftType = shiftType; }
    public String getProductionStage() { return productionStage; }
    public void setProductionStage(String productionStage) { this.productionStage = productionStage; }
    public boolean isPayable() { return payable; }
    public void setPayable(boolean payable) { this.payable = payable; }
}
