# Knowledge Document: AiPlanRequest.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/ai/AiPlanRequest.java",
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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AiPlanRequest {
    private String teamId;
    private String intent;
    private Map<String, Object> fields = new HashMap<>();
    private List<AiTeamMemberContext> members = new ArrayList<>();

    public String getTeamId() {
        return teamId;
    }

    public void setTeamId(String teamId) {
        this.teamId = teamId;
    }

    public String getIntent() {
        return intent;
    }

    public void setIntent(String intent) {
        this.intent = intent;
    }

    public Map<String, Object> getFields() {
        return fields;
    }

    public void setFields(Map<String, Object> fields) {
        this.fields = fields;
    }

    public List<AiTeamMemberContext> getMembers() {
        return members;
    }

    public void setMembers(List<AiTeamMemberContext> members) {
        this.members = members;
    }
}

```
