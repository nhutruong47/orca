# Knowledge Document: MarketplacePage.tsx (Chunk 12/70)

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
  "chunk_index": 11,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
cationDocument, setPubCertificationDocument] = useState('');
    const [publishing, setPublishing] = useState(false);
    const editingPublishedTeam = myTeams.find(team => team.id === publishTeamId && team.isPublished);
    const selectedPublishTeam = myTeams.find(team => team.id === publishTeamId);
    const publishVerificationStatus = selectedPublishTeam?.verificationStatus || 'NOT_SUBMITTED';

    const [featuredProducts, setFeaturedProducts] = useState<InventoryItem[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                setError('');
                const [teamsAllResult, teamsMineResult] = await Promise.allSettled([
                    teamService.getAllTeams(),
                    teamService.getMyTeams()
                ]);
                if (teamsAllResult.status === 'rejected') {
                    throw teamsAllResult.reason;
                }

                const teamsAll = teamsAllResult.value;
                const teamsMine = teamsMineResult.status === 'fulfilled' ? teamsMineResult.value : [];
                if (teamsMineResult.status === 'rejected') {
                    console.warn('Owned marketplace teams are unavailable', teamsMineResult.reason);
                }
                const publishedTeams = teamsAll.filter(t => t.isPublished);
                const ownedTeams = teamsMine.filter(t => t.ownerId === user?.id);
                setAllTeams(publishedTeams);
                setMyTeams(ownedTeams);
                if (ownedTeams.length > 0) {
                    setBuyerTeamId(ownedTeams[0].id);
                    setPublishTeamId(ownedTeams[0].id);
                }

                const [featuredItems, reqs] = await Promise.all([
                    inventoryService.getFeaturedProducts().catch(error => {
                        console.warn('Featured marketplace products are unavailable', error);
                        return [];
                    }),
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

```
