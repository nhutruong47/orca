package org.example.backend.dto;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class PayrollReportDTO {
    private UUID runId;
    private UUID teamId;
    private int year;
    private int month;
    private String status;
    private LocalDateTime updatedAt;
    private LocalDateTime finalizedAt;
    private LocalDateTime paidAt;
    private Summary summary = new Summary();
    private List<Item> items = new ArrayList<>();

    public static class Summary {
        private int memberCount;
        private int paidMemberCount;
        private int attendanceDays;
        private BigDecimal regularHours = BigDecimal.ZERO;
        private BigDecimal overtimeHours = BigDecimal.ZERO;
        private BigDecimal totalHours = BigDecimal.ZERO;
        private long grossPayVnd;
        private long allowanceVnd;
        private long deductionVnd;
        private long advanceVnd;
        private long netPayVnd;
        private int totalTasks;
        private int completedTasks;
        private int missingCheckoutCount;
        public int getMemberCount() { return memberCount; }
        public void setMemberCount(int memberCount) { this.memberCount = memberCount; }
        public int getPaidMemberCount() { return paidMemberCount; }
        public void setPaidMemberCount(int paidMemberCount) { this.paidMemberCount = paidMemberCount; }
        public int getAttendanceDays() { return attendanceDays; }
        public void setAttendanceDays(int attendanceDays) { this.attendanceDays = attendanceDays; }
        public BigDecimal getRegularHours() { return regularHours; }
        public void setRegularHours(BigDecimal regularHours) { this.regularHours = regularHours; }
        public BigDecimal getOvertimeHours() { return overtimeHours; }
        public void setOvertimeHours(BigDecimal overtimeHours) { this.overtimeHours = overtimeHours; }
        public BigDecimal getTotalHours() { return totalHours; }
        public void setTotalHours(BigDecimal totalHours) { this.totalHours = totalHours; }
        public long getGrossPayVnd() { return grossPayVnd; }
        public void setGrossPayVnd(long grossPayVnd) { this.grossPayVnd = grossPayVnd; }
        public long getAllowanceVnd() { return allowanceVnd; }
        public void setAllowanceVnd(long allowanceVnd) { this.allowanceVnd = allowanceVnd; }
        public long getDeductionVnd() { return deductionVnd; }
        public void setDeductionVnd(long deductionVnd) { this.deductionVnd = deductionVnd; }
        public long getAdvanceVnd() { return advanceVnd; }
        public void setAdvanceVnd(long advanceVnd) { this.advanceVnd = advanceVnd; }
        public long getNetPayVnd() { return netPayVnd; }
        public void setNetPayVnd(long netPayVnd) { this.netPayVnd = netPayVnd; }
        public int getTotalTasks() { return totalTasks; }
        public void setTotalTasks(int totalTasks) { this.totalTasks = totalTasks; }
        public int getCompletedTasks() { return completedTasks; }
        public void setCompletedTasks(int completedTasks) { this.completedTasks = completedTasks; }
        public int getMissingCheckoutCount() { return missingCheckoutCount; }
        public void setMissingCheckoutCount(int missingCheckoutCount) { this.missingCheckoutCount = missingCheckoutCount; }
    }

    public static class Item {
        private UUID itemId;
        private UUID memberId;
        private String memberName;
        private BigDecimal regularHours;
        private BigDecimal overtimeHours;
        private int attendanceDays;
        private int lateDays;
        private int missingCheckoutDays;
        private int totalTasks;
        private int completedTasks;
        private long hourlyRateVnd;
        private BigDecimal overtimeMultiplier;
        private long regularPayVnd;
        private long overtimePayVnd;
        private long allowanceVnd;
        private long deductionVnd;
        private long advanceVnd;
        private long netPayVnd;
        private String note;
        private List<AttendanceLine> attendanceLines = new ArrayList<>();
        public UUID getItemId() { return itemId; }
        public void setItemId(UUID itemId) { this.itemId = itemId; }
        public UUID getMemberId() { return memberId; }
        public void setMemberId(UUID memberId) { this.memberId = memberId; }
        public String getMemberName() { return memberName; }
        public void setMemberName(String memberName) { this.memberName = memberName; }
        public BigDecimal getRegularHours() { return regularHours; }
        public void setRegularHours(BigDecimal regularHours) { this.regularHours = regularHours; }
        public BigDecimal getOvertimeHours() { return overtimeHours; }
        public void setOvertimeHours(BigDecimal overtimeHours) { this.overtimeHours = overtimeHours; }
        public int getAttendanceDays() { return attendanceDays; }
        public void setAttendanceDays(int attendanceDays) { this.attendanceDays = attendanceDays; }
        public int getLateDays() { return lateDays; }
        public void setLateDays(int lateDays) { this.lateDays = lateDays; }
        public int getMissingCheckoutDays() { return missingCheckoutDays; }
        public void setMissingCheckoutDays(int missingCheckoutDays) { this.missingCheckoutDays = missingCheckoutDays; }
        public int getTotalTasks() { return totalTasks; }
        public void setTotalTasks(int totalTasks) { this.totalTasks = totalTasks; }
        public int getCompletedTasks() { return completedTasks; }
        public void setCompletedTasks(int completedTasks) { this.completedTasks = completedTasks; }
        public long getHourlyRateVnd() { return hourlyRateVnd; }
        public void setHourlyRateVnd(long hourlyRateVnd) { this.hourlyRateVnd = hourlyRateVnd; }
        public BigDecimal getOvertimeMultiplier() { return overtimeMultiplier; }
        public void setOvertimeMultiplier(BigDecimal overtimeMultiplier) { this.overtimeMultiplier = overtimeMultiplier; }
        public long getRegularPayVnd() { return regularPayVnd; }
        public void setRegularPayVnd(long regularPayVnd) { this.regularPayVnd = regularPayVnd; }
        public long getOvertimePayVnd() { return overtimePayVnd; }
        public void setOvertimePayVnd(long overtimePayVnd) { this.overtimePayVnd = overtimePayVnd; }
        public long getAllowanceVnd() { return allowanceVnd; }
        public void setAllowanceVnd(long allowanceVnd) { this.allowanceVnd = allowanceVnd; }
        public long getDeductionVnd() { return deductionVnd; }
        public void setDeductionVnd(long deductionVnd) { this.deductionVnd = deductionVnd; }
        public long getAdvanceVnd() { return advanceVnd; }
        public void setAdvanceVnd(long advanceVnd) { this.advanceVnd = advanceVnd; }
        public long getNetPayVnd() { return netPayVnd; }
        public void setNetPayVnd(long netPayVnd) { this.netPayVnd = netPayVnd; }
        public String getNote() { return note; }
        public void setNote(String note) { this.note = note; }
        public List<AttendanceLine> getAttendanceLines() { return attendanceLines; }
        public void setAttendanceLines(List<AttendanceLine> attendanceLines) { this.attendanceLines = attendanceLines; }
    }

    public static class AttendanceLine {
        private UUID id;
        private String date;
        private LocalDateTime checkInTime;
        private LocalDateTime checkOutTime;
        private LocalDateTime overtimeStartTime;
        private BigDecimal regularHours;
        private BigDecimal overtimeHours;
        private String attendanceStatus;
        private String shiftType;
        private String productionStage;
        private boolean payable;
        public UUID getId() { return id; }
        public void setId(UUID id) { this.id = id; }
        public String getDate() { return date; }
        public void setDate(String date) { this.date = date; }
        public LocalDateTime getCheckInTime() { return checkInTime; }
        public void setCheckInTime(LocalDateTime checkInTime) { this.checkInTime = checkInTime; }
        public LocalDateTime getCheckOutTime() { return checkOutTime; }
        public void setCheckOutTime(LocalDateTime checkOutTime) { this.checkOutTime = checkOutTime; }
        public LocalDateTime getOvertimeStartTime() { return overtimeStartTime; }
        public void setOvertimeStartTime(LocalDateTime overtimeStartTime) { this.overtimeStartTime = overtimeStartTime; }
        public BigDecimal getRegularHours() { return regularHours; }
        public void setRegularHours(BigDecimal regularHours) { this.regularHours = regularHours; }
        public BigDecimal getOvertimeHours() { return overtimeHours; }
        public void setOvertimeHours(BigDecimal overtimeHours) { this.overtimeHours = overtimeHours; }
        public String getAttendanceStatus() { return attendanceStatus; }
        public void setAttendanceStatus(String attendanceStatus) { this.attendanceStatus = attendanceStatus; }
        public String getShiftType() { return shiftType; }
        public void setShiftType(String shiftType) { this.shiftType = shiftType; }
        public String getProductionStage() { return productionStage; }
        public void setProductionStage(String productionStage) { this.productionStage = productionStage; }
        public boolean isPayable() { return payable; }
        public void setPayable(boolean payable) { this.payable = payable; }
    }

    public UUID getRunId() { return runId; }
    public void setRunId(UUID runId) { this.runId = runId; }
    public UUID getTeamId() { return teamId; }
    public void setTeamId(UUID teamId) { this.teamId = teamId; }
    public int getYear() { return year; }
    public void setYear(int year) { this.year = year; }
    public int getMonth() { return month; }
    public void setMonth(int month) { this.month = month; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
    public LocalDateTime getFinalizedAt() { return finalizedAt; }
    public void setFinalizedAt(LocalDateTime finalizedAt) { this.finalizedAt = finalizedAt; }
    public LocalDateTime getPaidAt() { return paidAt; }
    public void setPaidAt(LocalDateTime paidAt) { this.paidAt = paidAt; }
    public Summary getSummary() { return summary; }
    public void setSummary(Summary summary) { this.summary = summary; }
    public List<Item> getItems() { return items; }
    public void setItems(List<Item> items) { this.items = items; }
}
