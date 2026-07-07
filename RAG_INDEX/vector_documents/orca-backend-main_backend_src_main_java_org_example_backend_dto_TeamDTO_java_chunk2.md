# Knowledge Document: TeamDTO.java (Chunk 3/5)

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
  "chunk_index": 2,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of DTO in dto.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, employee

## Source Code Chunk
```java
tion = description;
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

    public void setMemberCount(int memberCount) {
        this.memberCount = memberCount;
    }

    public List<MemberInfo> getMembers() {
        return members;
    }

    public void setMembers(List<MemberInfo> members) {
        this.members = members;
    }

    public String getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
    }

    @JsonProperty("isPublished")
    public boolean isPublished() {
        return isPublished;
    }

    public void setPublished(boolean published) {
        isPublished = published;
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
        return factoryImageUrl;
    }

    public void setFactoryImageUrl(String factoryImageUrl) {
        this.factoryImageUrl = factoryImageUrl;
    }

    public List<String> getFactoryImages() {
        return factoryImages;
    }

    public void setFactoryImages(List<String> factoryImages) {
        this.factoryImages = factoryImages;
    }


```
