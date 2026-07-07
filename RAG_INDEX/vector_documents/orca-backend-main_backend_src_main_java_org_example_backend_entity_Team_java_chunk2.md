# Knowledge Document: Team.java (Chunk 3/6)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/entity/Team.java",
  "language": "java",
  "module": "entity",
  "business_domain": "factory",
  "tags": [
    "factory",
    "employee"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 6
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in entity.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, employee

## Source Code Chunk
```java
eatedAt = LocalDateTime.now();
        if (this.inviteCode == null || this.inviteCode.isEmpty()) {
            this.inviteCode = generateInviteCode();
        }
    }

    private static String generateInviteCode() {
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        Random rnd = new Random();
        StringBuilder sb = new StringBuilder(6);
        for (int i = 0; i < 6; i++)
            sb.append(chars.charAt(rnd.nextInt(chars.length())));
        return sb.toString();
    }

    public Team() {
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

    public User getOwner() {
        return owner;
    }

    public void setOwner(User owner) {
        this.owner = owner;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public boolean isPublished() {
        return isPublished;
    }

    public void setPublished(boolean isPublished) {
        this.isPublished = isPublished;
    }

    public String getSpecialty() {
        return specialty;
    }

    public void setSpecialty(String specialty) {
        this.specialty = specialty;
    }

    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }

    public String getRegion() {
        return region;
    }

    public void setRegion(String region) {
        this.region = region;
    }

    public String getFactoryType() {
        return factoryType;
    }

    public void setFactoryType(String factoryType) {
        this.factoryType = factoryType;
    }

    public Double getCapacityValue() {
        return capacityValue;
    }

    public void setCapacityValue(Double capacityValue) {
        this.capacityValue = capacityValue;
    }

    public String getCapacityUnit() {
        return capacityUnit;
    }

    public void setCapacityUnit(String capacityUnit) {
        this.capacityUnit = capacityUnit;
    }

    public String getFactoryImageUrl() {

```
