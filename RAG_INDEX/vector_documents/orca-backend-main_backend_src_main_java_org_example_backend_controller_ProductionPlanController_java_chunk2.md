# Knowledge Document: ProductionPlanController.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ProductionPlanController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "production",
  "tags": [
    "production",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, authentication, security

## Source Code Chunk
```java
Kg");
            Double actualPackagedKg = getDouble(body, "actualPackagedKg");
            Integer actualPackages = getInt(body, "actualPackages");
            String notes = getString(body, "notes");
            String issues = getString(body, "issues");

            DailyTargetDTO updated = planService.updateDailyActual(
                    targetId, actualRoastKg, actualQcKg, actualQcFailKg,
                    actualPackagedKg, actualPackages, notes, issues);
            return ResponseEntity.ok(updated);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/today/{teamId}")
    public ResponseEntity<?> getTodayTarget(
            @PathVariable UUID teamId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireTeamMember(currentUser, teamId);
        DailyTargetDTO target = planService.getTodayTarget(teamId);
        if (target != null) {
            return ResponseEntity.ok(target);
        }
        return ResponseEntity.noContent().build();
    }

    private String getString(Map<String, Object> body, String key) {
        Object v = body.get(key);
        return v != null ? v.toString() : null;
    }

    private Double getDouble(Map<String, Object> body, String key) {
        Object v = body.get(key);
        if (v == null) return null;
        if (v instanceof Number) return ((Number) v).doubleValue();
        try { return Double.parseDouble(v.toString()); } catch (Exception e) { return null; }
    }

    private Integer getInt(Map<String, Object> body, String key) {
        Object v = body.get(key);
        if (v == null) return null;
        if (v instanceof Number) return ((Number) v).intValue();
        try { return Integer.parseInt(v.toString()); } catch (Exception e) { return null; }
    }
}

```
