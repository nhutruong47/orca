# Knowledge Document: User.java (Chunk 2/4)

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
  "chunk_index": 1,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```java
 return aiPlanExpiresAt != null && LocalDateTime.now().isBefore(aiPlanExpiresAt);
        } else if ("professional".equalsIgnoreCase(aiPlan) || "plus".equalsIgnoreCase(aiPlan)) {
            return usage < 100;
        } else {
            return usage < 10;
        }
    }

    public long getAiTrialDaysRemaining() {
        if ("enterprise".equalsIgnoreCase(aiPlan) && aiPlanExpiresAt != null) {
            return java.time.temporal.ChronoUnit.DAYS.between(LocalDateTime.now(), aiPlanExpiresAt);
        }
        return 999;
    }

    public Integer getAiUsageCount() {
        return aiUsageCount != null ? aiUsageCount : 0;
    }

    public void setAiUsageCount(Integer aiUsageCount) {
        this.aiUsageCount = aiUsageCount;
    }

    public boolean isLocked() {
        return locked;
    }

    public void setLocked(boolean locked) {
        this.locked = locked;
    }

    public User() {
    }

    // ===== Builder =====
    public static UserBuilder builder() {
        return new UserBuilder();
    }

    public static class UserBuilder {
        private UUID id;
        private String username;
        private String password;
        private String fullName;
        private String email;
        private Role role = Role.MEMBER;
        private String chipId;
        private boolean locked = false;

        public UserBuilder id(UUID id) {
            this.id = id;
            return this;
        }

        public UserBuilder username(String username) {
            this.username = username;
            return this;
        }

        public UserBuilder password(String password) {
            this.password = password;
            return this;
        }

        public UserBuilder fullName(String fullName) {
            this.fullName = fullName;
            return this;
        }

        public UserBuilder email(String email) {
            this.email = email;
            return this;
        }

        public UserBuilder role(Role role) {
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

```
