# Knowledge Document: TeamService.java (Chunk 1/9)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/TeamService.java",
  "language": "java",
  "module": "service",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security",
    "factory",
    "inventory",
    "employee"
  ],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 9
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.TeamDTO;
import org.example.backend.entity.*;
import org.example.backend.repository.TeamMemberRepository;
import org.example.backend.repository.TeamRepository;
import org.example.backend.repository.UserRepository;
import org.example.backend.repository.TaskRepository;
import org.example.backend.security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class TeamService {

    @Autowired
    private TeamRepository teamRepository;

    @Autowired
    private TeamMemberRepository teamMemberRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private TaskRepository taskRepository;

    @Autowired
    private EmailService emailService;

    @Autowired
    private JwtUtil jwtUtil;

    @Autowired
    private InventoryService inventoryService;

    /**
     * Lấy tất cả nhóm mà user tham gia
     */
    @Transactional(readOnly = true)
    public List<TeamDTO> getTeamsForUser(String username) {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new RuntimeException("User not found"));

        List<TeamMember> memberships = teamMemberRepository.findByUserId(user.getId());
        return memberships.stream()
                .map(tm -> toDTO(tm.getTeam(), false))
                .collect(Collectors.toList());
    }

    /**
     * Lấy tất cả nhóm trên hệ thống có đăng quảng cáo (cho Marketplace)
     */
    @Transactional(readOnly = true)
    public List<TeamDTO> getAllTeams() {
        return teamRepository.findAll().stream()
                .filter(Team::isPublished)
                .map(t -> toDTO(t, false))
                .collect(Collectors.toList());
    }

    /**
     * Xem chi tiết nhóm (bao gồm danh sách thành viên)
     */
    @Transactional(readOnly = true)
    public TeamDTO getTeamDetail(UUID teamId) {
        Team team = teamRepository.findById(teamId)
                .orElseThrow(() -> new RuntimeException("Team not found"));
        return toDTO(team, true);
    }

    /**
     * Tạo nhóm mới — user trở thành Owner
     */

```
