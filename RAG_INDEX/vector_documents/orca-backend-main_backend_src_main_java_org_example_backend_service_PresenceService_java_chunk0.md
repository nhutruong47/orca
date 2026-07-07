# Knowledge Document: PresenceService.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/PresenceService.java",
  "language": "java",
  "module": "service",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Service",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.service;

import org.springframework.stereotype.Service;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class PresenceService {

    // userId -> set of session IDs
    private final Map<String, Set<String>> onlineUsers = new ConcurrentHashMap<>();

    public void userConnected(String userId, String sessionId) {
        onlineUsers.computeIfAbsent(userId, k -> ConcurrentHashMap.newKeySet()).add(sessionId);
    }

    public void userDisconnected(String sessionId) {
        onlineUsers.forEach((userId, sessions) -> {
            sessions.remove(sessionId);
            if (sessions.isEmpty()) {
                onlineUsers.remove(userId);
            }
        });
    }

    public Set<String> getOnlineUserIds() {
        return Collections.unmodifiableSet(onlineUsers.keySet());
    }

    public boolean isOnline(String userId) {
        Set<String> sessions = onlineUsers.get(userId);
        return sessions != null && !sessions.isEmpty();
    }
}

```
