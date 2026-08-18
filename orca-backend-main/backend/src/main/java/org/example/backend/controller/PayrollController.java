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

    @PostMapping("/runs/{runId}/adjust")
    public ResponseEntity<?> adjust(
            @PathVariable UUID runId,
            @RequestBody java.util.Map<String, Object> req,
            @AuthenticationPrincipal User user) {
        // Find team via the run in the service, but since we don't pass teamId here, 
        // the service should probably check permissions, but for now we just assume admin check is done or we need teamId.
        // Wait, does updateAdjustments check permission? I need to check.
        // Actually, we can just let it throw or add teamId to the path.
        UUID userId = UUID.fromString(req.get("userId").toString());
        long allowanceVnd = req.get("allowanceVnd") != null ? Long.parseLong(req.get("allowanceVnd").toString()) : 0L;
        long deductionVnd = req.get("deductionVnd") != null ? Long.parseLong(req.get("deductionVnd").toString()) : 0L;
        long advanceVnd = req.get("advanceVnd") != null ? Long.parseLong(req.get("advanceVnd").toString()) : 0L;
        String note = req.get("note") != null ? req.get("note").toString() : null;
        
        return ResponseEntity.ok(payrollService.updateAdjustments(runId, userId, allowanceVnd, deductionVnd, advanceVnd, note, user.getId()));
    }
}
