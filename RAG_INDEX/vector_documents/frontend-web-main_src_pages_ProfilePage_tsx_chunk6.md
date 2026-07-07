# Knowledge Document: ProfilePage.tsx (Chunk 7/11)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/ProfilePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "security",
  "tags": [
    "security"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 6,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
v className="webcam-body">
                            <video ref={videoRef} autoPlay playsInline className="webcam-video" />
                        </div>
                        <div className="webcam-footer">
                            <button className="primary-button capture-btn" onClick={capturePhoto}>
                                <ion-icon name="aperture-outline"></ion-icon> Chụp ngay
                            </button>
                        </div>
                    </div>
                </div>
            )}

            <div className="profile-section glass-panel">
                <h2 className="section-title text-glow-active" style={{ display: 'flex', alignItems: 'center', gap: 8, justifyContent: 'space-between' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span className="icon-container glow" style={{ width: 32, height: 32, fontSize: 18 }}><ion-icon name="clipboard-outline"></ion-icon></span> Thông tin cá nhân
                    </div>
                </h2>

                {isEditing ? (
                    <div className="profile-edit-grid">
                        <div className="premium-input-group">
                            <input
                                type="text"
                                className="premium-input"
                                value={formData.fullName}
                                onChange={(e) => setFormData({...formData, fullName: e.target.value})}
                                required
                            />
                            <label className="premium-label">Họ và tên</label>
                            <span className="premium-input-icon"><ion-icon name="person-outline"></ion-icon></span>
                        </div>
                        <div className="premium-input-group">
                            <input
                                type="email"
                                className="premium-input"
                                value={formData.email}
                                onChange={(e) => setFormData({...formData, email: e.target.value})}
                                required
                            />
                            <label className="premium-label">Email liên hệ</label>

```
