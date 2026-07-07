# Knowledge Document: User.java (Chunk 1/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/User.java",
  "language": "java",
  "module": "entity",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.time.LocalDateTime;
import java.util.Collection;
import java.util.List;
import java.util.UUID;

@Entity
@Table(name = "users")
public class User implements UserDetails {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @Column(unique = true, nullable = false)
    private String username;

    @Column(nullable = false)
    private String password;

    @Column(name = "full_name")
    private String fullName;

    private String email;

    private String avatar;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private Role role = Role.MEMBER;

    @Column(name = "chip_id", unique = true)
    private String chipId;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "ai_trial_start_date")
    private LocalDateTime aiTrialStartDate;

    @Column(name = "ai_plan")
    private String aiPlan = "free";

    @Column(name = "ai_plan_expires_at")
    private LocalDateTime aiPlanExpiresAt;

    @Column(name = "ai_usage_count")
    private Integer aiUsageCount = 0;

    @Column(name = "locked", nullable = false, columnDefinition = "boolean default false")
    private boolean locked = false;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
        if (this.aiTrialStartDate == null) {
            this.aiTrialStartDate = this.createdAt;
        }
    }

    public boolean isAiTrialActive() {
        int usage = aiUsageCount != null ? aiUsageCount : 0;
        if ("enterprise".equalsIgnoreCase(aiPlan)) {
            return aiPlanExpiresAt != null && LocalDateTime.now().isBefore(aiPlanExpiresAt);
        } else if ("professional".equalsIgnoreCase(aiPlan) || "plus".equalsIgnoreCase(aiPlan)) {
            return usage < 100;
        } else {
            return usage < 10;
        }
    }

    public long getAiTrialDaysRemaining() {
        if ("enterprise".equalsIgnoreCase(aiPlan) && aiPlanExpiresAt != null) {

```
