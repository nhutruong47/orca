# Knowledge Document: AuthController.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/AuthController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "authentication",
    "security"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
uthenticationException e) {
            log.warn("Login failed for username '{}'", request != null ? request.getUsername() : null);
            return ResponseEntity.status(401).body(Map.of("error", "Tai khoan hoac mat khau khong dung!"));
        } catch (Exception e) {
            log.error("Login failed due to server error for username '{}'", request != null ? request.getUsername() : null, e);
            return ResponseEntity.status(500).body(Map.of("error", "Khong the dang nhap do loi he thong."));
        }
    }

    @PutMapping("/profile")
    public ResponseEntity<?> updateProfile(@AuthenticationPrincipal User user, @RequestBody UpdateProfileRequest request) {
        try {
            return ResponseEntity.ok(authService.updateProfile(user, request));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PutMapping("/password")
    public ResponseEntity<?> changePassword(
            @AuthenticationPrincipal User user,
            @RequestBody ChangePasswordRequest request) {
        try {
            authService.changePassword(user, request);
            return ResponseEntity.ok(Map.of("message", "Đổi mật khẩu thành công."));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/password/reset")
    public ResponseEntity<?> resetPassword(
            @AuthenticationPrincipal User user,
            @RequestBody ResetPasswordRequest request) {
        try {
            authService.resetPassword(user, request);
            return ResponseEntity.ok(Map.of("message", "Đặt lại mật khẩu thành công."));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/me")
    public ResponseEntity<?> getCurrentUser(@AuthenticationPrincipal User user) {
        Map<String, Object> info = new HashMap<>();
        info.put("id", user.getId().toString());
        info.put("username", user.getUsername());
        info.put("fullName", user.getFullName() != null ? user.getFullName() : "");
        info.put("email", user.getEmail() != null ? user.getEmail() : "");
        info.put("avatar", user.getAvatar() != null ? user.getAvatar() : "");

```
