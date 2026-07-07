# Knowledge Document: ProfilePage.tsx (Chunk 8/11)

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
  "chunk_index": 7,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
                   type="email"
                                className="premium-input"
                                value={formData.email}
                                onChange={(e) => setFormData({...formData, email: e.target.value})}
                                required
                            />
                            <label className="premium-label">Email liên hệ</label>
                            <span className="premium-input-icon"><ion-icon name="mail-outline"></ion-icon></span>
                        </div>
                    </div>
                ) : (
                    <div className="profile-fields">
                        {profileFields.map((field, index) => (
                            <div key={index} className="profile-field">
                                <div className="field-icon">{field.icon}</div>
                                <div className="field-content">
                                    <span className="field-label">{field.label}</span>
                                    <span className="field-value">{field.value}</span>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>

            <div className="profile-section glass-panel">
                <h2 className="section-title text-glow-active" style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span className="icon-container glow" style={{ width: 32, height: 32, fontSize: 18 }}><ion-icon name="lock-closed-outline"></ion-icon></span> Bảo mật tài khoản
                </h2>
                <div className="security-info">
                    <div className="security-item">
                        <span className="security-icon"><ion-icon name="shield-checkmark-outline" style={{ fontSize: '16px' }}></ion-icon></span>
                        <div>
                            <span className="security-label">Mật khẩu</span>
                            <span className="security-value">Được bảo vệ bằng mã hóa chuẩn công nghiệp BCrypt</span>
                        </div>
                    </div>
                    <div className="security-item">
                        <span className="security-icon"><ion-icon name="finger-print-outline" style={{ fontSize: '16px' }}></ion-icon></span>

```
