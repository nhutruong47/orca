# Knowledge Document: ProfilePage.tsx (Chunk 3/11)

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
  "chunk_index": 2,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
me,
                    newPassword: passwordForm.newPassword
                });
                setFeedback({ type: 'success', message: 'Đặt lại mật khẩu thành công.' });
            }
            closePasswordForm();
        } catch (error) {
            const message = (error as any)?.response?.data?.error || 'Không thể cập nhật mật khẩu.';
            setFeedback({ type: 'error', message });
        } finally {
            setPasswordSaving(false);
        }
    };

    const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setUploadingAvatar(true);
            try {
                const res = await authService.uploadFile(e.target.files[0]);
                const updatedFormData = { ...formData, avatar: res.url };
                setFormData(updatedFormData);
                const profileRes = await authService.updateProfile(updatedFormData);
                sessionStorage.setItem('token', profileRes.token);
                await fetchUser();
            } catch (error) {
                console.error("Lỗi upload avatar", error);
                alert('Có lỗi khi upload ảnh');
            } finally {
                setUploadingAvatar(false);
            }
        }
    };

    const startWebcam = async () => {
        setShowWebcam(true);
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            streamRef.current = stream;
            if (videoRef.current) {
                videoRef.current.srcObject = stream;
            }
        } catch (err) {
            console.error("Camera access denied", err);
            alert("Không thể truy cập camera. Vui lòng cấp quyền.");
            setShowWebcam(false);
        }
    };

    const stopWebcam = () => {
        if (streamRef.current) {
            streamRef.current.getTracks().forEach(track => track.stop());
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

```
