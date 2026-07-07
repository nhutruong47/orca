# Knowledge Document: VersionFixRunner.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/config/VersionFixRunner.java",
  "language": "java",
  "module": "config",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in config.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend.config;

import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import org.springframework.jdbc.core.JdbcTemplate;

@Component
public class VersionFixRunner implements CommandLineRunner {
    private final JdbcTemplate jdbcTemplate;

    public VersionFixRunner(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Override
    public void run(String... args) {
        try {
            jdbcTemplate.execute("UPDATE teams SET version = 0 WHERE version IS NULL");
            System.out.println("Ran version fix runner for teams.");
        } catch (Exception e) {
            System.err.println("Failed to fix versions: " + e.getMessage());
        }
    }
}

```
