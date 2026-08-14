package org.example.backend.service;

import org.example.backend.dto.AttendanceDTO;
import org.example.backend.dto.AttendanceCorrectionDTO;
import org.example.backend.dto.AttendanceSettingsDTO;
import org.example.backend.dto.UpdateAttendanceRequest;
import org.example.backend.entity.Attendance;
import org.example.backend.entity.AttendanceCorrection;
import org.example.backend.entity.AttendanceSettings;
import org.example.backend.entity.Attendance.ShiftType;
import org.example.backend.entity.ProductionOrder;
import org.example.backend.entity.Team;
import org.example.backend.entity.User;
import org.example.backend.repository.AttendanceRepository;
import org.example.backend.repository.AttendanceCorrectionRepository;
import org.example.backend.repository.AttendanceSettingsRepository;
import org.example.backend.repository.ProductionOrderRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.ZoneId;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@Transactional
public class AttendanceService {
    private static final ZoneId VIETNAM_ZONE = ZoneId.of("Asia/Ho_Chi_Minh");

    private final AttendanceRepository attendanceRepo;
    private final UserRepository userRepo;
    private final TeamRepository teamRepo;
    private final ProductionOrderRepository orderRepo;
    private final AttendanceCorrectionRepository correctionRepo;
    private final AttendanceSettingsRepository settingsRepo;

    public AttendanceService(AttendanceRepository attendanceRepo, UserRepository userRepo,
                            TeamRepository teamRepo, ProductionOrderRepository orderRepo,
                            AttendanceCorrectionRepository correctionRepo,
                            AttendanceSettingsRepository settingsRepo) {
        this.attendanceRepo = attendanceRepo;
        this.userRepo = userRepo;
        this.teamRepo = teamRepo;
        this.orderRepo = orderRepo;
        this.correctionRepo = correctionRepo;
        this.settingsRepo = settingsRepo;
    }

    public AttendanceDTO checkIn(UUID userId, UUID teamId, ShiftType shiftType,
                                 Attendance.ProductionStage stage, UUID orderId, Integer breakMinutes) {
        LocalDate today = LocalDate.now(VIETNAM_ZONE);
        Optional<Attendance> existing = attendanceRepo.findFirstByUserIdAndTeamIdAndCheckOutTimeIsNullOrderByCheckInTimeDesc(userId, teamId);
        if (existing.isPresent()) {
            throw new RuntimeException("Ban dang trong ca lam, hay tan ca truoc khi vao ca moi");
        }
        if (attendanceRepo.findFirstByUserIdAndTeamIdAndDateOrderByCheckInTimeDesc(userId, teamId, today).isPresent()) {
            throw new RuntimeException("Hôm nay bạn đã có một ca làm được ghi nhận");
        }

        User user = userRepo.findById(userId)
                .orElseThrow(() -> new RuntimeException("User not found"));
        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        AttendanceSettings settings = getOrCreateSettings(team);

        Attendance a = new Attendance();
        a.setUser(user);
        a.setTeam(team);
        a.setDate(today);
        a.setCheckInTime(LocalDateTime.now(VIETNAM_ZONE));
        a.setShiftType(ShiftType.NGAY);
        a.setStage(stage);
        // Snapshot the active workshop settings so later configuration changes never rewrite history.
        a.setBreakMinutes(0);
        a.setShiftStartTime(settings.getWorkStartTime().toString());
        a.setShiftEndTime(settings.getWorkEndTime().toString());
        a.setStandardHoursSnapshot(settings.getStandardHours());
        a.setHourlyRateVndSnapshot(settings.getHourlyRateVnd());
        a.setOvertimeMultiplierSnapshot(settings.getOvertimeMultiplier());

        if (orderId != null) {
            ProductionOrder order = orderRepo.findById(orderId).orElse(null);
            a.setProductionOrder(order);
        }

        return toDTO(attendanceRepo.save(a));
    }

    public AttendanceDTO checkOut(UUID userId, UUID teamId) {
        Attendance a = attendanceRepo.findFirstByUserIdAndTeamIdAndCheckOutTimeIsNullOrderByCheckInTimeDesc(userId, teamId)
                .orElseThrow(() -> new RuntimeException("Ban chua vao ca hoac da tan ca"));

        if (a.getCheckOutTime() != null) {
            throw new RuntimeException("Ban da check-out hom nay roi");
        }

        a.setCheckOutTime(LocalDateTime.now(VIETNAM_ZONE));

        recalculate(a);

        return toDTO(attendanceRepo.save(a));
    }

    public AttendanceDTO getTodayAttendance(UUID userId, UUID teamId) {
        LocalDate today = LocalDate.now(VIETNAM_ZONE);
        return attendanceRepo.findFirstByUserIdAndTeamIdAndDateAndCheckOutTimeIsNullOrderByCheckInTimeDesc(userId, teamId, today)
                .or(() -> attendanceRepo.findFirstByUserIdAndTeamIdAndDateOrderByCheckInTimeDesc(userId, teamId, today))
                .map(this::toDTO)
                .orElse(null);
    }

    public List<AttendanceDTO> getAttendanceHistory(UUID userId, UUID teamId) {
        return attendanceRepo.findByUserIdAndTeamId(userId, teamId).stream()
                .sorted((a, b) -> b.getCheckInTime().compareTo(a.getCheckInTime()))
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    public List<AttendanceDTO> getTeamAttendanceToday(UUID teamId) {
        return getTeamAttendanceByDate(teamId, LocalDate.now(VIETNAM_ZONE));
    }

    public List<AttendanceDTO> getTeamAttendanceByDate(UUID teamId, LocalDate date) {
        LocalDate selectedDate = date == null ? LocalDate.now(VIETNAM_ZONE) : date;
        return attendanceRepo.findByTeamIdAndDate(teamId, selectedDate).stream()
                .sorted((a, b) -> a.getUser().getFullName().compareToIgnoreCase(b.getUser().getFullName()))
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    public List<AttendanceDTO> getTeamAttendanceHistory(UUID teamId) {
        return attendanceRepo.findByTeamId(teamId).stream()
                .sorted((a, b) -> b.getCheckInTime().compareTo(a.getCheckInTime()))
                .map(this::toDTO)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public AttendanceSettingsDTO getSettings(UUID teamId) {
        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        return toSettingsDTO(settingsRepo.findByTeamId(teamId).orElseGet(() -> defaultSettings(team)));
    }

    public AttendanceSettingsDTO updateSettings(UUID teamId, AttendanceSettingsDTO request) {
        Team team = teamRepo.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        validateSettings(request);
        AttendanceSettings settings = settingsRepo.findByTeamId(teamId).orElseGet(() -> defaultSettings(team));
        settings.setWorkStartTime(request.getWorkStartTime());
        settings.setWorkEndTime(request.getWorkEndTime());
        settings.setStandardHours(request.getStandardHours().setScale(2, RoundingMode.HALF_UP));
        settings.setHourlyRateVnd(request.getHourlyRateVnd());
        settings.setOvertimeMultiplier(request.getOvertimeMultiplier().setScale(2, RoundingMode.HALF_UP));
        return toSettingsDTO(settingsRepo.save(settings));
    }

    @Transactional(readOnly = true)
    public UUID getAttendanceTeamId(UUID attendanceId) {
        return attendanceRepo.findById(attendanceId)
                .map(attendance -> attendance.getTeam().getId())
                .orElseThrow(() -> new RuntimeException("Attendance record not found"));
    }

    @Transactional(readOnly = true)
    public List<AttendanceCorrectionDTO> getCorrections(UUID attendanceId) {
        if (!attendanceRepo.existsById(attendanceId)) {
            throw new RuntimeException("Attendance record not found");
        }
        return correctionRepo.findByAttendanceIdOrderByCreatedAtDesc(attendanceId).stream().map(correction -> {
            AttendanceCorrectionDTO dto = new AttendanceCorrectionDTO();
            dto.setId(correction.getId());
            String actorName = correction.getActor().getFullName();
            dto.setActorName(actorName == null || actorName.isBlank() ? correction.getActor().getUsername() : actorName);
            dto.setOldCheckInTime(correction.getOldCheckInTime());
            dto.setOldCheckOutTime(correction.getOldCheckOutTime());
            dto.setNewCheckInTime(correction.getNewCheckInTime());
            dto.setNewCheckOutTime(correction.getNewCheckOutTime());
            dto.setReason(correction.getReason());
            dto.setCreatedAt(correction.getCreatedAt());
            return dto;
        }).toList();
    }

    public AttendanceDTO updateAttendance(UUID attendanceId, UpdateAttendanceRequest req, UUID actorId) {
        Attendance a = attendanceRepo.findById(attendanceId)
                .orElseThrow(() -> new RuntimeException("Attendance record not found"));
        if (req.getCheckInTime() == null || req.getCheckOutTime() == null) {
            throw new RuntimeException("Cần nhập đầy đủ giờ vào và giờ ra");
        }
        String reason = req.getReason() == null ? "" : req.getReason().trim();
        if (reason.length() < 5 || reason.length() > 500) {
            throw new RuntimeException("Lý do sửa công phải từ 5 đến 500 ký tự");
        }
        if (!req.getCheckOutTime().isAfter(req.getCheckInTime())) {
            throw new RuntimeException("Giờ ra phải sau giờ vào");
        }
        LocalDate correctedDate = req.getCheckInTime().toLocalDate();
        attendanceRepo.findFirstByUserIdAndTeamIdAndDateOrderByCheckInTimeDesc(
                        a.getUser().getId(), a.getTeam().getId(), correctedDate)
                .filter(existing -> !existing.getId().equals(a.getId()))
                .ifPresent(existing -> {
                    throw new RuntimeException("Nhân viên đã có bản chấm công trong ngày này");
                });
        LocalDateTime oldCheckIn = a.getCheckInTime();
        LocalDateTime oldCheckOut = a.getCheckOutTime();
        a.setCheckInTime(req.getCheckInTime());
        a.setCheckOutTime(req.getCheckOutTime());
        a.setDate(correctedDate);
        recalculate(a);
        attendanceRepo.save(a);

        AttendanceCorrection correction = new AttendanceCorrection();
        correction.setAttendance(a);
        correction.setActor(userRepo.findById(actorId).orElseThrow(() -> new RuntimeException("User not found")));
        correction.setOldCheckInTime(oldCheckIn);
        correction.setOldCheckOutTime(oldCheckOut);
        correction.setNewCheckInTime(a.getCheckInTime());
        correction.setNewCheckOutTime(a.getCheckOutTime());
        correction.setReason(reason);
        correctionRepo.save(correction);
        return toDTO(a);
    }

    private void recalculate(Attendance attendance) {
        AttendanceCalculator.Result result;
        if (attendance.getStandardHoursSnapshot() == null) {
            result = AttendanceCalculator.calculateLegacy(
                    attendance.getCheckInTime(), attendance.getCheckOutTime(),
                    attendance.getBreakMinutes() == null ? 60 : attendance.getBreakMinutes());
        } else {
            LocalTime scheduledEnd = parseTime(attendance.getShiftEndTime(), AttendanceSettings.DEFAULT_END_TIME);
            result = AttendanceCalculator.calculate(
                    attendance.getCheckInTime(), attendance.getCheckOutTime(),
                    scheduledEnd, attendance.getStandardHoursSnapshot());
        }
        attendance.setActualWorkHours(result.totalHours().doubleValue());
        attendance.setRegularHours(result.regularHours().doubleValue());
        attendance.setOvertimeHours(result.overtimeHours().doubleValue());
        String expectedStart = attendance.getShiftStartTime();
        if (expectedStart != null) {
            String[] parts = expectedStart.split(":");
            LocalDateTime scheduled = attendance.getCheckInTime().toLocalDate()
                    .atTime(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
            attendance.setAttendanceStatus(attendance.getCheckInTime().isAfter(scheduled.plusMinutes(5))
                    ? Attendance.AttendanceStatus.LATE : Attendance.AttendanceStatus.ON_TIME);
        } else {
            attendance.setAttendanceStatus(Attendance.AttendanceStatus.ON_TIME);
        }
    }

    public Map<String, Double> getStageWorkerHours(UUID teamId, LocalDate date) {
        List<Attendance> attendances = attendanceRepo.findByTeamIdAndDate(teamId, date);
        return attendances.stream()
                .filter(a -> a.getStage() != null)
                .collect(Collectors.groupingBy(
                        a -> a.getStage().name(),
                        Collectors.summingDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                ));
    }

    public Double getOrderWorkerHours(UUID orderId) {
        List<Attendance> attendances = attendanceRepo.findByOrderId(orderId);
        return attendances.stream()
                .mapToDouble(a -> a.getRegularHours() + a.getOvertimeHours())
                .sum();
    }

    private AttendanceDTO toDTO(Attendance a) {
        AttendanceDTO dto = new AttendanceDTO();
        dto.setId(a.getId().toString());
        dto.setUserId(a.getUser().getId().toString());
        dto.setUserName(a.getUser().getFullName());
        dto.setTeamId(a.getTeam().getId().toString());
        dto.setDate(a.getDate());
        dto.setShiftType(a.getShiftType() != null ? a.getShiftType().name() : null);
        dto.setShiftStartTime(a.getShiftStartTime());
        dto.setShiftEndTime(a.getShiftEndTime());
        dto.setCheckInTime(a.getCheckInTime());
        dto.setCheckOutTime(a.getCheckOutTime());
        dto.setProductionStage(a.getStage() != null ? a.getStage().name() : null);
        if (a.getProductionOrder() != null) {
            dto.setOrderId(a.getProductionOrder().getId().toString());
            dto.setOrderTitle(a.getProductionOrder().getTitle());
        }
        dto.setBreakMinutes(a.getBreakMinutes());
        dto.setStandardHours(a.getStandardHoursSnapshot() == null ? null : a.getStandardHoursSnapshot().doubleValue());
        dto.setActualWorkHours(a.getActualWorkHours());
        dto.setWorkedHours(a.getActualWorkHours());
        dto.setRegularHours(a.getRegularHours());
        dto.setOvertimeHours(a.getOvertimeHours());
        long hourlyRate = a.getHourlyRateVndSnapshot() == null
                ? AttendanceSettings.DEFAULT_HOURLY_RATE_VND : a.getHourlyRateVndSnapshot();
        BigDecimal overtimeMultiplier = a.getOvertimeMultiplierSnapshot() == null
                ? AttendanceSettings.DEFAULT_OVERTIME_MULTIPLIER : a.getOvertimeMultiplierSnapshot();
        BigDecimal regularHours = BigDecimal.valueOf(a.getRegularHours() == null ? 0 : a.getRegularHours());
        BigDecimal overtimeHours = BigDecimal.valueOf(a.getOvertimeHours() == null ? 0 : a.getOvertimeHours());
        long regularPay = PayrollCalculator.multiply(regularHours, hourlyRate, BigDecimal.ONE);
        long overtimePay = PayrollCalculator.multiply(overtimeHours, hourlyRate, overtimeMultiplier);
        dto.setHourlyRateVnd(hourlyRate);
        dto.setOvertimeMultiplier(overtimeMultiplier);
        dto.setRegularPayVnd(regularPay);
        dto.setOvertimePayVnd(overtimePay);
        dto.setTotalPayVnd(Math.addExact(regularPay, overtimePay));
        String status = a.getAttendanceStatus() != null ? a.getAttendanceStatus().name() : null;
        if (a.getCheckInTime() != null && a.getCheckOutTime() == null && a.getDate().isBefore(LocalDate.now(VIETNAM_ZONE))) {
            status = Attendance.AttendanceStatus.MISSING_CHECKOUT.name();
        }
        dto.setAttendanceStatus(status);
        dto.setNotes(a.getNotes());
        return dto;
    }

    private AttendanceSettings getOrCreateSettings(Team team) {
        return settingsRepo.findByTeamId(team.getId())
                .orElseGet(() -> settingsRepo.save(defaultSettings(team)));
    }

    private AttendanceSettings defaultSettings(Team team) {
        AttendanceSettings settings = new AttendanceSettings();
        settings.setTeam(team);
        settings.setWorkStartTime(AttendanceSettings.DEFAULT_START_TIME);
        settings.setWorkEndTime(AttendanceSettings.DEFAULT_END_TIME);
        settings.setStandardHours(AttendanceSettings.DEFAULT_STANDARD_HOURS);
        settings.setHourlyRateVnd(AttendanceSettings.DEFAULT_HOURLY_RATE_VND);
        settings.setOvertimeMultiplier(AttendanceSettings.DEFAULT_OVERTIME_MULTIPLIER);
        return settings;
    }

    private AttendanceSettingsDTO toSettingsDTO(AttendanceSettings settings) {
        AttendanceSettingsDTO dto = new AttendanceSettingsDTO();
        dto.setWorkStartTime(settings.getWorkStartTime());
        dto.setWorkEndTime(settings.getWorkEndTime());
        dto.setStandardHours(settings.getStandardHours());
        dto.setHourlyRateVnd(settings.getHourlyRateVnd());
        dto.setOvertimeMultiplier(settings.getOvertimeMultiplier());
        return dto;
    }

    private void validateSettings(AttendanceSettingsDTO request) {
        if (request == null || request.getWorkStartTime() == null || request.getWorkEndTime() == null
                || request.getStandardHours() == null || request.getHourlyRateVnd() == null
                || request.getOvertimeMultiplier() == null) {
            throw new RuntimeException("Cần nhập đầy đủ giờ làm, đơn giá và hệ số tăng ca");
        }
        if (!request.getWorkEndTime().isAfter(request.getWorkStartTime())) {
            throw new RuntimeException("Giờ tan ca phải sau giờ vào ca");
        }
        if (request.getStandardHours().compareTo(new BigDecimal("0.25")) < 0
                || request.getStandardHours().compareTo(new BigDecimal("24.00")) > 0) {
            throw new RuntimeException("Giờ làm chuẩn phải từ 0,25 đến 24 giờ");
        }
        long configuredWindowMinutes = java.time.Duration.between(
                request.getWorkStartTime(), request.getWorkEndTime()).toMinutes();
        if (request.getStandardHours().multiply(BigDecimal.valueOf(60))
                .compareTo(BigDecimal.valueOf(configuredWindowMinutes)) > 0) {
            throw new RuntimeException("Giờ làm chuẩn không được dài hơn khoảng giờ vào đến giờ tan ca");
        }
        if (request.getHourlyRateVnd() < 1_000L || request.getHourlyRateVnd() > 10_000_000L) {
            throw new RuntimeException("Đơn giá phải từ 1.000đ đến 10.000.000đ mỗi giờ");
        }
        if (request.getOvertimeMultiplier().compareTo(BigDecimal.ONE) < 0
                || request.getOvertimeMultiplier().compareTo(new BigDecimal("3.00")) > 0) {
            throw new RuntimeException("Hệ số tăng ca phải từ 1,00 đến 3,00");
        }
    }

    private LocalTime parseTime(String value, LocalTime fallback) {
        try {
            return value == null ? fallback : LocalTime.parse(value);
        } catch (RuntimeException ignored) {
            return fallback;
        }
    }
}
