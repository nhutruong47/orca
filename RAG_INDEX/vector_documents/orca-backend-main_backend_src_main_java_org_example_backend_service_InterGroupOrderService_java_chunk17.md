# Knowledge Document: InterGroupOrderService.java (Chunk 18/18)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/service/InterGroupOrderService.java",
  "language": "java",
  "module": "service",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory",
    "production",
    "notification"
  ],
  "logical_type": "Service",
  "chunk_index": 17,
  "total_chunks": 18
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Service in service.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory, production, notification

## Source Code Chunk
```java
 inventoryService.deductPackagedStock(
                                order.getSellerTeam().getId(), productType, order.getQuantity());
                    } catch (Exception e) {
                        System.err.println("Auto inventory deduction failed: " + e.getMessage());
                    }
                }
            }
        }

        InterGroupOrder saved = orderRepo.save(order);

        User buyerToNotify = resolveBuyerUser(order);
        if (buyerToNotify != null) {
            String statusVi = switch (newStatus) {
                case "IN_PRODUCTION" -> "Đang sản xuất";
                case "QC" -> "Đang kiểm tra chất lượng";
                case "COMPLETED" -> "Đã hoàn thành";
                case "SHIPPING" -> "Đang giao hàng";
                case "DELIVERED" -> "Đã giao hàng";
                default -> newStatus;
            };
            notifyUser(buyerToNotify, "Cập nhật đơn hàng",
                    "Đơn \"" + order.getTitle() + "\" đã chuyển sang: " + statusVi,
                    "ORDER_STATUS_UPDATED", null);
        }
        return toDTO(saved);
    }

    /** Resolve the buyer user: either buyerUser (personal) or buyerTeam owner */
    private User resolveBuyerUser(InterGroupOrder order) {
        if (order.getBuyerUser() != null) {
            return order.getBuyerUser();
        }
        if (order.getBuyerTeam() != null) {
            return order.getBuyerTeam().getOwner();
        }
        return null;
    }

    /** Send notification, silently ignore failures */
    private void notifyUser(User user, String title, String message, String type, UUID taskId) {
        try {
            notificationService.createAndSend(user, title, message, type, taskId);
        } catch (Exception e) {
            // Don't let notification failures break order operations
            System.err.println("Failed to send notification: " + e.getMessage());
        }
    }
}

```
