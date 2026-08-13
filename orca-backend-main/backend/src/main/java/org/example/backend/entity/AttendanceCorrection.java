package org.example.backend.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.UUID;

@Entity
@Table(name = "attendance_corrections")
public class AttendanceCorrection {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "attendance_id", nullable = false)
    private Attendance attendance;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "actor_id", nullable = false)
    private User actor;

    @Column(name = "old_check_in_time")
    private LocalDateTime oldCheckInTime;
    @Column(name = "old_check_out_time")
    private LocalDateTime oldCheckOutTime;
    @Column(name = "new_check_in_time", nullable = false)
    private LocalDateTime newCheckInTime;
    @Column(name = "new_check_out_time", nullable = false)
    private LocalDateTime newCheckOutTime;
    @Column(nullable = false, length = 500)
    private String reason;
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @PrePersist
    void onCreate() { createdAt = LocalDateTime.now(ZoneId.of("Asia/Ho_Chi_Minh")); }

    public UUID getId() { return id; }
    public Attendance getAttendance() { return attendance; }
    public void setAttendance(Attendance attendance) { this.attendance = attendance; }
    public User getActor() { return actor; }
    public void setActor(User actor) { this.actor = actor; }
    public LocalDateTime getOldCheckInTime() { return oldCheckInTime; }
    public void setOldCheckInTime(LocalDateTime oldCheckInTime) { this.oldCheckInTime = oldCheckInTime; }
    public LocalDateTime getOldCheckOutTime() { return oldCheckOutTime; }
    public void setOldCheckOutTime(LocalDateTime oldCheckOutTime) { this.oldCheckOutTime = oldCheckOutTime; }
    public LocalDateTime getNewCheckInTime() { return newCheckInTime; }
    public void setNewCheckInTime(LocalDateTime newCheckInTime) { this.newCheckInTime = newCheckInTime; }
    public LocalDateTime getNewCheckOutTime() { return newCheckOutTime; }
    public void setNewCheckOutTime(LocalDateTime newCheckOutTime) { this.newCheckOutTime = newCheckOutTime; }
    public String getReason() { return reason; }
    public void setReason(String reason) { this.reason = reason; }
    public LocalDateTime getCreatedAt() { return createdAt; }
}
