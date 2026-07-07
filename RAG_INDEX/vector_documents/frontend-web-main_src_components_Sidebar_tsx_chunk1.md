# Knowledge Document: Sidebar.tsx (Chunk 2/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/Sidebar.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "subscription",
  "tags": [
    "subscription",
    "report",
    "dashboard",
    "workspace",
    "admin",
    "payment"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: subscription, report, dashboard, workspace, admin, payment

## Source Code Chunk
```tsx
      const myOutboundOrders = await interGroupOrderService.getMyOutboundOrders();
                    const nextCount = myOutboundOrders.filter(order => order.buyerViewed === false).length;
                    if (!cancelled) setPendingOrderCount(nextCount);
                    return;
                }

                const myOutboundOrders = await interGroupOrderService.getMyOutboundOrders();
                const teamOutboundOrders = await Promise.all(
                    ownedTeams.map(team => interGroupOrderService.getOutboundOrders(team.id))
                );
                const inboundOrders = await Promise.all(
                    ownedTeams.map(team => interGroupOrderService.getInboundOrders(team.id))
                );

                const outboundUnread = [
                    ...myOutboundOrders,
                    ...teamOutboundOrders.flat()
                ].filter(order => order.buyerViewed === false).length;

                const inboundUnread = inboundOrders
                    .flat()
                    .filter(order => order.sellerViewed === false).length;

                const nextCount = outboundUnread + inboundUnread;

                if (!cancelled) setPendingOrderCount(nextCount);
            } catch (error) {
                if (!cancelled) setPendingOrderCount(0);
                console.error('Unable to load pending order count', error);
            }
        };

        fetchPendingOrders();
        const intervalId = window.setInterval(fetchPendingOrders, 30000);
        window.addEventListener('focus', fetchPendingOrders);

        return () => {
            cancelled = true;
            window.clearInterval(intervalId);
            window.removeEventListener('focus', fetchPendingOrders);
        };
    }, [user]);

    const adminNavItems = [
        { path: '/admin?section=overview', label: 'Tổng quan & Phân tích', icon: 'speedometer-outline' },
        { path: '/admin?section=workspace_requests', label: 'Yêu cầu mở xưởng', icon: 'person-add-outline' },
        { path: '/admin?section=companies', label: 'Quản lý doanh nghiệp', icon: 'business-outline' },
        { path: '/admin?section=users', label: 'Quản lý người dùng', icon: 'people-outline' },
        { path: '/admin?section=subscriptions', label: 'Gói dịch vụ', icon: 'receipt-outline' },

```
