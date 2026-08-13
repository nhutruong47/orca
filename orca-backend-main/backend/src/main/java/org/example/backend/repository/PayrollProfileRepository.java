package org.example.backend.repository;

import org.example.backend.entity.PayrollProfile;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface PayrollProfileRepository extends JpaRepository<PayrollProfile, UUID> {
    Optional<PayrollProfile> findByTeamIdAndUserId(UUID teamId, UUID userId);
    List<PayrollProfile> findByTeamId(UUID teamId);
}
