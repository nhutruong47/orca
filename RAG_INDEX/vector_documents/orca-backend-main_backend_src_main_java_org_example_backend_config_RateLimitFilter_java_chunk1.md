# Knowledge Document: RateLimitFilter.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/config/RateLimitFilter.java",
  "language": "java",
  "module": "config",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in config.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```java
) {
            res.setStatus(429);
            res.setContentType("application/json");
            res.getWriter().write("{\"error\":\"Too many requests. Please try again later.\"}");
            return;
        }

        res.setHeader("X-RateLimit-Limit", String.valueOf(MAX_REQUESTS_PER_MINUTE));
        res.setHeader("X-RateLimit-Remaining", String.valueOf(MAX_REQUESTS_PER_MINUTE - current));
        res.setHeader("X-RateLimit-Reset", String.valueOf(bucket.windowStart + WINDOW_SECONDS));

        chain.doFilter(request, response);
    }

    private String getClientId(HttpServletRequest req) {
        String xf = req.getHeader("X-Forwarded-For");
        if (xf != null && !xf.isEmpty()) {
            return xf.split(",")[0].trim();
        }
        return req.getRemoteAddr();
    }

    private boolean isExcluded(String path) {
        return path.startsWith("/api/auth/login")
                || path.startsWith("/api/auth/register")
                || path.startsWith("/api/debug")
                || path.startsWith("/actuator")
                || path.startsWith("/ws");
    }
}

```
