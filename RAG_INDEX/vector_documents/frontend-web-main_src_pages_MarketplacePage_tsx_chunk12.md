# Knowledge Document: MarketplacePage.tsx (Chunk 13/70)

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
  "chunk_index": 12,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
   loadRequests()
                ]);
                setFeaturedProducts(featuredItems);
                setManufacturingRequests(reqs);
            } catch (err) {
                console.error('Failed to load marketplace', err);
                setError('Không thể tải dữ liệu thị trường.');
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [user]);

    useEffect(() => {
        if (!allTeams.length) return;
        const fetchReviews = async () => {
            const summaries: typeof factoryReviewsSummary = {};
            await Promise.all(allTeams.map(async (team) => {
                try {
                    summaries[team.id] = await reviewService.getSummary(team.id);
                } catch {}
            }));
            setFactoryReviewsSummary(summaries);
        };
        fetchReviews();
    }, [allTeams]);

    const loadFactoryReviews = async (teamId: string) => {
        setReviewsLoading(true);
        try {
            const [reviews, summary] = await Promise.all([
                reviewService.getByTeam(teamId),
                reviewService.getSummary(teamId),
            ]);
            setFactoryReviews(prev => ({ ...prev, [teamId]: reviews }));
            setFactoryReviewsSummary(prev => ({ ...prev, [teamId]: summary }));
        } catch (err) {
            console.error('Failed to load factory reviews', err);
        } finally {
            setReviewsLoading(false);
        }
    };

    useEffect(() => {
        if (selectedFactory && activeProfileTab === 'reviews') {
            loadFactoryReviews(selectedFactory.id);
        }
    }, [selectedFactory?.id, activeProfileTab]);

    const factories = useMemo(() => allTeams.map(normalizeFactory), [allTeams]);

    const displayedFactories = useMemo(() => {
        const removeAccents = (str: string) => str ? str.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase() : '';
        const q = removeAccents(searchQuery.trim());
        const minCapacity = Number(minCapacityFilter) || 0;

        return factories.filter(factory => {
            const translatedRegion = t[factory.region || ''] || factory.region || t.vietnam;
            const translatedType = t[factory.factoryType || ''] || factory.factoryType || t.roastery;

```
