# Knowledge Document: OrderManagementPage.tsx (Chunk 2/23)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/OrderManagementPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "production",
  "tags": [
    "production"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 23
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: production

## Source Code Chunk
```tsx
                console.error(err);
            }
        };
        fetchTeams();
    }, [user]);

    useEffect(() => {
        if (activeTab === 'inbound' && (selectedTeam === PERSONAL_BUYER || selectedTeam === '')) {
            setOrders([]);
            setLoading(false);
            return;
        }

        const fetchOrders = async () => {
            setLoading(true);
            try {
                if (activeTab === 'outbound') {
                    const data = (selectedTeam === PERSONAL_BUYER || selectedTeam === '')
                        ? await interGroupOrderService.getMyOutboundOrders()
                        : await interGroupOrderService.getOutboundOrders(selectedTeam);
                    
                    const unreadIds = data.filter(o => o.buyerViewed === false).map(o => o.id);
                    if (unreadIds.length > 0) {
                        interGroupOrderService.markViewed(unreadIds, 'BUYER').catch(console.error);
                        data.forEach(o => { if (unreadIds.includes(o.id)) o.buyerViewed = true; });
                    }
                    setOrders(data);
                } else {
                    const data = await interGroupOrderService.getInboundOrders(selectedTeam);
                    const unreadIds = data.filter(o => o.sellerViewed === false).map(o => o.id);
                    if (unreadIds.length > 0) {
                        interGroupOrderService.markViewed(unreadIds, 'SELLER').catch(console.error);
                        data.forEach(o => { if (unreadIds.includes(o.id)) o.sellerViewed = true; });
                    }
                    setOrders(data);
                }
            } catch (err) {
                console.error(err);
            } finally {
                setLoading(false);
            }
        };

        fetchOrders();
    }, [selectedTeam, activeTab]);

    useEffect(() => {
        const fetchUnreadCounts = async () => {
            if (!user) return;
            try {
                const outb = (selectedTeam === PERSONAL_BUYER || selectedTeam === '')
                    ? await interGroupOrderService.getMyOutboundOrders()
                    : await interGroupOrderService.getOutboundOrders(selectedTeam);
                setUnreadOutboundCount(outb.filter(o => o.buyerViewed === false).length);
            } catch (err) {}
        };
        fetchUnreadCounts();

```
