package org.example.backend.repository;

import org.example.backend.entity.PayrollAuditLog;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.UUID;

public interface PayrollAuditLogRepository extends JpaRepository<PayrollAuditLog, UUID> {
}
