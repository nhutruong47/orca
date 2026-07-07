# Knowledge Document: MarketplacePage.tsx (Chunk 20/70)

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
  "chunk_index": 19,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
lue = pubCapacityValue.trim() ? Number(pubCapacityValue) : undefined;
        const capacityText = [pubCapacityValue.trim(), pubCapacityUnit].filter(Boolean).join(' ');

        try {
            setPublishing(true);
            await teamService.advertise(publishTeamId, {
                factoryType: pubFactoryType,
                specialty: pubSpecialty,
                capacity: capacityText,
                capacityValue: typeof capacityValue === 'number' && Number.isFinite(capacityValue) ? capacityValue : undefined,
                capacityUnit: pubCapacityUnit,
                region: pubRegion,
                description: pubDescription,
                factoryImageUrl: pubFactoryImages[0] || pubFactoryImageUrl,
                factoryImages: pubFactoryImages,
            } as Partial<Team>);
            await teamService.submitVerification(publishTeamId, {
                businessLicense: pubBusinessLicense,
                businessAddress: pubBusinessAddress,
                websiteUrl: pubWebsiteUrl,
                facebookUrl: pubFacebookUrl,
                certificates: pubCertificates,
                certificationDocument: pubCertificationDocument,
            } as Partial<Team>);
            setShowPublishModal(false);
            alert('Xưởng đã được lưu và hồ sơ xác minh đã gửi Admin duyệt.');
            const [teamsAll, teamsMine] = await Promise.all([teamService.getAllTeams(), teamService.getMyTeams()]);
            setAllTeams(teamsAll.filter(t => t.isPublished));
            setMyTeams(teamsMine.filter(t => t.ownerId === user?.id));
        } catch {
            alert('Không thể đăng xưởng. Vui lòng thử lại.');
        } finally {
            setPublishing(false);
        }
    };

    const handleUnpublish = async (teamId: string) => {
        if (!confirm('Gỡ xưởng này khỏi thị trường?')) return;
        try {
            await teamService.unpublish(teamId);
            alert('Đã gỡ xưởng khỏi thị trường.');
            const [teamsAll, teamsMine] = await Promise.all([teamService.getAllTeams(), teamService.getMyTeams()]);
            setAllTeams(teamsAll.filter(t => t.isPublished));
            setMyTeams(teamsMine.filter(t => t.ownerId === user?.id));
        } catch {
            alert('Không thể gỡ xưởng.');
        }
    };

    const deliveryResultLabel = (status?: string) => {
        switch (status) {

```
