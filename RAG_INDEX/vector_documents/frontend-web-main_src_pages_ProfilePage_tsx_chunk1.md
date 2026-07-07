# Knowledge Document: ProfilePage.tsx (Chunk 2/11)

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
  "chunk_index": 1,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
ync () => {
        if (!formData.fullName.trim()) {
            setFeedback({ type: 'error', message: 'Họ và tên không được để trống.' });
            return;
        }
        setSaving(true);
        setFeedback(null);
        try {
            const response = await authService.updateProfile(formData);
            sessionStorage.setItem('token', response.token);
            await fetchUser();
            setIsEditing(false);
            setFeedback({ type: 'success', message: 'Cập nhật hồ sơ thành công.' });
        } catch (error) {
            console.error('Update profile failed', error);
            const message = (error as any)?.response?.data?.error || 'Có lỗi xảy ra khi cập nhật hồ sơ.';
            setFeedback({ type: 'error', message });
        } finally {
            setSaving(false);
        }
    };

    const closePasswordForm = () => {
        setPasswordMode(null);
        setPasswordForm({
            currentPassword: '',
            username: '',
            newPassword: '',
            confirmPassword: ''
        });
    };

    const handlePasswordSubmit = async () => {
        if (passwordForm.newPassword.length < 6) {
            setFeedback({ type: 'error', message: 'Mật khẩu mới phải có ít nhất 6 ký tự.' });
            return;
        }
        if (passwordForm.newPassword !== passwordForm.confirmPassword) {
            setFeedback({ type: 'error', message: 'Mật khẩu nhập lại không khớp.' });
            return;
        }

        setPasswordSaving(true);
        setFeedback(null);
        try {
            if (passwordMode === 'change') {
                await authService.changePassword({
                    currentPassword: passwordForm.currentPassword,
                    newPassword: passwordForm.newPassword
                });
                setFeedback({ type: 'success', message: 'Đổi mật khẩu thành công.' });
            } else {
                await authService.resetPassword({
                    username: passwordForm.username,
                    newPassword: passwordForm.newPassword
                });
                setFeedback({ type: 'success', message: 'Đặt lại mật khẩu thành công.' });
            }
            closePasswordForm();
        } catch (error) {
            const message = (error as any)?.response?.data?.error || 'Không thể cập nhật mật khẩu.';
            setFeedback({ type: 'error', message });

```
