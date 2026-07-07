# Knowledge Document: OAuth2LoginSuccessHandler.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/security/OAuth2LoginSuccessHandler.java",
  "language": "java",
  "module": "security",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in security.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
il);
                                        return userRepository.save(newUser);
                                });

                String token = jwtUtil.generateToken(user);
                String redirectUrl = frontendUrl + "/oauth2/callback?token=" + token
                                + "&username=" + user.getUsername()
                                + "&role=" + user.getRole().name();
                getRedirectStrategy().sendRedirect(request, response, redirectUrl);
        }
}

```
