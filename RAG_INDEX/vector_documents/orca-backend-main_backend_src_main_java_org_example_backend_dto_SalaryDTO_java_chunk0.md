# Knowledge Document: SalaryDTO.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/SalaryDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "DTO",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.dto;

public class SalaryDTO {
    private String memberId;
    private String memberName;
    private int totalTasks;
    private int completedTasks;
    private double totalWorkload;
    private double totalActualWorkload;
    private double hourlyRate;
    private double estimatedSalary;

    private double regularHours;
    private double overtimeHours;
    private double overtimeRate;

    // === Getters & Setters ===
    public String getMemberId() { return memberId; }
    public void setMemberId(String memberId) { this.memberId = memberId; }

    public String getMemberName() { return memberName; }
    public void setMemberName(String memberName) { this.memberName = memberName; }

    public int getTotalTasks() { return totalTasks; }
    public void setTotalTasks(int totalTasks) { this.totalTasks = totalTasks; }

    public int getCompletedTasks() { return completedTasks; }
    public void setCompletedTasks(int completedTasks) { this.completedTasks = completedTasks; }

    public double getTotalWorkload() { return totalWorkload; }
    public void setTotalWorkload(double totalWorkload) { this.totalWorkload = totalWorkload; }

    public double getTotalActualWorkload() { return totalActualWorkload; }
    public void setTotalActualWorkload(double totalActualWorkload) { this.totalActualWorkload = totalActualWorkload; }

    public double getHourlyRate() { return hourlyRate; }
    public void setHourlyRate(double hourlyRate) { this.hourlyRate = hourlyRate; }
    
    public double getRegularHours() { return regularHours; }
    public void setRegularHours(double regularHours) { this.regularHours = regularHours; }

    public double getOvertimeHours() { return overtimeHours; }
    public void setOvertimeHours(double overtimeHours) { this.overtimeHours = overtimeHours; }

    public double getOvertimeRate() { return overtimeRate; }
    public void setOvertimeRate(double overtimeRate) { this.overtimeRate = overtimeRate; }

    public double getEstimatedSalary() { return estimatedSalary; }
    public void setEstimatedSalary(double estimatedSalary) { this.estimatedSalary = estimatedSalary; }
}

```
