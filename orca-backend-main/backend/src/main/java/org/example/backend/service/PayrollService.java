package org.example.backend.service;

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.example.backend.dto.PayrollReportDTO;
import org.example.backend.entity.*;
import org.example.backend.repository.*;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.io.ByteArrayOutputStream;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.YearMonth;
import java.time.ZoneId;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

@Service
public class PayrollService {
    private static final ZoneId VIETNAM_ZONE = ZoneId.of("Asia/Ho_Chi_Minh");
    public static final long DEFAULT_HOURLY_RATE = 50_000L;
    public static final BigDecimal DEFAULT_OVERTIME_MULTIPLIER = new BigDecimal("1.50");

    private final TeamRepository teamRepository;
    private final TeamMemberRepository memberRepository;
    private final AttendanceRepository attendanceRepository;
    private final TaskRepository taskRepository;
    private final UserRepository userRepository;
    private final PayrollProfileRepository profileRepository;
    private final PayrollRunRepository runRepository;
    private final PayrollItemRepository itemRepository;
    private final PayrollAttendanceLineRepository attendanceLineRepository;
    private final PayrollAuditLogRepository auditRepository;

    public PayrollService(TeamRepository teamRepository,
                          TeamMemberRepository memberRepository,
                          AttendanceRepository attendanceRepository,
                          TaskRepository taskRepository,
                          UserRepository userRepository,
                          PayrollProfileRepository profileRepository,
                          PayrollRunRepository runRepository,
                          PayrollItemRepository itemRepository,
                          PayrollAttendanceLineRepository attendanceLineRepository,
                          PayrollAuditLogRepository auditRepository) {
        this.teamRepository = teamRepository;
        this.memberRepository = memberRepository;
        this.attendanceRepository = attendanceRepository;
        this.taskRepository = taskRepository;
        this.userRepository = userRepository;
        this.profileRepository = profileRepository;
        this.runRepository = runRepository;
        this.itemRepository = itemRepository;
        this.attendanceLineRepository = attendanceLineRepository;
        this.auditRepository = auditRepository;
    }

    @Transactional
    public PayrollReportDTO getReport(UUID teamId, Integer year, Integer month) {
        YearMonth period = normalizePeriod(year, month);
        PayrollRun run = getOrCreateRun(teamId, period);
        if (run.getStatus() == PayrollRun.Status.DRAFT || run.getStatus() == PayrollRun.Status.CALCULATED) syncDraft(run);
        return toDto(run);
    }

    @Transactional(readOnly = true)
    public PayrollReportDTO.Item getMyPayslip(UUID teamId, UUID userId, Integer year, Integer month) {
        YearMonth period = normalizePeriod(year, month);
        PayrollRun run = runRepository.findByTeamIdAndYearAndMonth(teamId, period.getYear(), period.getMonthValue())
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Kỳ lương chưa được tạo"));
        if (run.getStatus() == PayrollRun.Status.DRAFT || run.getStatus() == PayrollRun.Status.CALCULATED) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Phiếu lương chỉ hiển thị sau khi quản lý chốt kỳ");
        }
        PayrollItem item = itemRepository.findByPayrollRunIdAndUserId(run.getId(), userId)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Không có phiếu lương"));
        return toItemDto(item);
    }

    @Transactional
    public PayrollReportDTO updateProfile(UUID teamId, UUID userId, long hourlyRateVnd,
                                          BigDecimal overtimeMultiplier, UUID actorId,
                                          Integer year, Integer month) {
        if (hourlyRateVnd < 1_000 || hourlyRateVnd > 10_000_000) {
            throw badRequest("Đơn giá giờ phải từ 1.000đ đến 10.000.000đ");
        }
        if (overtimeMultiplier == null || overtimeMultiplier.compareTo(BigDecimal.ONE) < 0
                || overtimeMultiplier.compareTo(new BigDecimal("3.00")) > 0) {
            throw badRequest("Hệ số tăng ca phải từ 1,00 đến 3,00");
        }
        TeamMember membership = memberRepository.findByTeamIdAndUserId(teamId, userId)
                .orElseThrow(() -> badRequest("Nhân viên không thuộc xưởng"));
        User actor = requireUser(actorId);
        PayrollProfile profile = profileRepository.findByTeamIdAndUserId(teamId, userId)
                .orElseGet(() -> newProfile(membership.getTeam(), membership.getUser()));
        profile.setHourlyRateVnd(hourlyRateVnd);
        profile.setOvertimeMultiplier(overtimeMultiplier.setScale(2, RoundingMode.HALF_UP));
        profile.setUpdatedBy(actor);
        profileRepository.save(profile);

        PayrollReportDTO report = getReport(teamId, year, month);
        PayrollRun run = requireRun(report.getRunId());
        audit(run, actor, "UPDATE_PAY_PROFILE",
                "Cập nhật đơn giá " + displayName(membership.getUser()) + " thành " + hourlyRateVnd + "đ/giờ");
        return toDto(run);
    }

    @Transactional
    public PayrollReportDTO updateAdjustments(UUID runId, UUID userId, long allowanceVnd,
                                              long deductionVnd, long advanceVnd, String note, UUID actorId) {
        validateMoney("Phụ cấp", allowanceVnd);
        validateMoney("Khấu trừ", deductionVnd);
        validateMoney("Tạm ứng", advanceVnd);
        PayrollRun run = requireEditableRun(runId);
        PayrollItem item = itemRepository.findByPayrollRunIdAndUserId(runId, userId)
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Không tìm thấy dòng lương"));
        long totalBeforeDeductions = Math.addExact(Math.addExact(item.getRegularPayVnd(), item.getOvertimePayVnd()), allowanceVnd);
        long totalDeductions = Math.addExact(deductionVnd, advanceVnd);
        if (totalDeductions > totalBeforeDeductions) {
            throw badRequest("Khoản trừ không được lớn hơn tiền lương và tiền thưởng của kỳ này");
        }
        String cleanedNote = cleanNote(note);
        if ((allowanceVnd > 0 || deductionVnd > 0 || advanceVnd > 0)
                && (cleanedNote == null || cleanedNote.length() < 5)) {
            throw badRequest("Lý do điều chỉnh phải có ít nhất 5 ký tự");
        }
        item.setAllowanceVnd(allowanceVnd);
        item.setDeductionVnd(deductionVnd);
        item.setAdvanceVnd(advanceVnd);
        item.setNote(cleanedNote);
        recalculateItem(item);
        itemRepository.save(item);
        recalculateRun(run);
        audit(run, requireUser(actorId), "UPDATE_ADJUSTMENT", "Cập nhật điều chỉnh cho " + item.getMemberNameSnapshot());
        return toDto(run);
    }

    @Transactional
    public PayrollReportDTO recalculate(UUID runId, UUID actorId) {
        PayrollRun run = requireEditableRun(runId);
        syncDraft(run);
        run.setStatus(PayrollRun.Status.CALCULATED);
        runRepository.save(run);
        audit(run, requireUser(actorId), "RECALCULATE", "Tính lại bảng lương từ dữ liệu chấm công");
        return toDto(run);
    }

    @Transactional
    public PayrollReportDTO finalizeRun(UUID runId, UUID actorId) {
        PayrollRun run = requireEditableRun(runId);
        syncDraft(run);
        int missingCheckouts = itemRepository.findByPayrollRunId(runId).stream()
                .mapToInt(PayrollItem::getMissingCheckoutDays).sum();
        if (missingCheckouts > 0) {
            throw badRequest("Còn " + missingCheckouts + " ca thiếu giờ ra. Hãy xử lý trước khi chốt lương.");
        }
        User actor = requireUser(actorId);
        if (run.getStatus() == PayrollRun.Status.DRAFT) {
            throw badRequest("Hãy tính bảng lương trước khi duyệt");
        }
        run.setStatus(PayrollRun.Status.APPROVED);
        run.setFinalizedBy(actor);
        run.setFinalizedAt(LocalDateTime.now(VIETNAM_ZONE));
        runRepository.save(run);
        audit(run, actor, "FINALIZE", "Chốt kỳ lương " + String.format("%02d/%d", run.getMonth(), run.getYear()));
        return toDto(run);
    }

    @Transactional
    public PayrollReportDTO reopen(UUID runId, UUID actorId) {
        PayrollRun run = requireRun(runId);
        if (run.getStatus() == PayrollRun.Status.PAID) throw badRequest("Kỳ lương đã thanh toán không thể mở lại");
        if (run.getStatus() != PayrollRun.Status.APPROVED && run.getStatus() != PayrollRun.Status.CALCULATED) {
            throw badRequest("Chỉ kỳ lương đã tính hoặc đã duyệt mới có thể mở lại");
        }
        run.setStatus(PayrollRun.Status.DRAFT);
        run.setFinalizedBy(null);
        run.setFinalizedAt(null);
        runRepository.save(run);
        audit(run, requireUser(actorId), "REOPEN", "Mở lại kỳ lương để điều chỉnh");
        return toDto(run);
    }

    @Transactional
    public PayrollReportDTO markPaid(UUID runId, UUID actorId) {
        PayrollRun run = requireRun(runId);
        if (run.getStatus() != PayrollRun.Status.APPROVED) {
            throw badRequest("Phải duyệt bảng lương trước khi xác nhận thanh toán");
        }
        User actor = requireUser(actorId);
        run.setStatus(PayrollRun.Status.PAID);
        run.setPaidBy(actor);
        run.setPaidAt(LocalDateTime.now(VIETNAM_ZONE));
        runRepository.save(run);
        audit(run, actor, "MARK_PAID", "Xác nhận đã thanh toán " + run.getNetPayVnd() + "đ");
        return toDto(run);
    }

    @Transactional
    public byte[] exportExcel(UUID teamId, Integer year, Integer month) throws Exception {
        PayrollReportDTO report = getReport(teamId, year, month);
        try (Workbook workbook = new XSSFWorkbook(); ByteArrayOutputStream output = new ByteArrayOutputStream()) {
            Sheet sheet = workbook.createSheet("Bang luong");
            String[] headers = {"Nhân viên", "Ngày công", "Giờ thường", "Tăng ca", "Đơn giá/giờ",
                    "Lương thường", "Lương tăng ca", "Phụ cấp", "Khấu trừ", "Tạm ứng", "Thực nhận", "Ghi chú"};
            Row header = sheet.createRow(0);
            CellStyle headerStyle = workbook.createCellStyle();
            Font font = workbook.createFont(); font.setBold(true); headerStyle.setFont(font);
            for (int i = 0; i < headers.length; i++) { Cell cell = header.createCell(i); cell.setCellValue(headers[i]); cell.setCellStyle(headerStyle); }
            int rowIndex = 1;
            for (PayrollReportDTO.Item item : report.getItems()) {
                Row row = sheet.createRow(rowIndex++);
                row.createCell(0).setCellValue(item.getMemberName());
                row.createCell(1).setCellValue(item.getAttendanceDays());
                row.createCell(2).setCellValue(item.getRegularHours().doubleValue());
                row.createCell(3).setCellValue(item.getOvertimeHours().doubleValue());
                row.createCell(4).setCellValue(item.getHourlyRateVnd());
                row.createCell(5).setCellValue(item.getRegularPayVnd());
                row.createCell(6).setCellValue(item.getOvertimePayVnd());
                row.createCell(7).setCellValue(item.getAllowanceVnd());
                row.createCell(8).setCellValue(item.getDeductionVnd());
                row.createCell(9).setCellValue(item.getAdvanceVnd());
                row.createCell(10).setCellValue(item.getNetPayVnd());
                row.createCell(11).setCellValue(item.getNote() == null ? "" : item.getNote());
            }
            Row total = sheet.createRow(rowIndex);
            total.createCell(0).setCellValue("TỔNG CỘNG");
            total.createCell(2).setCellValue(report.getSummary().getRegularHours().doubleValue());
            total.createCell(3).setCellValue(report.getSummary().getOvertimeHours().doubleValue());
            total.createCell(10).setCellValue(report.getSummary().getNetPayVnd());
            for (int i = 0; i < headers.length; i++) sheet.autoSizeColumn(i);

            Sheet attendanceSheet = workbook.createSheet("Chi tiet cham cong");
            String[] attendanceHeaders = {"Nhân viên", "Ngày", "Vào ca", "Ra ca", "Giờ thường",
                    "Bắt đầu tăng ca", "Kết thúc tăng ca", "Giờ tăng ca", "Trạng thái", "Được tính lương"};
            Row attendanceHeader = attendanceSheet.createRow(0);
            for (int i = 0; i < attendanceHeaders.length; i++) {
                Cell cell = attendanceHeader.createCell(i); cell.setCellValue(attendanceHeaders[i]); cell.setCellStyle(headerStyle);
            }
            int attendanceRowIndex = 1;
            for (PayrollReportDTO.Item item : report.getItems()) {
                for (PayrollReportDTO.AttendanceLine line : item.getAttendanceLines()) {
                    Row row = attendanceSheet.createRow(attendanceRowIndex++);
                    row.createCell(0).setCellValue(item.getMemberName());
                    row.createCell(1).setCellValue(line.getDate());
                    row.createCell(2).setCellValue(line.getCheckInTime() == null ? "" : line.getCheckInTime().toLocalTime().toString());
                    row.createCell(3).setCellValue(line.getCheckOutTime() == null ? "" : line.getCheckOutTime().toLocalTime().toString());
                    row.createCell(4).setCellValue(line.getRegularHours().doubleValue());
                    row.createCell(5).setCellValue(line.getOvertimeStartTime() == null ? "" : line.getOvertimeStartTime().toLocalTime().toString());
                    row.createCell(6).setCellValue(line.getOvertimeHours().signum() > 0 && line.getCheckOutTime() != null ? line.getCheckOutTime().toLocalTime().toString() : "");
                    row.createCell(7).setCellValue(line.getOvertimeHours().doubleValue());
                    row.createCell(8).setCellValue(line.getAttendanceStatus() == null ? "" : line.getAttendanceStatus());
                    row.createCell(9).setCellValue(line.isPayable() ? "Có" : "Không");
                }
            }
            for (int i = 0; i < attendanceHeaders.length; i++) attendanceSheet.autoSizeColumn(i);
            workbook.write(output);
            return output.toByteArray();
        }
    }

    @Transactional(readOnly = true)
    public UUID getRunTeamId(UUID runId) { return requireRun(runId).getTeam().getId(); }

    private PayrollRun getOrCreateRun(UUID teamId, YearMonth period) {
        return runRepository.findByTeamIdAndYearAndMonth(teamId, period.getYear(), period.getMonthValue())
                .orElseGet(() -> {
                    Team team = teamRepository.findById(teamId)
                            .orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Không tìm thấy xưởng"));
                    PayrollRun run = new PayrollRun();
                    run.setTeam(team); run.setYear(period.getYear()); run.setMonth(period.getMonthValue());
                    return runRepository.save(run);
                });
    }

    private void syncDraft(PayrollRun run) {
        YearMonth period = YearMonth.of(run.getYear(), run.getMonth());
        LocalDate start = period.atDay(1); LocalDate end = period.atEndOfMonth();
        List<TeamMember> members = memberRepository.findByTeamId(run.getTeam().getId());
        Map<UUID, List<Attendance>> attendanceByUser = attendanceRepository
                .findByTeamIdAndDateBetween(run.getTeam().getId(), start, end).stream()
                .collect(Collectors.groupingBy(a -> a.getUser().getId()));
        Map<UUID, List<Task>> tasksByUser = taskRepository.findByGoalTeamId(run.getTeam().getId()).stream()
                .filter(task -> task.getMember() != null && isTaskInPeriod(task, period))
                .collect(Collectors.groupingBy(task -> task.getMember().getId()));
        Map<UUID, PayrollProfile> profiles = profileRepository.findByTeamId(run.getTeam().getId()).stream()
                .collect(Collectors.toMap(p -> p.getUser().getId(), Function.identity()));
        Map<UUID, PayrollItem> existing = itemRepository.findByPayrollRunId(run.getId()).stream()
                .collect(Collectors.toMap(item -> item.getUser().getId(), Function.identity()));
        Set<UUID> activeUsers = new HashSet<>();

        for (TeamMember member : members) {
            UUID userId = member.getUser().getId(); activeUsers.add(userId);
            PayrollProfile profile = profiles.computeIfAbsent(userId, ignored -> profileRepository.save(newProfile(run.getTeam(), member.getUser())));
            PayrollItem item = existing.getOrDefault(userId, new PayrollItem());
            if (item.getId() == null) { item.setPayrollRun(run); item.setUser(member.getUser()); }
            item.setMemberNameSnapshot(displayName(member.getUser()));
            List<Attendance> records = attendanceByUser.getOrDefault(userId, List.of());
            List<Attendance> payable = records.stream().filter(this::isPayableAttendance).toList();
            item.setRegularHours(sumHours(payable, false));
            item.setOvertimeHours(sumHours(payable, true));
            item.setAttendanceDays((int) payable.stream().map(Attendance::getDate).distinct().count());
            item.setLateDays((int) records.stream().filter(a -> a.getAttendanceStatus() == Attendance.AttendanceStatus.LATE).count());
            item.setMissingCheckoutDays((int) records.stream().filter(a -> a.getCheckOutTime() == null
                    || a.getAttendanceStatus() == Attendance.AttendanceStatus.MISSING_CHECKOUT).count());
            List<Task> tasks = tasksByUser.getOrDefault(userId, List.of());
            item.setTotalTasks(tasks.size());
            item.setCompletedTasks((int) tasks.stream().filter(t -> "COMPLETED".equalsIgnoreCase(t.getStatus())).count());
            item.setHourlyRateVnd(profile.getHourlyRateVnd());
            item.setOvertimeMultiplier(profile.getOvertimeMultiplier());
            recalculateItem(item);
            item = itemRepository.save(item);
            syncAttendanceLines(item, records);
        }
        existing.values().stream().filter(item -> !activeUsers.contains(item.getUser().getId())).forEach(itemRepository::delete);
        recalculateRun(run);
    }

    private boolean isPayableAttendance(Attendance attendance) {
        return attendance.getCheckInTime() != null && attendance.getCheckOutTime() != null
                && attendance.getAttendanceStatus() != Attendance.AttendanceStatus.ABSENT
                && attendance.getAttendanceStatus() != Attendance.AttendanceStatus.MISSING_CHECKOUT;
    }

    private BigDecimal sumHours(List<Attendance> records, boolean overtime) {
        return records.stream().map(a -> overtime ? a.getOvertimeHours() : a.getRegularHours())
                .filter(Objects::nonNull).map(BigDecimal::valueOf).reduce(BigDecimal.ZERO, BigDecimal::add)
                .setScale(2, RoundingMode.HALF_UP);
    }

    private void recalculateItem(PayrollItem item) {
        long regular = PayrollCalculator.multiply(item.getRegularHours(), item.getHourlyRateVnd(), BigDecimal.ONE);
        long overtime = PayrollCalculator.multiply(item.getOvertimeHours(), item.getHourlyRateVnd(), item.getOvertimeMultiplier());
        item.setRegularPayVnd(regular); item.setOvertimePayVnd(overtime);
        item.setNetPayVnd(PayrollCalculator.net(regular, overtime, safe(item.getAllowanceVnd()),
                safe(item.getDeductionVnd()), safe(item.getAdvanceVnd())));
    }

    private void recalculateRun(PayrollRun run) {
        List<PayrollItem> items = itemRepository.findByPayrollRunId(run.getId());
        run.setRegularHours(items.stream().map(PayrollItem::getRegularHours).reduce(BigDecimal.ZERO, BigDecimal::add));
        run.setOvertimeHours(items.stream().map(PayrollItem::getOvertimeHours).reduce(BigDecimal.ZERO, BigDecimal::add));
        run.setGrossPayVnd(items.stream().mapToLong(i -> i.getRegularPayVnd() + i.getOvertimePayVnd()).sum());
        run.setAllowanceVnd(items.stream().mapToLong(i -> safe(i.getAllowanceVnd())).sum());
        run.setDeductionVnd(items.stream().mapToLong(i -> safe(i.getDeductionVnd())).sum());
        run.setAdvanceVnd(items.stream().mapToLong(i -> safe(i.getAdvanceVnd())).sum());
        run.setNetPayVnd(items.stream().mapToLong(i -> safe(i.getNetPayVnd())).sum());
        runRepository.save(run);
    }

    private PayrollReportDTO toDto(PayrollRun run) {
        List<PayrollItem> items = itemRepository.findByPayrollRunId(run.getId()).stream()
                .sorted(Comparator.comparing(PayrollItem::getMemberNameSnapshot, String.CASE_INSENSITIVE_ORDER))
                .toList();
        PayrollReportDTO dto = new PayrollReportDTO();
        dto.setRunId(run.getId()); dto.setTeamId(run.getTeam().getId()); dto.setYear(run.getYear()); dto.setMonth(run.getMonth());
        dto.setStatus(run.getStatus().name()); dto.setUpdatedAt(run.getUpdatedAt()); dto.setFinalizedAt(run.getFinalizedAt()); dto.setPaidAt(run.getPaidAt());
        dto.setItems(items.stream().map(this::toItemDto).toList());
        PayrollReportDTO.Summary summary = new PayrollReportDTO.Summary();
        summary.setMemberCount(items.size()); summary.setPaidMemberCount((int) items.stream().filter(i -> i.getNetPayVnd() > 0).count());
        summary.setAttendanceDays(items.stream().mapToInt(PayrollItem::getAttendanceDays).sum());
        summary.setRegularHours(run.getRegularHours()); summary.setOvertimeHours(run.getOvertimeHours());
        summary.setTotalHours(run.getRegularHours().add(run.getOvertimeHours())); summary.setGrossPayVnd(run.getGrossPayVnd());
        summary.setAllowanceVnd(run.getAllowanceVnd()); summary.setDeductionVnd(run.getDeductionVnd());
        summary.setAdvanceVnd(run.getAdvanceVnd()); summary.setNetPayVnd(run.getNetPayVnd());
        summary.setTotalTasks(items.stream().mapToInt(PayrollItem::getTotalTasks).sum());
        summary.setCompletedTasks(items.stream().mapToInt(PayrollItem::getCompletedTasks).sum());
        summary.setMissingCheckoutCount(items.stream().mapToInt(PayrollItem::getMissingCheckoutDays).sum());
        dto.setSummary(summary); return dto;
    }

    private PayrollReportDTO.Item toItemDto(PayrollItem item) {
        PayrollReportDTO.Item dto = new PayrollReportDTO.Item();
        dto.setItemId(item.getId()); dto.setMemberId(item.getUser().getId()); dto.setMemberName(item.getMemberNameSnapshot());
        dto.setRegularHours(item.getRegularHours()); dto.setOvertimeHours(item.getOvertimeHours()); dto.setAttendanceDays(item.getAttendanceDays());
        dto.setLateDays(item.getLateDays()); dto.setMissingCheckoutDays(item.getMissingCheckoutDays());
        dto.setTotalTasks(item.getTotalTasks()); dto.setCompletedTasks(item.getCompletedTasks()); dto.setHourlyRateVnd(item.getHourlyRateVnd());
        dto.setOvertimeMultiplier(item.getOvertimeMultiplier()); dto.setRegularPayVnd(item.getRegularPayVnd()); dto.setOvertimePayVnd(item.getOvertimePayVnd());
        dto.setAllowanceVnd(item.getAllowanceVnd()); dto.setDeductionVnd(item.getDeductionVnd()); dto.setAdvanceVnd(item.getAdvanceVnd());
        dto.setNetPayVnd(item.getNetPayVnd()); dto.setNote(item.getNote());
        dto.setAttendanceLines(attendanceLines(item));
        return dto;
    }

    private void syncAttendanceLines(PayrollItem item, List<Attendance> records) {
        attendanceLineRepository.deleteAll(attendanceLineRepository.findByPayrollItemId(item.getId()));
        attendanceLineRepository.flush();
        for (Attendance attendance : records.stream()
                .sorted(Comparator.comparing(Attendance::getDate)
                        .thenComparing(Attendance::getCheckInTime, Comparator.nullsLast(Comparator.naturalOrder())))
                .toList()) {
            PayrollAttendanceLine line = new PayrollAttendanceLine();
            line.setPayrollItem(item);
            line.setSourceAttendanceId(attendance.getId());
            line.setAttendanceDate(attendance.getDate());
            line.setCheckInTime(attendance.getCheckInTime());
            line.setCheckOutTime(attendance.getCheckOutTime());
            line.setRegularHours(BigDecimal.valueOf(attendance.getRegularHours() == null ? 0 : attendance.getRegularHours()).setScale(2, RoundingMode.HALF_UP));
            line.setOvertimeHours(BigDecimal.valueOf(attendance.getOvertimeHours() == null ? 0 : attendance.getOvertimeHours()).setScale(2, RoundingMode.HALF_UP));
            line.setAttendanceStatus(attendance.getAttendanceStatus() == null ? null : attendance.getAttendanceStatus().name());
            line.setShiftType(attendance.getShiftType() == null ? null : attendance.getShiftType().name());
            line.setProductionStage(attendance.getStage() == null ? null : attendance.getStage().name());
            line.setPayable(isPayableAttendance(attendance));
            attendanceLineRepository.save(line);
        }
    }

    private List<PayrollReportDTO.AttendanceLine> attendanceLines(PayrollItem item) {
        return attendanceLineRepository.findByPayrollItemIdOrderByAttendanceDateAscCheckInTimeAsc(item.getId()).stream()
                .map(line -> {
                    PayrollReportDTO.AttendanceLine dto = new PayrollReportDTO.AttendanceLine();
                    dto.setId(line.getId());
                    dto.setDate(line.getAttendanceDate().toString());
                    dto.setCheckInTime(line.getCheckInTime());
                    dto.setCheckOutTime(line.getCheckOutTime());
                    if (line.getCheckOutTime() != null && line.getOvertimeHours().compareTo(BigDecimal.ZERO) > 0) {
                        dto.setOvertimeStartTime(line.getCheckOutTime().minusMinutes(
                                line.getOvertimeHours().multiply(BigDecimal.valueOf(60)).longValue()));
                    }
                    dto.setRegularHours(line.getRegularHours());
                    dto.setOvertimeHours(line.getOvertimeHours());
                    dto.setAttendanceStatus(line.getAttendanceStatus());
                    dto.setShiftType(line.getShiftType());
                    dto.setProductionStage(line.getProductionStage());
                    dto.setPayable(line.isPayable());
                    return dto;
                }).toList();
    }

    private PayrollProfile newProfile(Team team, User user) {
        PayrollProfile profile = new PayrollProfile(); profile.setTeam(team); profile.setUser(user);
        profile.setHourlyRateVnd(DEFAULT_HOURLY_RATE); profile.setOvertimeMultiplier(DEFAULT_OVERTIME_MULTIPLIER); return profile;
    }
    private boolean isTaskInPeriod(Task task, YearMonth period) {
        LocalDateTime date = task.getDueTime() != null ? task.getDueTime() : task.getDeadline() != null ? task.getDeadline() : task.getCreatedAt();
        return date != null && YearMonth.from(date).equals(period);
    }
    private YearMonth normalizePeriod(Integer year, Integer month) {
        YearMonth now = YearMonth.now(VIETNAM_ZONE);
        int y = year == null ? now.getYear() : year; int m = month == null ? now.getMonthValue() : month;
        if (y < 2020 || y > now.getYear() + 1 || m < 1 || m > 12) throw badRequest("Kỳ lương không hợp lệ");
        return YearMonth.of(y, m);
    }
    private PayrollRun requireRun(UUID runId) { return runRepository.findById(runId).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Không tìm thấy kỳ lương")); }
    private PayrollRun requireEditableRun(UUID runId) { PayrollRun run = requireRun(runId); if (run.getStatus() != PayrollRun.Status.DRAFT && run.getStatus() != PayrollRun.Status.CALCULATED) throw badRequest("Kỳ lương đã duyệt, không thể chỉnh sửa"); return run; }
    private User requireUser(UUID id) { return userRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Không tìm thấy người dùng")); }
    private void audit(PayrollRun run, User actor, String action, String details) { PayrollAuditLog log = new PayrollAuditLog(); log.setPayrollRun(run); log.setActor(actor); log.setAction(action); log.setDetails(details); auditRepository.save(log); }
    private void validateMoney(String label, long value) { if (value < 0 || value > 1_000_000_000L) throw badRequest(label + " không hợp lệ"); }
    private String cleanNote(String note) { if (note == null || note.isBlank()) return null; String value = note.trim(); return value.length() > 500 ? value.substring(0, 500) : value; }
    private String displayName(User user) { return user.getFullName() == null || user.getFullName().isBlank() ? user.getUsername() : user.getFullName(); }
    private long safe(Long value) { return value == null ? 0L : value; }
    private ResponseStatusException badRequest(String message) { return new ResponseStatusException(HttpStatus.BAD_REQUEST, message); }
}
