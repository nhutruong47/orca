# Knowledge Document: TeamMemberRepository.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/repository/TeamMemberRepository.java",
  "language": "java",
  "module": "repository",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Repository",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Repository in repository.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.repository;

import org.example.backend.entity.TeamMember;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface TeamMemberRepository extends JpaRepository<TeamMember, UUID> {
    List<TeamMember> findByTeamId(UUID teamId);

    List<TeamMember> findByUserId(UUID userId);

    Optional<TeamMember> findByTeamIdAndUserId(UUID teamId, UUID userId);

    boolean existsByTeamIdAndUserId(UUID teamId, UUID userId);

    void deleteByTeamIdAndUserId(UUID teamId, UUID userId);
}

```
