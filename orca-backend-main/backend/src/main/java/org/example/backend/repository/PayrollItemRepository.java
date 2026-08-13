package org.example.backend.repository;

import org.example.backend.entity.PayrollItem;
import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface PayrollItemRepository extends JpaRepository<PayrollItem, UUID> {
    @EntityGraph(attributePaths = {"user"})
    List<PayrollItem> findByPayrollRunId(UUID payrollRunId);
    Optional<PayrollItem> findByPayrollRunIdAndUserId(UUID payrollRunId, UUID userId);
}
