# Knowledge Document: DebugController.java (Chunk 3/8)

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
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
ges.get(i % images.size()));
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
                        "configuredUsername", adminUsername,
                        "exists", true,
                        "role", user.getRole().name(),
                        "passwordMatchesConfiguredValue", passwordEncoder.matches(adminPassword, user.getPassword())))
                .orElseGet(() -> Map.of(
                        "configuredUsername", adminUsername,
                        "exists", false,
                        "passwordMatchesConfiguredValue", false));
    }

    @GetMapping("/seed-factories")
    @Transactional
    public Map<String, Object> seedFactories() {
        // Find or create a dummy owner
        User owner = userRepository.findByUsername("admin").orElseGet(() -> {
            User u = new User();
            u.setUsername("admin");
            u.setPassword(passwordEncoder.encode("Admin@123"));
            u.setRole(Role.ADMIN);
            return userRepository.save(u);
        });

        List<Team> factories = List.of(
                createMockTeam("Xưởng Rang Đắk Lắk", "Đắk Lắk, Tây Nguyên", "Rang cà phê,Đóng gói,Gia công OEM", 95, 4.8, 125, 100.0, 5, owner, "50 kg", "3-5 Ngày", 8, "Đang nhận đơn", 25, "1000 m2"),
                createMockTeam("Xưởng Rang Gia Lai", "Gia Lai, Tây Nguyên", "Arabica Specialty,OEM Coffee", 92, 4.9, 87, 85.0, 8, owner, "100 kg", "5-7 Ngày", 5, "Sắp kín lịch", 15, "800 m2"),
                createMockTeam("Cà Phê Mộc Sơn", "Lâm Đồng", "Xay cà phê (Grinding),Rang mẫu / Test profile", 88, 4.5, 42, 150.0, 6, owner, "200 kg", "7-10 Ngày", 12, "Đang nhận đơn", 40, "1500 m2"),
                createMockTeam("Xưởng Rang Quận 9", "Hồ Chí Minh", "Rang cà phê (Roasting),Đóng gói (Packaging)", 98, 5.0, 210, 200.0, 4, owner, "500 kg", "3-5 Ngày", 15, "Tạm ngưng", 60, "2000 m2"),
                createMockTeam("Cầu Đất Roaster", "Lâm Đồng", "Cà phê đặc sản Cầu Đất, rang mộc thủ công", 90, 4.7, 65, 60.0, 8, owner, "10 kg", "2-3 Ngày", 3, "Đang nhận đơn", 10, "300 m2")
        );


```
