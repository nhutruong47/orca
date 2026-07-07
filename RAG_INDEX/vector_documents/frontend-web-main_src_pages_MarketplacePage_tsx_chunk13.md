# Knowledge Document: MarketplacePage.tsx (Chunk 14/70)

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
  "chunk_index": 13,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
e(/[\u0300-\u036f]/g, "").toLowerCase() : '';
        const q = removeAccents(searchQuery.trim());
        const minCapacity = Number(minCapacityFilter) || 0;

        return factories.filter(factory => {
            const translatedRegion = t[factory.region || ''] || factory.region || t.vietnam;
            const translatedType = t[factory.factoryType || ''] || factory.factoryType || t.roastery;
            const translatedTags = factory.specializationsMock?.map(tag => t[tag.replace(' ', '_')] || tag) || [];

            const searchable = removeAccents([
                factory.name,
                factory.region,
                translatedRegion,
                factory.factoryType,
                translatedType,
                factory.specialty,
                factory.description,
                ...(factory.services || []),
                ...(factory.coffeeTypes || []),
                ...translatedTags
            ].filter(Boolean).join(' '));

            const matchesSearch = !q || searchable.includes(q);
            const matchesRegion = !regionFilter || factory.region === regionFilter;
            const matchesType = !factoryTypeFilter || factory.factoryType === factoryTypeFilter;
            const matchesSpecialty = !specialtyFilter || factory.capabilitiesMock?.services.includes(specialtyFilter) || splitMultiValue(factory.specialty).includes(specialtyFilter);
            const matchesStatus = !statusFilter || factory.statusBadgeMock === statusFilter;
            const matchesCapacity = !minCapacity || (factory.capacityValue || 0) >= minCapacity;
            const matchesVerified = !verifiedFilter
                || (verifiedFilter === 'verified' ? factory.verificationStatus === 'APPROVED' : factory.verificationStatus !== 'APPROVED');
            const matchesCertificate = !certificateFilter
                || (certificateFilter === 'has' ? Boolean(factory.certifications?.length) : !factory.certifications?.length);
            const matchesRating = !minRatingFilter || (factory.rating || 0) >= Number(minRatingFilter);

            return matchesSearch && matchesRegion && matchesType && matchesSpecialty && matchesStatus && matchesCapacity && matchesVerified && matchesCertificate && matchesRating;
        });

```
