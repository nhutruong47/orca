# Knowledge Document: PayosConfig.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/config/PayosConfig.java",
  "language": "java",
  "module": "config",
  "business_domain": "factory",
  "tags": [
    "factory"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in config.
- **Dependencies**: Refer to module imports.
- **Tags**: factory

## Source Code Chunk
```java
package org.example.backend.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import vn.payos.PayOS;

@Configuration
public class PayosConfig {

    @Value("${payos.client-id:test}")
    private String clientId;

    @Value("${payos.api-key:test}")
    private String apiKey;

    @Value("${payos.checksum-key:test}")
    private String checksumKey;

    @Bean
    public PayOS payOS() {
        return new PayOS(clientId, apiKey, checksumKey);
    }
}

```
