package org.example.backend.entity;

import jakarta.persistence.*;

import java.math.BigDecimal;
import java.time.LocalTime;
import java.util.UUID;

@Entity
@Table(name = "attendance_settings", uniqueConstraints =
        @UniqueConstraint(name = "uk_attendance_settings_team", columnNames = "team_id"))
public class AttendanceSettings {
    public static final LocalTime DEFAULT_START_TIME = LocalTime.of(9, 0);
    public static final LocalTime DEFAULT_END_TIME = LocalTime.of(17, 30);
    public static final BigDecimal DEFAULT_STANDARD_HOURS = new BigDecimal("7.50");
    public static final long DEFAULT_HOURLY_RATE_VND = 50_000L;
    public static final BigDecimal DEFAULT_OVERTIME_MULTIPLIER = new BigDecimal("1.50");

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @OneToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "team_id", nullable = false)
    private Team team;

    @Column(name = "work_start_time", nullable = false)
    private LocalTime workStartTime = DEFAULT_START_TIME;

    @Column(name = "work_end_time", nullable = false)
    private LocalTime workEndTime = DEFAULT_END_TIME;

    @Column(name = "standard_hours", nullable = false, precision = 4, scale = 2)
    private BigDecimal standardHours = DEFAULT_STANDARD_HOURS;

    @Column(name = "hourly_rate_vnd", nullable = false)
    private Long hourlyRateVnd = DEFAULT_HOURLY_RATE_VND;

    @Column(name = "overtime_multiplier", nullable = false, precision = 4, scale = 2)
    private BigDecimal overtimeMultiplier = DEFAULT_OVERTIME_MULTIPLIER;

    public UUID getId() { return id; }
    public Team getTeam() { return team; }
    public void setTeam(Team team) { this.team = team; }
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
