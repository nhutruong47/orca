# Knowledge Document: TaskService.java (Chunk 7/15)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/TaskService.java",
  "language": "java",
  "module": "service",
  "business_domain": "report",
  "tags": [
    "report",
    "production",
    "attendance",
    "employee",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 6,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
ream()
                .filter(t -> "COMPLETED".equals(t.getStatus()))
                .mapToDouble(t -> t.getActualWorkload() != null ? t.getActualWorkload() : (t.getWorkload() != null ? t.getWorkload() : 0))
                .sum();

            // Get attendance data for this member and team
            List<Attendance> attendances = attendanceRepo.findByUserIdAndTeamId(member.getId(), teamId);
            double totalRegularHours = attendances.stream().mapToDouble(a -> a.getRegularHours() != null ? a.getRegularHours() : 0.0).sum();
            double totalOvertimeHours = attendances.stream().mapToDouble(a -> a.getOvertimeHours() != null ? a.getOvertimeHours() : 0.0).sum();

            // Use hourly rate from tasks or default 50000 VND/hour
            double avgRate = teamTasks.stream()
                .filter(t -> t.getHourlyRate() != null)
                .mapToDouble(Task::getHourlyRate)
                .average().orElse(50000);
            
            // Overtime rate defaults to 1.5x of normal rate
            double defaultOvertimeRate = avgRate * 1.5;

            SalaryDTO dto = new SalaryDTO();
            dto.setMemberId(member.getId().toString());
            dto.setMemberName(member.getFullName() != null ? member.getFullName() : member.getUsername());
            dto.setTotalTasks(totalTasks);
            dto.setCompletedTasks(completed);
            dto.setTotalWorkload(totalWorkload);
            dto.setTotalActualWorkload(totalWorkload);
            
            dto.setRegularHours(totalRegularHours);
            dto.setOvertimeHours(totalOvertimeHours);
            dto.setHourlyRate(avgRate);
            dto.setOvertimeRate(defaultOvertimeRate);
            
            // Salary calculation based on Attendance, not Task Workload anymore
            // Fallback to totalWorkload if no attendance data exists (backward compatibility or testing)
            double billableRegular = totalRegularHours > 0 ? totalRegularHours : totalWorkload;
            dto.setEstimatedSalary((billableRegular * avgRate) + (totalOvertimeHours * defaultOvertimeRate));
            report.add(dto);
        }
        return report;
    }

    public void delete(UUID id) {
        Task t = taskRepo.findById(id).orElseThrow(() -> new RuntimeException("Task not found"));
        UUID goalId = t.getGoal() != null ? t.getGoal().getId() : null;

```
