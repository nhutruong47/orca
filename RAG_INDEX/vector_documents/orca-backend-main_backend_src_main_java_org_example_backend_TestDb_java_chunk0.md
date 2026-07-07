# Knowledge Document: TestDb.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/TestDb.java",
  "language": "java",
  "module": "backend",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in backend.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
package org.example.backend;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class TestDb {
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection("jdbc:postgresql://127.0.0.1:5432/postgres", "postgres", "123456");
             Statement stmt = conn.createStatement()) {
            stmt.executeUpdate("CREATE DATABASE orca_db;");
            System.out.println("Database created successfully!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```
