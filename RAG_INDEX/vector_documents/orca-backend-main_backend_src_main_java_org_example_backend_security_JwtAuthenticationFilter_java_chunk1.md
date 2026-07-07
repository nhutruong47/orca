# Knowledge Document: JwtAuthenticationFilter.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/security/JwtAuthenticationFilter.java",
  "language": "java",
  "module": "security",
  "business_domain": "admin",
  "tags": [
    "admin",
    "factory",
    "authentication",
    "security",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in security.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, factory, authentication, security, authorization

## Source Code Chunk
```java
oken(jwt, userDetails)) {
                    UsernamePasswordAuthenticationToken authToken = new UsernamePasswordAuthenticationToken(
                            userDetails, null, userDetails.getAuthorities());
                    authToken.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                    SecurityContextHolder.getContext().setAuthentication(authToken);
                }
            }
        } catch (Exception e) {
            // Token không hợp lệ — bỏ qua và tiếp tục filter chain
            logger.error("Không thể xác thực JWT: " + e.getMessage());
        }

        filterChain.doFilter(request, response);
    }
}

```
