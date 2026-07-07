# Knowledge Document: ProfilePage.tsx (Chunk 6/11)

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
  "chunk_index": 5,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
                     <button className="avatar-edit-btn" title="Chụp từ Camera" onClick={startWebcam}>
                                <ion-icon name="camera-outline"></ion-icon>
                            </button>
                        </div>
                        {uploadingAvatar && <div className="avatar-uploading-spinner"><ion-icon name="sync-outline" className="spin"></ion-icon></div>}
                    </div>

                    <h1 className="profile-name" style={{ marginTop: 16 }}>{formData.fullName || user?.fullName || user?.username}</h1>
                    <span className="role-badge large member" style={{ marginTop: 8 }}><ion-icon name="person-outline" style={{ fontSize: '14px' }}></ion-icon> Thành viên</span>
                </div>

                <button
                    className={isEditing ? "primary-button pulse" : "secondary-button"}
                    style={{ position: 'absolute', top: 20, right: 20, padding: '10px 20px', borderRadius: 20, zIndex: 2 }}
                    onClick={() => isEditing ? handleSave() : setIsEditing(true)}
                    disabled={saving}
                >
                    {saving ? (
                        <><ion-icon name="sync-outline" className="spin"></ion-icon> Đang lưu...</>
                    ) : (
                        isEditing ? <><ion-icon name="checkmark-outline"></ion-icon> Lưu thay đổi</> : <><ion-icon name="create-outline"></ion-icon> Chỉnh sửa hồ sơ</>
                    )}
                </button>
            </div>

            {showWebcam && (
                <div className="webcam-modal-backdrop">
                    <div className="webcam-modal glass-panel">
                        <div className="webcam-header">
                            <h3>Chụp ảnh đại diện</h3>
                            <button onClick={stopWebcam} className="close-btn"><ion-icon name="close-outline"></ion-icon></button>
                        </div>
                        <div className="webcam-body">
                            <video ref={videoRef} autoPlay playsInline className="webcam-video" />
                        </div>
                        <div className="webcam-footer">
                            <button className="primary-button capture-btn" onClick={capturePhoto}>
                                <ion-icon name="aperture-outline"></ion-icon> Chụp ngay

```
