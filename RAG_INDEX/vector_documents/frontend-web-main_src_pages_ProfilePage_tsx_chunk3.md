# Knowledge Document: ProfilePage.tsx (Chunk 4/11)

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
  "chunk_index": 3,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
;
            streamRef.current = null;
        }
        setShowWebcam(false);
    };

    const capturePhoto = () => {
        if (videoRef.current) {
            const canvas = document.createElement('canvas');
            canvas.width = videoRef.current.videoWidth;
            canvas.height = videoRef.current.videoHeight;
            const ctx = canvas.getContext('2d');
            if (ctx) {
                ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
                canvas.toBlob(async (blob) => {
                    if (blob) {
                        stopWebcam();
                        setUploadingAvatar(true);
                        try {
                            const file = new File([blob], `webcam-${Date.now()}.png`, { type: 'image/png' });
                            const res = await authService.uploadFile(file);
                            const updatedFormData = { ...formData, avatar: res.url };
                            setFormData(updatedFormData);
                            const profileRes = await authService.updateProfile(updatedFormData);
                            sessionStorage.setItem('token', profileRes.token);
                            await fetchUser();
                        } catch (error) {
                            console.error("Lỗi upload avatar từ camera", error);
                            alert('Có lỗi khi upload ảnh từ camera');
                        } finally {
                            setUploadingAvatar(false);
                        }
                    }
                }, 'image/png');
            }
        }
    };

    useEffect(() => {
        if (!user) return;
        setFormData({
            fullName: user.fullName || '',
            email: user.email || '',
            avatar: user.avatar || ''
        });
        setPasswordForm(current => ({ ...current, username: user.username || '' }));
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

```
