# Knowledge Document: AuthService.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/AuthService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Service",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
enticate(
                new UsernamePasswordAuthenticationToken(request.getUsername(), request.getPassword()));
        User user = (User) authentication.getPrincipal();
        String token = jwtUtil.generateToken(user);
        return buildResponse(token, user);
    }

    public AuthResponse updateProfile(User user, UpdateProfileRequest request) {
        if (request.getFullName() != null) {
            user.setFullName(request.getFullName().trim());
        }
        if (request.getAvatar() != null) {
            user.setAvatar(request.getAvatar());
        }
        if (request.getEmail() != null) {
            user.setEmail(request.getEmail());
        }
        userRepository.save(user);
        String token = jwtUtil.generateToken(user);
        return buildResponse(token, user);
    }

    public void changePassword(User user, ChangePasswordRequest request) {
        validateNewPassword(request.getNewPassword());
        if (request.getCurrentPassword() == null
                || !passwordEncoder.matches(request.getCurrentPassword(), user.getPassword())) {
            throw new RuntimeException("Mật khẩu hiện tại không đúng.");
        }
        user.setPassword(passwordEncoder.encode(request.getNewPassword()));
        userRepository.save(user);
    }

    public void resetPassword(User user, ResetPasswordRequest request) {
        validateNewPassword(request.getNewPassword());
        if (request.getUsername() == null
                || !user.getUsername().equalsIgnoreCase(request.getUsername().trim())) {
            throw new RuntimeException("Tên đăng nhập xác nhận không đúng.");
        }
        user.setPassword(passwordEncoder.encode(request.getNewPassword()));
        userRepository.save(user);
    }

    private void validateNewPassword(String password) {
        if (password == null || password.length() < 6) {
            throw new RuntimeException("Mật khẩu mới phải có ít nhất 6 ký tự.");
        }
    }

    private AuthResponse buildResponse(String token, User user) {
        AuthResponse r = new AuthResponse();
        r.setToken(token);
        r.setId(user.getId() != null ? user.getId().toString() : null);
        r.setUsername(user.getUsername());
        r.setFullName(user.getFullName());
        r.setEmail(user.getEmail());
        r.setRole(user.getRole().name());
        return r;
    }


```
