# Knowledge Document: MarketplacePage.tsx (Chunk 19/70)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/MarketplacePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "notification",
    "factory",
    "inventory",
    "employee",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 18,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
                           quantity: rfqQuantity,
                            deadline: rfqDeadline,
                            contactPhone: deliveryPhone || undefined,
                            contactPhoneAlt: deliveryPhoneAlt || undefined,
                            deliveryAddress: deliveryAddress || undefined,
                            preferredDeliveryFrom: deliveryFrom || undefined,
                            preferredDeliveryTo: deliveryTo || undefined,
                            deliveryFailureAction: deliveryFailureAction || undefined,
                            deliveryNote: deliveryNote || undefined,
                        };
                        await interGroupOrderService.placeOrder(dto);
                    }
                    const request = {
                        type: rfqRequestType as ManufacturingRequest['type'],
                        title: rfqTitle,
                        coffeeType: rfqProductName,
                        quantity: `${rfqQuantity} ${rfqUnit}`,
                        deadline: rfqDeadline,
                        region: selectedSeller?.region || 'Toàn quốc',
                        details: detailLines,
                        buyerTeamId: buyerTeamId || undefined,
                    };
                    const savedRequest = await manufacturingRequestService.create(request);
                    setManufacturingRequests(prev => [savedRequest, ...prev]);
                } catch {
                    alert('Gửi RFQ qua API thất bại. (Chế độ mock vẫn hoạt động)');
                } finally {
                    setSubmitting(false);
                }
            }, 2500);

        } catch {
            alert('Không thể gửi RFQ. Vui lòng thử lại.');
            setSubmitting(false);
        }
    };

    const handlePublish = async (event: React.FormEvent) => {
        event.preventDefault();
        if (!publishTeamId) return;
        const capacityValue = pubCapacityValue.trim() ? Number(pubCapacityValue) : undefined;
        const capacityText = [pubCapacityValue.trim(), pubCapacityUnit].filter(Boolean).join(' ');

        try {
            setPublishing(true);
            await teamService.advertise(publishTeamId, {
                factoryType: pubFactoryType,
                specialty: pubSpecialty,
                capacity: capacityText,

```
