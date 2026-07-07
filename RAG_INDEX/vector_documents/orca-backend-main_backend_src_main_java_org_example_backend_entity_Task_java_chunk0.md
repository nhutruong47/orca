# Knowledge Document: Task.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/Task.java",
  "language": "java",
  "module": "entity",
  "business_domain": "report",
  "tags": [
    "report",
    "production"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;
import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.Max;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "tasks")
public class Task {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "goal_id", nullable = false)
    @OnDelete(action = OnDeleteAction.CASCADE)
    private Goal goal;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "member_id")
    @OnDelete(action = OnDeleteAction.CASCADE)
    private User member;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "backup_member_id")
    @OnDelete(action = OnDeleteAction.CASCADE)
    private User backupMember;

    @Column(nullable = false, length = 500)
    private String title;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Min(1)
    @Max(5)
    private Integer priority = 1; // 1-5

    @Column(nullable = false)
    private String status = "PENDING"; // PENDING / IN_PROGRESS / COMPLETED

    /** WAITING / ACCEPTED / REJECTED */
    @Column(name = "acceptance_status", length = 20)
    private String acceptanceStatus = "WAITING";

    @Column(name = "hourly_rate")
    private Double hourlyRate; // đơn giá mỗi giờ/đơn vị công

    @Min(0)
    private Double workload; // estimated workload (hours or units)

    @Min(0)
    @Column(name = "actual_workload")
    private Double actualWorkload; // actual workload reported by member

    @Min(0)
    @Max(100)
    @Column(name = "completion_percentage")
    private Integer completionPercentage = 0; // 0-100

    @Min(0)
    @Column(name = "output_target")
    private Double outputTarget;

    @Min(0)
    @Column(name = "actual_output")
    private Double actualOutput;

    private LocalDateTime deadline;

    @Column(name = "production_stage")
    private String productionStage;

    @Column(name = "due_time")
    private LocalDateTime dueTime;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "supervisor_id")
    @OnDelete(action = OnDeleteAction.SET_NULL)
    private User supervisor;


```
