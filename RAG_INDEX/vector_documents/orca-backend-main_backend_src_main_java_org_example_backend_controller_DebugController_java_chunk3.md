# Knowledge Document: DebugController.java (Chunk 4/8)

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
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
             createMockTeam("Xưởng Rang Quận 9", "Hồ Chí Minh", "Rang cà phê (Roasting),Đóng gói (Packaging)", 98, 5.0, 210, 200.0, 4, owner, "500 kg", "3-5 Ngày", 15, "Tạm ngưng", 60, "2000 m2"),
                createMockTeam("Cầu Đất Roaster", "Lâm Đồng", "Cà phê đặc sản Cầu Đất, rang mộc thủ công", 90, 4.7, 65, 60.0, 8, owner, "10 kg", "2-3 Ngày", 3, "Đang nhận đơn", 10, "300 m2")
        );

        teamRepository.saveAll(factories);

        List<InventoryItem> products = new java.util.ArrayList<>();
        for (Team f : factories) {
            products.add(createMockProduct(f, "Arabica Cầu Đất", "ROASTED", 500.0, "kg", null, null, null, null, null, null, null, false));
            products.add(createMockProduct(f, "Robusta Honey", "GREEN", 1000.0, "kg", null, null, null, null, null, null, null, false));
            products.add(createMockProduct(f, "Espresso Blend", "PACKAGED", 200.0, "kg", null, null, null, null, null, null, null, false));
            products.add(createMockProduct(f, "Culi Đặc Biệt", "ROASTED", 150.0, "kg", null, null, null, null, null, null, null, false));
            products.add(createMockProduct(f, "Arabica Blend", "GROUND", 300.0, "kg", null, null, null, null, null, null, null, false));
        }

        // Add 5 Featured Products linked to the first factory
        Team mainFactory = factories.get(0);
        products.add(createMockProduct(mainFactory, "Ethiopia Yirgacheffe G1", "ROASTED", 100.0, "kg",
                "450.000đ", "Sơ chế Natural với nốt hương hoa nhài và trà đen đặc trưng. Được thu hoạch từ vùng trồng Yirgacheffe danh tiếng, mang lại trải nghiệm hương vị tinh tế, nhẹ nhàng và hậu vị ngọt kéo dài.",
                "/coffee-hero.png", "Yirgacheffe, Ethiopia", "Light - Medium", "Natural", "Hoa nhài, Trà đen, Cam chanh, Mật ong", true));
        products.add(createMockProduct(mainFactory, "Colombia Supremo", "ROASTED", 50.0, "kg",
                "380.000đ", "Vị đậm đà, body mượt mà với hương chocolate và hạt dẻ.",
                "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=720&q=85",
                "Huila, Colombia", "Medium", "Washed", "Chocolate, Caramel, Hạt dẻ", true));
        products.add(createMockProduct(mainFactory, "Kenya AA Top", "ROASTED", 20.0, "kg",
                "550.000đ", "Độ chua sáng, nốt hương trái cây nhiệt đới rõ nét.",

```
