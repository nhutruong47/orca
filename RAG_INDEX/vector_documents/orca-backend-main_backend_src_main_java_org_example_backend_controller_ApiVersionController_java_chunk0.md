# Knowledge Document: ApiVersionController.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/ApiVersionController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Controller",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/api/version")
public class ApiVersionController {

    @GetMapping
    public ResponseEntity<Map<String, String>> getVersion() {
        return ResponseEntity.ok(Map.of(
                "version", "v1",
                "status", "stable",
                "timestamp", java.time.Instant.now().toString()
        ));
    }
}

```
