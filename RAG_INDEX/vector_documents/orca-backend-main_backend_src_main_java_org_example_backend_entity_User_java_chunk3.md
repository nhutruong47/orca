# Knowledge Document: User.java (Chunk 4/4)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/User.java",
  "language": "java",
  "module": "entity",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 3,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```java
his.aiTrialStartDate = aiTrialStartDate;
    }

    public String getAiPlan() {
        return aiPlan;
    }

    public void setAiPlan(String aiPlan) {
        this.aiPlan = aiPlan;
    }

    public LocalDateTime getAiPlanExpiresAt() {
        return aiPlanExpiresAt;
    }

    public void setAiPlanExpiresAt(LocalDateTime aiPlanExpiresAt) {
        this.aiPlanExpiresAt = aiPlanExpiresAt;
    }

    // ===== UserDetails =====
    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return List.of(new SimpleGrantedAuthority("ROLE_" + role.name()));
    }

    @Override
    public String getUsername() {
        return this.username;
    }

    @Override
    public String getPassword() {
        return this.password;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return !locked;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}

```
