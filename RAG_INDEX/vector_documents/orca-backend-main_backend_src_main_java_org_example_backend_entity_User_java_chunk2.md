# Knowledge Document: User.java (Chunk 3/4)

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
  "chunk_index": 2,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```java
      this.role = role;
            return this;
        }

        public UserBuilder chipId(String chipId) {
            this.chipId = chipId;
            return this;
        }

        public UserBuilder locked(boolean locked) {
            this.locked = locked;
            return this;
        }

        public User build() {
            User user = new User();
            user.id = this.id;
            user.username = this.username;
            user.password = this.password;
            user.fullName = this.fullName;
            user.email = this.email;
            user.role = this.role;
            user.chipId = this.chipId;
            user.locked = this.locked;
            return user;
        }
    }

    // ===== Getters & Setters =====
    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }

    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }

    public String getChipId() {
        return chipId;
    }

    public void setChipId(String chipId) {
        this.chipId = chipId;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public LocalDateTime getAiTrialStartDate() {
        return aiTrialStartDate;
    }

    public void setAiTrialStartDate(LocalDateTime aiTrialStartDate) {
        this.aiTrialStartDate = aiTrialStartDate;
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


```
