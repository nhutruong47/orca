# Knowledge Document: TestPayos.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/TestPayos.java",
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

import vn.payos.PayOS;
import java.lang.reflect.Method;

public class TestPayos {
    public static void main(String[] args) {
        for (Method m : PayOS.class.getMethods()) {
            if (m.getName().toLowerCase().contains("webhook")) {
                Class<?> retType = m.getReturnType();
                for (Method m2 : retType.getMethods()) {
                    if (m2.getName().equals("verify")) {
                        System.out.println("Return type: " + m2.getReturnType().getName());
                    }
                }
            }
        }
    }
}

```
