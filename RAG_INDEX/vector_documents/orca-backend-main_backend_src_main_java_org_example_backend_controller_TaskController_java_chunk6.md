# Knowledge Document: TaskController.java (Chunk 7/7)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/TaskController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "report",
  "tags": [
    "report",
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 6,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: report, factory, authentication, security

## Source Code Chunk
```java
rt(teamId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/salary/{teamId}/export-excel")
    public ResponseEntity<byte[]> exportSalaryExcel(@PathVariable UUID teamId, @AuthenticationPrincipal User user) throws Exception {
        accessControlService.requireTeamMember(user, teamId);
        byte[] excelBytes = taskService.exportSalaryExcel(teamId);
        String filename = "bang-luong-" + teamId + ".xlsx";
        return ResponseEntity.ok()
            .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + filename + "\"")
            .contentType(MediaType.parseMediaType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))
            .body(excelBytes);
    }

    @PostMapping("/salary/{teamId}/payout")
    public ResponseEntity<?> payoutSalary(@PathVariable UUID teamId,
            @AuthenticationPrincipal User user) {
        return ResponseEntity.ok(taskService.payoutSalary(teamId, user.getId()));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> delete(@PathVariable UUID id, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTaskAccess(user, id);
            taskService.delete(id);
            return ResponseEntity.ok(Map.of("message", "Đã xóa task"));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }
}

```
