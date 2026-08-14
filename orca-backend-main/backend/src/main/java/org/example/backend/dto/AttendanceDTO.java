package org.example.backend.dto;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;

public class AttendanceDTO {
    private String id;
    private String userId;
    private String userName;
    private String teamId;
    private LocalDate date;
    private String shiftType;
    private String shiftStartTime;
    private String shiftEndTime;
    private LocalDateTime checkInTime;
    private LocalDateTime checkOutTime;
    private String productionStage;
    private String orderId;
    private String orderTitle;
    private Integer breakMinutes;
    private Double standardHours;
    private Double actualWorkHours;
    private Double workedHours;
    private Double regularHours;
    private Double overtimeHours;
    private Long hourlyRateVnd;
    private BigDecimal overtimeMultiplier;
    private Long regularPayVnd;
    private Long overtimePayVnd;
    private Long totalPayVnd;
    private String attendanceStatus;
    private String notes;

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getUserId() { return userId; }
    public void setUserId(String userId) { this.userId = userId; }
    public String getUserName() { return userName; }
    public void setUserName(String userName) { this.userName = userName; }
    public String getTeamId() { return teamId; }
    public void setTeamId(String teamId) { this.teamId = teamId; }
    public LocalDate getDate() { return date; }
    public void setDate(LocalDate date) { this.date = date; }
    public String getShiftType() { return shiftType; }
    public void setShiftType(String shiftType) { this.shiftType = shiftType; }
    public String getShiftStartTime() { return shiftStartTime; }
    public void setShiftStartTime(String shiftStartTime) { this.shiftStartTime = shiftStartTime; }
    public String getShiftEndTime() { return shiftEndTime; }
    public void setShiftEndTime(String shiftEndTime) { this.shiftEndTime = shiftEndTime; }
    public LocalDateTime getCheckInTime() { return checkInTime; }
    public void setCheckInTime(LocalDateTime checkInTime) { this.checkInTime = checkInTime; }
    public LocalDateTime getCheckOutTime() { return checkOutTime; }
    public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }
    public String getProductionStage() { return productionStage; }
    public void setProductionStage(String productionStage) { this.productionStage = productionStage; }
    public String getOrderId() { return orderId; }
    public void setOrderId(String orderId) { this.orderId = orderId; }
    public String getOrderTitle() { return orderTitle; }
    public void setOrderTitle(String orderTitle) { this.orderTitle = orderTitle; }
    public Integer getBreakMinutes() { return breakMinutes; }
    public void setBreakMinutes(Integer breakMinutes) { this.breakMinutes = breakMinutes; }
    public Double getStandardHours() { return standardHours; }
    public void setStandardHours(Double standardHours) { this.standardHours = standardHours; }
    public Double getActualWorkHours() { return actualWorkHours; }
    public void setActualWorkHours(Double actualWorkHours) { this.actualWorkHours = actualWorkHours; }
    public Double getWorkedHours() { return workedHours; }
    public void setWorkedHours(Double workedHours) { this.workedHours = workedHours; }
    public Double getRegularHours() { return regularHours; }
    public void setRegularHours(Double regularHours) { this.regularHours = regularHours; }
    public Double getOvertimeHours() { return overtimeHours; }
    public void setOvertimeHours(Double overtimeHours) { this.overtimeHours = overtimeHours; }
    public Long getHourlyRateVnd() { return hourlyRateVnd; }
    public void setHourlyRateVnd(Long hourlyRateVnd) { this.hourlyRateVnd = hourlyRateVnd; }
    public BigDecimal getOvertimeMultiplier() { return overtimeMultiplier; }
    public void setOvertimeMultiplier(BigDecimal overtimeMultiplier) { this.overtimeMultiplier = overtimeMultiplier; }
    public Long getRegularPayVnd() { return regularPayVnd; }
    public void setRegularPayVnd(Long regularPayVnd) { this.regularPayVnd = regularPayVnd; }
    public Long getOvertimePayVnd() { return overtimePayVnd; }
    public void setOvertimePayVnd(Long overtimePayVnd) { this.overtimePayVnd = overtimePayVnd; }
    public Long getTotalPayVnd() { return totalPayVnd; }
    public void setTotalPayVnd(Long totalPayVnd) { this.totalPayVnd = totalPayVnd; }
    public String getAttendanceStatus() { return attendanceStatus; }
    public void setAttendanceStatus(String attendanceStatus) { this.attendanceStatus = attendanceStatus; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
}
