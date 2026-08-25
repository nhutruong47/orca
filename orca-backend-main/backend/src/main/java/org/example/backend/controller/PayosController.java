package org.example.backend.controller;

import jakarta.servlet.http.HttpServletRequest;
import org.example.backend.entity.User;
import org.example.backend.service.PayosPaymentService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/payments/payos")
public class PayosController {

    private final PayosPaymentService payosPaymentService;

    @Value("${app.frontend.url:http://localhost:5173}")
    private String defaultFrontendUrl;

    public PayosController(PayosPaymentService payosPaymentService) {
        this.payosPaymentService = payosPaymentService;
    }

    @PostMapping("/create")
    public ResponseEntity<Map<String, Object>> createPaymentLink(
            @AuthenticationPrincipal User user,
            @RequestBody Map<String, String> body,
            HttpServletRequest request) {
        String planId = body.get("planId");
        String baseUrl = getBaseUrl(request, defaultFrontendUrl);
        return ResponseEntity.ok(payosPaymentService.createPaymentLink(user, planId, baseUrl));
    }

    @PostMapping("/webhook")
    public ResponseEntity<Map<String, Object>> handleWebhook(@RequestBody Map<String, Object> body) {
        // PayOS webhook verification should happen inside the service
        Map<String, Object> result = payosPaymentService.handleWebhook(body);
        return ResponseEntity.ok(result);
    }

    private String getBaseUrl(HttpServletRequest request, String defaultUrl) {
        String origin = request.getHeader("Origin");
        if (origin != null && !origin.isEmpty()) return origin;
        String referer = request.getHeader("Referer");
        if (referer != null && !referer.isEmpty()) {
            try {
                java.net.URL url = new java.net.URL(referer);
                return url.getProtocol() + "://" + url.getHost() + (url.getPort() != -1 ? ":" + url.getPort() : "");
            } catch (Exception e) {}
        }
        return defaultUrl;
    }
}
