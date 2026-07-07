# Knowledge Document: ApiVersioningFilter.java (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/config/ApiVersioningFilter.java",
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

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.time.Instant;

@Component
@Order(Ordered.LOWEST_PRECEDENCE)
public class ApiVersioningFilter implements jakarta.servlet.Filter {

    private static final String API_VERSION = "v1";

    @Override
    public void doFilter(jakarta.servlet.ServletRequest request, jakarta.servlet.ServletResponse response,
                         FilterChain chain) throws IOException, ServletException {
        HttpServletResponse res = (HttpServletResponse) response;
        res.setHeader("X-API-Version", API_VERSION);
        res.setHeader("X-Timestamp", Instant.now().toString());
        chain.doFilter(request, response);
    }
}

```
