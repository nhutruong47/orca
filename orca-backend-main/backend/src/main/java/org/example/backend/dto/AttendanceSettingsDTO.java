package org.example.backend.dto;

import java.math.BigDecimal;
import java.time.LocalTime;

public class AttendanceSettingsDTO {
    private LocalTime workStartTime;
    private LocalTime workEndTime;
    private BigDecimal standardHours;
    private Long hourlyRateVnd;
    private BigDecimal overtimeMultiplier;

    public LocalTime getWorkStartTime() { return workStartTime; }
    public void setWorkStartTime(LocalTime workStartTime) { this.workStartTime = workStartTime; }
    public LocalTime getWorkEndTime() { return workEndTime; }
    public void setWorkEndTime(LocalTime workEndTime) { this.workEndTime = workEndTime; }
    public BigDecimal getStandardHours() { return standardHours; }
    public void setStandardHours(BigDecimal standardHours) { this.standardHours = standardHours; }
    public Long getHourlyRateVnd() { return hourlyRateVnd; }
    public void setHourlyRateVnd(Long hourlyRateVnd) { this.hourlyRateVnd = hourlyRateVnd; }
    public BigDecimal getOvertimeMultiplier() { return overtimeMultiplier; }
    public void setOvertimeMultiplier(BigDecimal overtimeMultiplier) { this.overtimeMultiplier = overtimeMultiplier; }
}
