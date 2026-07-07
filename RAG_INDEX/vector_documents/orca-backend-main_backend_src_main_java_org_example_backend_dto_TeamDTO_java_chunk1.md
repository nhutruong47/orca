# Knowledge Document: TeamDTO.java (Chunk 2/5)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/dto/TeamDTO.java",
  "language": "java",
  "module": "dto",
  "business_domain": "factory",
  "tags": [
    "factory",
    "admin",
    "employee"
  ],
  "logical_type": "DTO",
  "chunk_index": 1,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, employee

## Source Code Chunk
```java
           this.userId = userId;
        }

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public String getFullName() {
            return fullName;
        }

        public void setFullName(String fullName) {
            this.fullName = fullName;
        }

        public String getGroupRole() {
            return groupRole;
        }

        public void setGroupRole(String groupRole) {
            this.groupRole = groupRole;
        }

        public String getJoinedAt() {
            return joinedAt;
        }

        public void setJoinedAt(String joinedAt) {
            this.joinedAt = joinedAt;
        }

        public List<String> getJobLabels() {
            return jobLabels;
        }

        public void setJobLabels(List<String> jobLabels) {
            this.jobLabels = jobLabels;
        }

        public int getTotalTasks() {
            return totalTasks;
        }

        public void setTotalTasks(int totalTasks) {
            this.totalTasks = totalTasks;
        }

        public int getCompletedTasks() {
            return completedTasks;
        }

        public void setCompletedTasks(int completedTasks) {
            this.completedTasks = completedTasks;
        }

        public int getCompletionRate() {
            return completionRate;
        }

        public void setCompletionRate(int completionRate) {
            this.completionRate = completionRate;
        }
    }

    // === Getters & Setters ===
    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public UUID getOwnerId() {
        return ownerId;
    }

    public void setOwnerId(UUID ownerId) {
        this.ownerId = ownerId;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    public int getMemberCount() {
        return memberCount;
    }


```
