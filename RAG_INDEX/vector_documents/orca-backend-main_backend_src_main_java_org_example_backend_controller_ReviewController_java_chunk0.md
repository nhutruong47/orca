# Knowledge Document: ReviewController.java (Chunk 1/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ReviewController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
package org.example.backend.controller;

import org.example.backend.dto.ReviewDTO;
import org.example.backend.entity.User;
import org.example.backend.repository.TeamRepository;
import org.example.backend.service.AccessControlService;
import org.example.backend.service.ReviewService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api/reviews")
public class ReviewController {

    @Autowired
    private ReviewService reviewService;

    @Autowired
    private TeamRepository teamRepo;

    @Autowired
    private AccessControlService accessControlService;

    @GetMapping("/team/{teamId}")
    public ResponseEntity<?> getReviewsByTeam(@PathVariable UUID teamId, @AuthenticationPrincipal User user) {
        try {
            accessControlService.requireTeamMember(user, teamId);
            return ResponseEntity.ok(reviewService.getReviewsByTeam(teamId));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    /**
     * Public summary used by the marketplace.
     * Authentication is required, but only basic — no team membership check,
     * since this is the publicly advertised trust score.
     */
    @GetMapping("/team/{teamId}/summary")
    public ResponseEntity<?> getTeamReviewSummary(@PathVariable UUID teamId) {
        var teamOpt = teamRepo.findById(teamId);
        if (teamOpt.isEmpty()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Team not found"));
        }
        var team = teamOpt.get();
        long reviewCount = reviewService.getReviewCount(teamId);
        double avgRating = team.getTotalRatings() > 0
                ? team.getSumRatings() / team.getTotalRatings()
                : 0.0;
        double onTimeRate = team.getTotalOrders() > 0
                ? (double) team.getOnTimeOrders() / team.getTotalOrders() * 100
                : 0.0;
        return ResponseEntity.ok(Map.of(
                "avgRating", Math.round(avgRating * 10.0) / 10.0,
                "reviewCount", reviewCount,

```
