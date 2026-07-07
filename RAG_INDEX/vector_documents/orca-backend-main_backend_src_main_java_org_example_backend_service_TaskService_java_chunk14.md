# Knowledge Document: TaskService.java (Chunk 15/15)

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
  "chunk_index": 14,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
le salary = (s.getRegularHours() > 0 ? s.getRegularHours() : s.getTotalWorkload()) * s.getHourlyRate()
                        + (s.getOvertimeHours() * s.getOvertimeRate());
                totalSalary += salary;
                row.createCell(7).setCellValue(salary);
            }
            Row totalRow = sheet.createRow(report.size() + 1);
            totalRow.createCell(0).setCellValue("");
            totalRow.createCell(1).setCellValue("TONG");
            totalRow.createCell(7).setCellValue(totalSalary);
            for (int i = 0; i < headers.length; i++) {
                sheet.autoSizeColumn(i);
            }
            wb.write(out);
            return out.toByteArray();
        }
    }

    public Map<String, Object> payoutSalary(UUID teamId, UUID actorId) {
        List<SalaryDTO> report = getSalaryReport(teamId);
        double totalSalary = report.stream()
                .mapToDouble(s -> {
                    // Use attendance hours if available, fallback to task workload (same as getSalaryReport)
                    double billableRegular = s.getRegularHours() > 0 ? s.getRegularHours() : s.getTotalWorkload();
                    double overtimeHours = s.getOvertimeHours() > 0 ? s.getOvertimeHours() : 0;
                    return (billableRegular * s.getHourlyRate())
                            + (overtimeHours * s.getOvertimeRate());
                })
                .sum();
        if (totalSalary <= 0) {
            throw new RuntimeException("Khong co luong de phat cho nhom nay.");
        }
        User actor = userRepo.findById(actorId).orElseThrow(() -> new RuntimeException("User not found"));
        String description = "Phat luong thang cho " + report.size() + " nhan vien. Tong quy: "
                + String.format("%,.0f", totalSalary) + " VND.";
        notificationService.createAndSend(
                actor,
                "Phat luong thanh cong",
                description,
                "SALARY_PAYOUT",
                null);
        return Map.of(
                "message", "Phat luong thanh cong",
                "totalEmployees", report.size(),
                "totalSalary", totalSalary,
                "currency", "VND");
    }
}

```
