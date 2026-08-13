package org.example.backend.dto;

import java.time.LocalDateTime;
import java.util.UUID;

public class AttendanceCorrectionDTO {
    private UUID id;
    private String actorName;
    private LocalDateTime oldCheckInTime;
    private LocalDateTime oldCheckOutTime;
    private LocalDateTime newCheckInTime;
    private LocalDateTime newCheckOutTime;
    private String reason;
    private LocalDateTime createdAt;

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }
    public String getActorName() { return actorName; }
    public void setActorName(String actorName) { this.actorName = actorName; }
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
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
