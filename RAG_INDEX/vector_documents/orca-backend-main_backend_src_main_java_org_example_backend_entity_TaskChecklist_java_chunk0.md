# Knowledge Document: TaskChecklist.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/TaskChecklist.java",
  "language": "java",
  "module": "entity",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.entity;

import jakarta.persistence.*;
import java.util.UUID;

@Entity
@Table(name = "task_checklists")
public class TaskChecklist {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(updatable = false, nullable = false)
    private UUID id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "task_id", nullable = false)
    private Task task;

    @Column(nullable = false, length = 500)
    private String content;

    @Column(nullable = false)
    private Boolean checked = false;

    @Column(name = "sort_order")
    private Integer sortOrder = 0;

    public TaskChecklist() {
    }

    // === Getters & Setters ===
    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public Task getTask() {
        return task;
    }

    public void setTask(Task task) {
        this.task = task;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public Boolean getChecked() {
        return checked;
    }

    public void setChecked(Boolean checked) {
        this.checked = checked;
    }

    public Integer getSortOrder() {
        return sortOrder;
    }

    public void setSortOrder(Integer sortOrder) {
        this.sortOrder = sortOrder;
    }
}

```
