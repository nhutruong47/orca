# Knowledge Document: MarketplacePage.tsx (Chunk 16/70)

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
  "chunk_index": 15,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
 '');
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
        fillPublishForm(myTeams[0]);
        setShowPublishModal(true);
    };

    const openEditPublishedTeam = (team: Team) => {
        fillPublishForm(team);
        setShowPublishModal(true);
    };

    const handleFactoryImageFile = (event: React.ChangeEvent<HTMLInputElement>) => {
        const files = Array.from(event.target.files || []);
        if (files.length === 0) return;
        if (pubFactoryImages.length + files.length > 10) {
            alert('Chỉ được tải tối đa 10 ảnh xưởng.');
            event.target.value = '';
            return;
        }
        const invalid = files.find(file => !['image/jpeg', 'image/png', 'image/webp'].includes(file.type));
        if (invalid) {
            alert('Ảnh xưởng chỉ hỗ trợ JPG, PNG hoặc WEBP.');
            event.target.value = '';
            return;
        }
        const tooLarge = files.find(file => file.size > 5 * 1024 * 1024);
        if (tooLarge) {
            alert('Mỗi ảnh xưởng tối đa 5MB.');
            event.target.value = '';
            return;
        }
        Promise.all(files.map(file => new Promise<string>((resolve) => {
            const reader = new FileReader();
            reader.onload = () => resolve(String(reader.result || ''));
            reader.readAsDataURL(file);
        }))).then(images => {
            setPubFactoryImages(current => {
                const next = [...current, ...images].slice(0, 10);
                setPubFactoryImageUrl(next[0] || '');
                return next;
            });
        });
        event.target.value = '';
    };

    const handleDocumentFile = (event: React.ChangeEvent<HTMLInputElement>, setter: (value: string) => void) => {
        const file = event.target.files?.[0];
        if (!file) return;
        if (!['application/pdf', 'image/jpeg', 'image/png'].includes(file.type)) {
            alert('Tài liệu chỉ hỗ trợ PDF, JPG hoặc PNG.');
            event.target.value = '';
            return;
        }

```
