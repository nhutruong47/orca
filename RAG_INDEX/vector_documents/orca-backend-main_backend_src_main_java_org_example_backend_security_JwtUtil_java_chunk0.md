# Knowledge Document: JwtUtil.java (Chunk 1/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/security/JwtUtil.java",
  "language": "java",
  "module": "security",
  "business_domain": "factory",
  "tags": [
    "factory",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in security.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, security

## Source Code Chunk
```java
package org.example.backend.security;

import io.jsonwebtoken.*;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

@Component
public class JwtUtil {

    @Value("${app.jwt.secret}")
    private String secret;

    @Value("${app.jwt.expiration}")
    private long expiration;

    /**
     * Tạo JWT token cho user
     */
    public String generateToken(UserDetails userDetails) {
        Map<String, Object> claims = new HashMap<>();
        // Thêm role vào claims
        claims.put("role", userDetails.getAuthorities().iterator().next().getAuthority());
        return createToken(claims, userDetails.getUsername());
    }

    private String createToken(Map<String, Object> claims, String subject) {
        return Jwts.builder()
                .claims(claims)
                .subject(subject)
                .issuedAt(new Date(System.currentTimeMillis()))
                .expiration(new Date(System.currentTimeMillis() + expiration))
                .signWith(getSigningKey())
                .compact();
    }

    /**
     * Tạo JWT token cho lời mời vào nhóm (expiration 7 ngày)
     */
    public String generateInviteToken(String email, java.util.UUID teamId, String groupRole) {
        Map<String, Object> claims = new HashMap<>();
        claims.put("teamId", teamId.toString());
        claims.put("groupRole", groupRole);
        return Jwts.builder()
                .claims(claims)
                .subject(email)
                .issuedAt(new Date(System.currentTimeMillis()))
                .expiration(new Date(System.currentTimeMillis() + 7L * 24 * 60 * 60 * 1000)) // 7 days
                .signWith(getSigningKey())
                .compact();
    }

    /**
     * Parse token lời mời và trả về claims
     */
    public Claims parseInviteToken(String token) {
        return extractAllClaims(token);
    }

    /**
     * Lấy username từ token
     */
    public String extractUsername(String token) {
        return extractClaim(token, Claims::getSubject);
    }

    /**
     * Lấy ngày hết hạn từ token
     */

```
