# Knowledge Document: DebugController.java (Chunk 5/8)

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
  "chunk_index": 4,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
hocolate và hạt dẻ.",
                "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=720&q=85",
                "Huila, Colombia", "Medium", "Washed", "Chocolate, Caramel, Hạt dẻ", true));
        products.add(createMockProduct(mainFactory, "Kenya AA Top", "ROASTED", 20.0, "kg",
                "550.000đ", "Độ chua sáng, nốt hương trái cây nhiệt đới rõ nét.",
                "https://images.unsplash.com/photo-1587293852726-70cdb56c2866?auto=format&fit=crop&w=720&q=85",
                "Nyeri, Kenya", "Light", "Washed", "Blackberry, Chanh vàng, Mía đường", true));
        products.add(createMockProduct(mainFactory, "Máy đo độ ẩm S3", "PACKAGED", 5.0, "chiếc",
                "2.100.000đ", "Thiết bị cầm tay độ chính xác cao cho hạt xanh. Giúp kiểm soát chất lượng cà phê nhân xanh trước khi rang một cách dễ dàng và nhanh chóng.",
                "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?auto=format&fit=crop&w=720&q=85",
                "Đài Loan", "", "", "", true));
        products.add(createMockProduct(mainFactory, "Dịch vụ Rang Test", "PACKAGED", 999.0, "lần",
                "350.000đ", "Gói 5 mẫu profile khác nhau cho 1kg hạt. Phù hợp cho khách hàng muốn tìm ra profile rang tối ưu nhất cho dòng hạt mới trước khi sản xuất số lượng lớn.",
                "https://images.unsplash.com/photo-1580933073521-dc49ac0d4e6a?auto=format&fit=crop&w=720&q=85",
                "", "", "", "", true));

        inventoryRepository.saveAll(products);

        return Map.of("message", "Đã tạo " + factories.size() + " xưởng và " + products.size() + " sản phẩm thành công!");
    }

    private InventoryItem createMockProduct(Team team, String type, String state, Double quantity, String unit, String price, String description, String imageUrl, String origin, String roastLevel, String processing, String tasteNotes, boolean isFeatured) {
        InventoryItem item = new InventoryItem();
        item.setTeam(team);
        item.setProductType(type);
        item.setProductState(state);
        item.setQuantity(quantity);
        item.setUnit(unit);
        item.setLowStockThreshold(50.0);
        item.setPrice(price);
        item.setDescription(description);
        item.setImageUrl(imageUrl);
        item.setOrigin(origin);
        item.setRoastLevel(roastLevel);
        item.setProcessing(processing);

```
