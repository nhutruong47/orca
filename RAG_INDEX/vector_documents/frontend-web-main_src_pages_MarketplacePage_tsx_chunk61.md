# Knowledge Document: MarketplacePage.tsx (Chunk 62/70)

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
  "chunk_index": 61,
  "total_chunks": 70
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, notification, factory, inventory, employee, chat

## Source Code Chunk
```tsx
event.target.value);
                                        if (team) fillPublishForm(team);
                                    }}
                                >
                                    {myTeams.map(team => <option key={team.id} value={team.id}>{team.name} {team.isPublished ? '(Đã đăng)' : ''}</option>)}
                                </select>
                            </div>
                            <div className="mp-form-group">
                                <label>Loại hình xưởng</label>
                                <select value={pubFactoryType} onChange={event => setPubFactoryType(event.target.value)}>
                                    <option value="">Chọn loại hình</option>
                                    {FACTORY_TYPE_OPTIONS.map(option => <option key={option} value={option}>{option}</option>)}
                                </select>
                            </div>
                            <div className="mp-form-group">
                                <label>Khu vực</label>
                                <select value={pubRegion} onChange={event => setPubRegion(event.target.value)}>
                                    <option value="">Chọn khu vực</option>
                                    {REGION_OPTIONS.map(option => <option key={option} value={option}>{option}</option>)}
                                </select>
                            </div>
                            <div className="mp-form-group">
                                <label>Chuyên môn</label>
                                <div className="mp-publish-chip-grid">
                                    {SPECIALTY_OPTIONS.map(option => {
                                        const selected = splitMultiValue(pubSpecialty).includes(option);
                                        return (
                                            <button
                                                type="button"
                                                className={selected ? 'selected' : ''}
                                                key={option}
                                                onClick={() => setPubSpecialty(toggleListValue(splitMultiValue(pubSpecialty), option).join(', '))}
                                            >
                                                {option}

```
