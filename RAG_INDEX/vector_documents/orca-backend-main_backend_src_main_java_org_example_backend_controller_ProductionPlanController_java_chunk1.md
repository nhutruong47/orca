# Knowledge Document: ProductionPlanController.java (Chunk 2/3)

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
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: production, authentication, security

## Source Code Chunk
```java
ers/{orderId}")
    public ResponseEntity<?> getPlansByOrder(
            @PathVariable UUID orderId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireProductionOrderAccess(currentUser, orderId);
        return ResponseEntity.ok(planService.getPlansByOrder(orderId));
    }

    @PatchMapping("/{planId}/approve")
    public ResponseEntity<?> approvePlan(
            @PathVariable UUID planId,
            @AuthenticationPrincipal User currentUser,
            @RequestBody(required = false) Map<String, String> body) {
        accessControlService.requireProductionPlanAccess(currentUser, planId);
        try {
            UUID approvedBy = null;
            if (body != null && body.get("approvedBy") != null) {
                approvedBy = UUID.fromString(body.get("approvedBy"));
            }
            return ResponseEntity.ok(planService.approvePlan(planId, approvedBy));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{planId}/daily-targets")
    public ResponseEntity<?> getDailyTargets(
            @PathVariable UUID planId,
            @AuthenticationPrincipal User currentUser) {
        accessControlService.requireProductionPlanAccess(currentUser, planId);
        return ResponseEntity.ok(planService.getDailyTargetsByPlan(planId));
    }

    @PatchMapping("/daily-targets/{targetId}")
    public ResponseEntity<?> updateDailyActual(
            @PathVariable UUID targetId,
            @AuthenticationPrincipal User currentUser,
            @RequestBody Map<String, Object> body) {
        accessControlService.requireDailyTargetAccess(currentUser, targetId);
        try {
            Double actualRoastKg = getDouble(body, "actualRoastKg");
            Double actualQcKg = getDouble(body, "actualQcKg");
            Double actualQcFailKg = getDouble(body, "actualQcFailKg");
            Double actualPackagedKg = getDouble(body, "actualPackagedKg");
            Integer actualPackages = getInt(body, "actualPackages");
            String notes = getString(body, "notes");
            String issues = getString(body, "issues");

            DailyTargetDTO updated = planService.updateDailyActual(
                    targetId, actualRoastKg, actualQcKg, actualQcFailKg,

```
