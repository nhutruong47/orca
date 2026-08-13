package org.example.backend.repository;

import org.example.backend.entity.PayrollRun;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;
import java.util.UUID;

public interface PayrollRunRepository extends JpaRepository<PayrollRun, UUID> {
    Optional<PayrollRun> findByTeamIdAndYearAndMonth(UUID teamId, Integer year, Integer month);
}
