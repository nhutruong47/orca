package org.example.backend.dto;

import java.time.LocalDateTime;

public class UpdateAttendanceRequest {
    private LocalDateTime checkInTime;
    private LocalDateTime checkOutTime;
    private String reason;

    public LocalDateTime getCheckInTime() {
        return checkInTime;
    }

    public void setCheckInTime(LocalDateTime checkInTime) {
        this.checkInTime = checkInTime;
    }

    public LocalDateTime getCheckOutTime() {
        return checkOutTime;
    }

    public void setCheckOutTime(LocalDateTime checkOutTime) {
        this.checkOutTime = checkOutTime;
    }

    public String getReason() { return reason; }
    public void setReason(String reason) { this.reason = reason; }
}
