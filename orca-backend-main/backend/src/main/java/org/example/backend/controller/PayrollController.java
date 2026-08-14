package org.example.backend.controller;

import org.example.backend.entity.User;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.PayrollService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

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
}
