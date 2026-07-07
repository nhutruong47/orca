# Knowledge Document: MockDataInitializer.java (Chunk 3/3)

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
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in config.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, admin, inventory, security

## Source Code Chunk
```java
ional<User> existingUser = userRepository.findByUsername(username);
            if (existingUser.isPresent()) {
                factoryOwner = existingUser.get();
            } else {
                factoryOwner = User.builder()
                        .username(username)
                        .password(passwordEncoder.encode("123456"))
                        .fullName("Chủ xưởng " + (i + 1))
                        .email("factory" + (i + 1) + "@orca.local")
                        .role(Role.MEMBER)
                        .chipId(java.util.UUID.randomUUID().toString())
                        .build();
                factoryOwner = userRepository.save(factoryOwner);
            }

            Team team = new Team();
            String spec = specialties[i % specialties.length];
            team.setName("Xưởng " + spec + " " + (i + 1));
            team.setDescription("Đây là xưởng chuyên " + spec + " với công nghệ hiện đại, đáp ứng mọi nhu cầu của đối tác.");
            team.setOwner(factoryOwner);
            team.setPublished(true);
            team.setSpecialty(spec);
            team.setRegion(i % 2 == 0 ? "Việt Nam" : "Đắk Lắk");
            team.setCapacity("1000");
            team.setCapacityUnit("kg/tháng");
            team.setCapacityValue(1000.0);
            team.setVerificationStatus(i % 3 == 0 ? "PENDING" : "VERIFIED");
            team.setCompletedOrders(10 + i * 5);
            team.setTotalOrders(15 + i * 5);
            
            // Trust / Rating
            int onTime = (int) ((8 + i) * 0.85);
            team.setOnTimeOrders(onTime);
            team.setLateOrders((10 + i * 5) - onTime);
            int ratings = 5 + (i % 10);
            team.setTotalRatings(ratings);
            team.setSumRatings(ratings * (4.0 + (i % 3) * 0.5));
            if (i != 4 && i != 7 && i != 18) {
                team.setFactoryImageUrl(images.get(i % images.size()));
            }
            team.setFactoryType("roastery");
            
            teamRepository.save(team);
            inventoryService.initializeDefaultInventory(team.getId());
        }
    }
}

```
