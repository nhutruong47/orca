# Knowledge Document: TaskService.java (Chunk 14/15)

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
  "chunk_index": 13,
  "total_chunks": 15
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: report, production, attendance, employee, notification

## Source Code Chunk
```java
rn m;
    }

    public List<Map<String, Object>> getDependencies(UUID taskId) {
        return dependencyRepo.findByTaskId(taskId).stream()
                .map(d -> {
                    Task dep = d.getDependsOnTask();
                    Map<String, Object> m = new LinkedHashMap<>();
                    m.put("id", d.getId().toString());
                    m.put("taskId", taskId.toString());
                    m.put("dependsOnTaskId", dep.getId().toString());
                    m.put("dependsOnTaskTitle", dep.getTitle());
                    m.put("dependencyType", d.getDependencyType());
                    return m;
                }).collect(Collectors.toList());
    }

    public byte[] exportSalaryExcel(UUID teamId) throws Exception {
        List<SalaryDTO> report = getSalaryReport(teamId);
        try (Workbook wb = new XSSFWorkbook(); ByteArrayOutputStream out = new ByteArrayOutputStream()) {
            Sheet sheet = wb.createSheet("Bang luong");
            String[] headers = {"STT", "Nhan vien", "Tong task", "Hoan thanh", "Gio thuong", "Gio tang ca",
                    "Don gia/gio (VND)", "Luong thuc nhan (VND)"};
            Row hRow = sheet.createRow(0);
            for (int i = 0; i < headers.length; i++) {
                hRow.createCell(i).setCellValue(headers[i]);
            }
            double totalSalary = 0;
            for (int i = 0; i < report.size(); i++) {
                SalaryDTO s = report.get(i);
                Row row = sheet.createRow(i + 1);
                row.createCell(0).setCellValue(i + 1);
                row.createCell(1).setCellValue(s.getMemberName());
                row.createCell(2).setCellValue(s.getTotalTasks());
                row.createCell(3).setCellValue(s.getCompletedTasks());
                row.createCell(4).setCellValue(s.getRegularHours());
                row.createCell(5).setCellValue(s.getOvertimeHours());
                row.createCell(6).setCellValue(s.getHourlyRate());
                double salary = (s.getRegularHours() > 0 ? s.getRegularHours() : s.getTotalWorkload()) * s.getHourlyRate()
                        + (s.getOvertimeHours() * s.getOvertimeRate());
                totalSalary += salary;
                row.createCell(7).setCellValue(salary);
            }
            Row totalRow = sheet.createRow(report.size() + 1);
            totalRow.createCell(0).setCellValue("");

```
