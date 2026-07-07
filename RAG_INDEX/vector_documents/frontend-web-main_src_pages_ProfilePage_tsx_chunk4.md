# Knowledge Document: ProfilePage.tsx (Chunk 5/11)

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
  "chunk_index": 4,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
me || '' }));
    }, [user]);

    useEffect(() => {
        return () => {
            if (streamRef.current) {
                streamRef.current.getTracks().forEach(track => track.stop());
            }
        };
    }, []);

    return (
        <div className="profile-page fade-in">
            {feedback && (
                <div className={`profile-feedback ${feedback.type}`} role="status">
                    <ion-icon name={feedback.type === 'success' ? 'checkmark-circle-outline' : 'alert-circle-outline'}></ion-icon>
                    <span>{feedback.message}</span>
                    <button type="button" onClick={() => setFeedback(null)} aria-label="Đóng thông báo">
                        <ion-icon name="close-outline"></ion-icon>
                    </button>
                </div>
            )}
            <div className="profile-header glass-panel" style={{ position: 'relative', overflow: 'hidden' }}>
                <div className="profile-header-backdrop" style={formData.avatar || user?.avatar ? { backgroundImage: `url(${formData.avatar || user?.avatar})` } : {}}></div>
                <div style={{ position: 'relative', zIndex: 2, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <div className="profile-avatar-large" style={formData.avatar || user?.avatar ? { backgroundImage: `url(${formData.avatar || user?.avatar})`, backgroundSize: 'cover', backgroundPosition: 'center', color: 'transparent' } : {}}>
                        {!(formData.avatar || user?.avatar) && user?.username.charAt(0).toUpperCase()}

                        <div className="avatar-edit-overlay">
                            <label className="avatar-edit-btn" title="Tải ảnh lên">
                                <ion-icon name="cloud-upload-outline"></ion-icon>
                                <input type="file" accept="image/*" style={{ display: 'none' }} onChange={handleFileUpload} />
                            </label>
                            <button className="avatar-edit-btn" title="Chụp từ Camera" onClick={startWebcam}>
                                <ion-icon name="camera-outline"></ion-icon>
                            </button>
                        </div>
                        {uploadingAvatar && <div className="avatar-uploading-spinner"><ion-icon name="sync-outline" className="spin"></ion-icon></div>}

```
