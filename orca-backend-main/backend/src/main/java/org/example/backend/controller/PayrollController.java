package org.example.backend.controller;

import jakarta.validation.Valid;
import jakarta.validation.constraints.DecimalMax;
import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.PayrollService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.time.YearMonth;
import java.util.UUID;

@RestController
@RequestMapping("/api/payroll")
public class PayrollController {
    private final PayrollService payrollService;
    private final AccessControlService accessControlService;

    public PayrollController(PayrollService payrollService, AccessControlService accessControlService) {
        this.payrollService = payrollService;
        this.accessControlService = accessControlService;
    }

    @GetMapping("/teams/{teamId}")
    public ResponseEntity<?> getReport(@PathVariable UUID teamId,
                                       @RequestParam(required = false) Integer year,
                                       @RequestParam(required = false) Integer month,
                                       @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, teamId);
        return ResponseEntity.ok(payrollService.getReport(teamId, year, month));
    }

    @GetMapping("/teams/{teamId}/my-payslip")
    public ResponseEntity<?> getMyPayslip(@PathVariable UUID teamId,
                                          @RequestParam(required = false) Integer year,
                                          @RequestParam(required = false) Integer month,
                                          @AuthenticationPrincipal User user) {
        accessControlService.requireTeamMember(user, teamId);
        return ResponseEntity.ok(payrollService.getMyPayslip(teamId, user.getId(), year, month));
    }

    @PutMapping("/teams/{teamId}/profiles/{userId}")
    public ResponseEntity<?> updateProfile(@PathVariable UUID teamId, @PathVariable UUID userId,
                                           @RequestParam(required = false) Integer year,
                                           @RequestParam(required = false) Integer month,
                                           @Valid @RequestBody PayProfileRequest request,
                                           @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, teamId);
        return ResponseEntity.ok(payrollService.updateProfile(teamId, userId, request.hourlyRateVnd,
                request.overtimeMultiplier, user.getId(), year, month));
    }

    @PatchMapping("/runs/{runId}/items/{userId}")
    public ResponseEntity<?> updateAdjustments(@PathVariable UUID runId, @PathVariable UUID userId,
                                               @Valid @RequestBody AdjustmentRequest request,
                                               @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, payrollService.getRunTeamId(runId));
        return ResponseEntity.ok(payrollService.updateAdjustments(runId, userId, request.allowanceVnd,
                request.deductionVnd, request.advanceVnd, request.note, user.getId()));
    }

    @PostMapping("/runs/{runId}/recalculate")
    public ResponseEntity<?> recalculate(@PathVariable UUID runId, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, payrollService.getRunTeamId(runId));
        return ResponseEntity.ok(payrollService.recalculate(runId, user.getId()));
    }

    @PostMapping("/runs/{runId}/finalize")
    public ResponseEntity<?> finalizeRun(@PathVariable UUID runId, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, payrollService.getRunTeamId(runId));
        return ResponseEntity.ok(payrollService.finalizeRun(runId, user.getId()));
    }

    @PostMapping("/runs/{runId}/approve")
    public ResponseEntity<?> approve(@PathVariable UUID runId, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, payrollService.getRunTeamId(runId));
        return ResponseEntity.ok(payrollService.finalizeRun(runId, user.getId()));
    }

    @PostMapping("/runs/{runId}/reopen")
    public ResponseEntity<?> reopen(@PathVariable UUID runId, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, payrollService.getRunTeamId(runId));
        return ResponseEntity.ok(payrollService.reopen(runId, user.getId()));
    }

    @PostMapping("/runs/{runId}/mark-paid")
    public ResponseEntity<?> markPaid(@PathVariable UUID runId, @AuthenticationPrincipal User user) {
        accessControlService.requireTeamAdmin(user, payrollService.getRunTeamId(runId));
        return ResponseEntity.ok(payrollService.markPaid(runId, user.getId()));
    }

    @GetMapping("/teams/{teamId}/export-excel")
    public ResponseEntity<byte[]> export(@PathVariable UUID teamId,
                                         @RequestParam(required = false) Integer year,
                                         @RequestParam(required = false) Integer month,
                                         @AuthenticationPrincipal User user) throws Exception {
        accessControlService.requireTeamAdmin(user, teamId);
        byte[] bytes = payrollService.exportExcel(teamId, year, month);
        YearMonth selected = year != null && month != null ? YearMonth.of(year, month) : YearMonth.now();
        String period = String.format("%04d-%02d", selected.getYear(), selected.getMonthValue());
        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=bang-luong-" + period + ".xlsx")
                .contentType(MediaType.parseMediaType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))
                .body(bytes);
    }

    public static class PayProfileRequest {
        @Min(1_000) @Max(10_000_000)
        public long hourlyRateVnd;
        @DecimalMin("1.00") @DecimalMax("3.00")
        public BigDecimal overtimeMultiplier = new BigDecimal("1.50");
    }

    public static class AdjustmentRequest {
        @Min(0) @Max(1_000_000_000) public long allowanceVnd;
        @Min(0) @Max(1_000_000_000) public long deductionVnd;
        @Min(0) @Max(1_000_000_000) public long advanceVnd;
        public String note;
    }
}
