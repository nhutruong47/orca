# Knowledge Document: MarketplacePage.tsx (Chunk 15/70)

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
  "chunk_index": 14,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
tificateFilter === 'has' ? Boolean(factory.certifications?.length) : !factory.certifications?.length);
            const matchesRating = !minRatingFilter || (factory.rating || 0) >= Number(minRatingFilter);

            return matchesSearch && matchesRegion && matchesType && matchesSpecialty && matchesStatus && matchesCapacity && matchesVerified && matchesCertificate && matchesRating;
        });
    }, [certificateFilter, factories, factoryTypeFilter, minCapacityFilter, regionFilter, searchQuery, specialtyFilter, statusFilter, verifiedFilter, minRatingFilter, t]);

    const selectedCompareFactories = factories.filter(factory => compareIds.includes(factory.id));
    const myPublishedTeams = myTeams.filter(team => team.isPublished);

    useEffect(() => {
        setCurrentPage(1);
    }, [displayedFactories]);

    const itemsPerPage = 12;
    const totalPages = Math.ceil(displayedFactories.length / itemsPerPage);
    const featuredFactories = displayedFactories.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

    const totalCompletedOrders = factories.reduce((sum, factory) => sum + (factory.completedOrders || 0), 0);

    const fillPublishForm = (team: Team) => {
        const images = team.factoryImages?.length ? team.factoryImages : team.factoryImageUrl ? [team.factoryImageUrl] : [];
        setPublishTeamId(team.id);
        setPubFactoryType(team.factoryType || '');
        setPubSpecialty(team.specialty || '');
        setPubCapacityValue(team.capacityValue ? String(team.capacityValue) : '');
        setPubCapacityUnit(team.capacityUnit || 'kg/tháng');
        setPubRegion(team.region || '');
        setPubDescription(team.description || '');
        setPubFactoryImageUrl(team.factoryImageUrl || images[0] || '');
        setPubFactoryImages(images);
        setPubBusinessLicense(team.businessLicense || '');
        setPubBusinessAddress(team.businessAddress || '');
        setPubWebsiteUrl(team.websiteUrl || '');
        setPubFacebookUrl(team.facebookUrl || '');
        setPubCertificates(team.certificates || []);
        setPubCertificationDocument(team.certificationDocument || '');
    };

    const openPublishModal = () => {
        if (myTeams.length === 0) {
            alert('Bạn cần tạo ít nhất 1 nhóm xưởng trước khi đăng tải.');
            navigate('/groups');
            return;
        }

```
