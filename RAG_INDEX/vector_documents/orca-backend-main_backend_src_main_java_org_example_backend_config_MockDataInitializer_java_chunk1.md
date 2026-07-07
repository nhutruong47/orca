# Knowledge Document: MockDataInitializer.java (Chunk 2/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/config/MockDataInitializer.java",
  "language": "java",
  "module": "config",
  "business_domain": "factory",
  "tags": [
    "factory",
    "admin",
    "inventory",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in config.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, inventory, security

## Source Code Chunk
```java
ạch"};
        List<String> images = Arrays.asList(
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
            "https://images.unsplash.com/photo-1524350876685-274059332603?w=500&q=80",
            "https://images.unsplash.com/photo-1587293852726-70cdb56c2866?w=500&q=80",
            "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=500&q=80",
            "https://images.unsplash.com/photo-1580933073521-dc49ac0d4e6a?w=500&q=80",
            "https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=500&q=80",
            "https://images.unsplash.com/photo-1559525839-b184a4d698c7?w=500&q=80"
        );

        for (int i = 0; i < 20; i++) {
            // Create a unique owner for each factory
            String username = "factory_owner_" + (i + 1);
            User factoryOwner;
            Optional<User> existingUser = userRepository.findByUsername(username);
            if (existingUser.isPresent()) {
                factoryOwner = existingUser.get();
            } else {
                factoryOwner = User.builder()
                        .username(username)
                        .password(passwordEncoder.encode("123456"))
                        .fullName("Chủ xưởng " + (i + 1))

```
