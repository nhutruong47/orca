# Knowledge Document: DebugController.java (Chunk 6/8)

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
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security, factory, inventory, employee

## Source Code Chunk
```java
);
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
        item.setTasteNotes(tasteNotes);
        item.setIsFeatured(isFeatured);
        return item;
    }

    private Team createMockTeam(String name, String region, String specialty, int score, double rating, int orders, double capacity, int delivery, User owner, String moq, String leadTime, int yearsInOperation, String statusBadge, int employeeCount, String factorySize) {
        Team t = new Team();
        t.setName(name);
        t.setDescription("Đây là xưởng mẫu được tạo tự động.");
        t.setRegion(region);
        t.setSpecialty(specialty);
        t.setCapacityValue(capacity);
        t.setCapacityUnit("kg");
        t.setFactoryType("Xưởng rang & đóng gói");
        t.setPublished(true);
        t.setOwner(owner);
        
        t.setCompletedOrders(orders);
        t.setOnTimeOrders(orders - 2);
        t.setTotalOrders(orders + 2);
        
        t.setRating(rating);
        t.setReviewCount((int) (Math.random() * 50) + 10);
        
        t.setMoq(moq);
        t.setLeadTime(leadTime);
        t.setYearsInOperation(yearsInOperation);
        t.setStatusBadge(statusBadge);
        t.setEmployeeCount(employeeCount);
        t.setFactorySize(factorySize);
        t.setVerificationStatus("APPROVED");

        String mockCapabilities = "{\"services\":[\"Rang cà phê\",\"Đóng gói\",\"Gia công OEM\"],\"coffeeTypes\":[\"Arabica\",\"Robusta\",\"Culi / Peaberry\",\"Moka\",\"Catimor\",\"Blend (Phối trộn)\"],\"packagingFormats\":[\"Túi 250g\",\"Túi 500g\",\"Túi 1kg\",\"Bao 5kg\"]}";
        String mockEquipment = "{\"roasters\":[{\"model\":\"Probat P25\",\"capacity\":\"25kg/mẻ\",\"year\":\"2021\"},{\"model\":\"Bühler Infinity\",\"capacity\":\"120kg/mẻ\",\"year\":\"2019\"}],\"packaging\":[\"Máy đóng gói tự động\",\"Máy hút chân không\"],\"grinders\":[\"Mahlkönig EK43\",\"Ditting KR804\"],\"qc\":[\"Máy đo màu rang\",\"Máy đo độ ẩm\",\"Khúc xạ kế\"]}";

```
