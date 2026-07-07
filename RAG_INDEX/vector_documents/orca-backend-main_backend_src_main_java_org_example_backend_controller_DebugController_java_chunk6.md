# Knowledge Document: DebugController.java (Chunk 7/8)

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
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
Túi 1kg\",\"Bao 5kg\"]}";
        String mockEquipment = "{\"roasters\":[{\"model\":\"Probat P25\",\"capacity\":\"25kg/mẻ\",\"year\":\"2021\"},{\"model\":\"Bühler Infinity\",\"capacity\":\"120kg/mẻ\",\"year\":\"2019\"}],\"packaging\":[\"Máy đóng gói tự động\",\"Máy hút chân không\"],\"grinders\":[\"Mahlkönig EK43\",\"Ditting KR804\"],\"qc\":[\"Máy đo màu rang\",\"Máy đo độ ẩm\",\"Khúc xạ kế\"]}";
        String mockPortfolio = "[{\"name\":\"Dự án OEM Chuỗi Cafe\",\"type\":\"OEM\",\"image\":\"https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=900&q=85\"},{\"name\":\"Gia công xuất khẩu\",\"type\":\"Export\",\"image\":\"https://images.unsplash.com/photo-1504630083234-14187a9df0f5?auto=format&fit=crop&w=900&q=85\"}]";
        String mockReviews = "[{\"author\":\"Nguyen Van A\",\"company\":\"The Coffee Shop\",\"rating\":5,\"date\":\"10/06/2026\",\"content\":\"Chất lượng rang ổn định, giao hàng đúng hẹn.\"},{\"author\":\"Tran Thi B\",\"company\":\"Daily Roast\",\"rating\":4,\"date\":\"02/05/2026\",\"content\":\"Máy móc hiện đại, làm việc chuyên nghiệp, hỗ trợ tốt.\"}]";
        String mockCertificates = "[{\"name\":\"ISO 22000:2018\",\"issueDate\":\"12/05/2022\",\"expDate\":\"12/05/2025\",\"status\":\"Verified\"},{\"name\":\"HACCP\",\"issueDate\":\"10/08/2023\",\"expDate\":\"10/08/2026\",\"status\":\"Verified\"}]";
        
        t.setMetadata(String.format("{\"capabilitiesMock\":%s,\"equipmentMock\":%s,\"portfolioMock\":%s,\"reviewsMock\":%s,\"certificatesMock\":%s}", mockCapabilities, mockEquipment, mockPortfolio, mockReviews, mockCertificates));

        return t;
    }

    @GetMapping("/seed-20-members")
    @Transactional
    public Map<String, Object> seed20Members() {
        // Create owner
        User owner = userRepository.findByUsername("trangdh857").orElseGet(() -> {
            User u = new User();
            u.setUsername("trangdh857");
            u.setFullName("Chủ xưởng Đặng Hải Trang");
            u.setEmail("trangdh857@demo.com");
            u.setRole(Role.MEMBER);
            return u;
        });
        owner.setPassword(passwordEncoder.encode("123456"));
        final User finalOwner = userRepository.save(owner);

        // Create team
        Team team = teamRepository.findAll().stream().filter(t -> "Nhà máy Đặng Hải Trang".equals(t.getName())).findFirst().orElseGet(() -> {

```
