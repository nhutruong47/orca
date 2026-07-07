# Knowledge Document: InventoryController.java (Chunk 2/2)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/controller/InventoryController.java",
  "language": "java",
  "module": "controller",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "security",
    "authentication"
  ],
  "logical_type": "Controller",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Controller in controller.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, security, authentication

## Source Code Chunk
```java
body.get("quantity");
            if (qty == null) {
                return ResponseEntity.badRequest().body(Map.of("error", "Vui lòng nhập số lượng (quantity)"));
            }
            return ResponseEntity.ok(inventoryService.updateQuantity(id, qty));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> delete(@PathVariable UUID id, @AuthenticationPrincipal User user) {
        accessControlService.requireInventoryItemAccess(user, id);
        try {
            inventoryService.delete(id);
            return ResponseEntity.ok(Map.of("message", "Đã xóa mặt hàng khỏi kho"));
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(Map.of("error", e.getMessage()));
        }
    }
}

```
