# Knowledge Document: AuthService.java (Chunk 1/3)

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
  "chunk_index": 0,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, authentication, security

## Source Code Chunk
```java
package org.example.backend.service;

import org.example.backend.dto.AuthResponse;
import org.example.backend.dto.ChangePasswordRequest;
import org.example.backend.dto.LoginRequest;
import org.example.backend.dto.RegisterRequest;
import org.example.backend.dto.ResetPasswordRequest;
import org.example.backend.dto.UpdateProfileRequest;
import org.example.backend.entity.Role;
import org.example.backend.entity.User;
import org.example.backend.repository.UserRepository;
import org.example.backend.security.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class AuthService {

    @Autowired
    private UserRepository userRepository;
    @Autowired
    private PasswordEncoder passwordEncoder;
    @Autowired
    private JwtUtil jwtUtil;
    @Autowired
    private AuthenticationManager authenticationManager;

    public AuthResponse register(RegisterRequest request) {
        if (userRepository.existsByUsername(request.getUsername())) {
            throw new RuntimeException("Username đã tồn tại: " + request.getUsername());
        }

        User user = User.builder()
                .username(request.getUsername())
                .password(passwordEncoder.encode(request.getPassword()))
                .role(Role.MEMBER)
                .chipId(generateUniqueChipId())
                .build();

        userRepository.save(user);
        String token = jwtUtil.generateToken(user);
        return buildResponse(token, user);
    }

    public AuthResponse login(LoginRequest request) {
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(request.getUsername(), request.getPassword()));
        User user = (User) authentication.getPrincipal();
        String token = jwtUtil.generateToken(user);
        return buildResponse(token, user);
    }

    public AuthResponse updateProfile(User user, UpdateProfileRequest request) {
        if (request.getFullName() != null) {

```
