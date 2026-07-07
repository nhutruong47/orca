# Knowledge Document: DebugController.java (Chunk 2/8)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/DebugController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security",
    "factory",
    "inventory",
    "employee"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
wordEncoder = passwordEncoder;
        this.entityManager = entityManager;
        this.adminUsername = adminUsername;
        this.adminPassword = adminPassword;
    }

    @GetMapping("/ping")
    public String ping() {
        return "pong";
    }

    @GetMapping("/fix-images")
    @Transactional
    public Map<String, Object> fixImages() {
        List<Team> teams = teamRepository.findAll();
        List<String> images = java.util.Arrays.asList(
            "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=500&q=80",
            "https://images.unsplash.com/photo-1514432324607-a09d9b4aefda?w=500&q=80",
            "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=500&q=80",
            "https://images.unsplash.com/photo-1504630083234-14187a9df0f5?w=500&q=80",
            "https://images.unsplash.com/photo-1498804103079-a6351b050096?w=500&q=80",
            "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=500&q=80",
            "https://images.unsplash.com/photo-1497515114889-1c06568a37b8?w=500&q=80",
            "https://images.unsplash.com/photo-1442512595331-e89e73853f31?w=500&q=80",
            "https://images.unsplash.com/photo-1511537190424-bbbab87ac5eb?w=500&q=80",
            "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500&q=80",
            "https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=500&q=80",
            "https://images.unsplash.com/photo-1512568400610-62da28bc8a13?w=500&q=80",
            "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=500&q=80",
            "https://images.unsplash.com/photo-1507133750050-4a2ce37285f1?w=500&q=80",
            "https://images.unsplash.com/photo-1524350876685-274059332603?w=500&q=80"
        );
        int count = 0;
        for (int i = 0; i < teams.size(); i++) {
            Team t = teams.get(i);
            if (t.getFactoryImageUrl() == null || t.getFactoryImageUrl().isBlank()) {
                t.setFactoryImageUrl(images.get(i % images.size()));
                count++;
            }
        }
        teamRepository.saveAll(teams);
        return Map.of("message", "Đã cập nhật ảnh cho " + count + " xưởng!");
    }

    @GetMapping("/admin-status")
    public Map<String, Object> adminStatus() {
        return userRepository.findByUsername(adminUsername)
                .<Map<String, Object>>map(user -> Map.of(

```
