# Knowledge Document: AiReviseRequest.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ai/AiReviseRequest.java",
  "language": "java",
  "module": "ai",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in ai.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.dto.ai;

import java.util.ArrayList;
import java.util.List;

public class AiReviseRequest {
    private String teamId;
    private String instruction;
    private AiPlanDraftResponse draft;
    private List<AiTeamMemberContext> members = new ArrayList<>();

    public String getTeamId() {
        return teamId;
    }

    public void setTeamId(String teamId) {
        this.teamId = teamId;
    }

    public String getInstruction() {
        return instruction;
    }

    public void setInstruction(String instruction) {
        this.instruction = instruction;
    }

    public AiPlanDraftResponse getDraft() {
        return draft;
    }

    public void setDraft(AiPlanDraftResponse draft) {
        this.draft = draft;
    }

    public List<AiTeamMemberContext> getMembers() {
        return members;
    }

    public void setMembers(List<AiTeamMemberContext> members) {
        this.members = members;
    }
}

```
