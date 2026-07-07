# Knowledge Document: ProfilePage.tsx (Chunk 1/11)

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
  "chunk_index": 0,
  "total_chunks": 11
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: security

## Source Code Chunk
```tsx
import { useState, useRef, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { authService } from '../services/authService';
import '../components/Profile.css';

export default function ProfilePage() {
    const { user, fetchUser } = useAuth();
    const [isEditing, setIsEditing] = useState(false);
    const [formData, setFormData] = useState({
        fullName: user?.fullName || '',
        email: user?.email || '',
        avatar: user?.avatar || ''
    });
    const [saving, setSaving] = useState(false);
    const [uploadingAvatar, setUploadingAvatar] = useState(false);
    const [passwordMode, setPasswordMode] = useState<'change' | 'reset' | null>(null);
    const [passwordSaving, setPasswordSaving] = useState(false);
    const [passwordForm, setPasswordForm] = useState({
        currentPassword: '',
        username: '',
        newPassword: '',
        confirmPassword: ''
    });
    const [feedback, setFeedback] = useState<{ type: 'success' | 'error'; message: string } | null>(null);

    // Webcam states
    const [showWebcam, setShowWebcam] = useState(false);
    const videoRef = useRef<HTMLVideoElement>(null);
    const streamRef = useRef<MediaStream | null>(null);

    const profileFields = [
        { icon: <ion-icon name="key-outline" style={{ fontSize: '16px' }}></ion-icon>, label: 'User ID', value: user?.id?.toString() || '—' },
        { icon: <ion-icon name="person-outline" style={{ fontSize: '16px' }}></ion-icon>, label: 'Tên đăng nhập', value: user?.username || '—' },
        { icon: <ion-icon name="document-text-outline" style={{ fontSize: '16px' }}></ion-icon>, label: 'Họ tên', value: user?.fullName || '—' },
        { icon: <ion-icon name="mail-outline" style={{ fontSize: '16px' }}></ion-icon>, label: 'Email', value: user?.email || '—' },
        { icon: <ion-icon name="ribbon-outline" style={{ fontSize: '16px' }}></ion-icon>, label: 'Vai trò', value: 'Thành viên' },
    ];

    const handleSave = async () => {
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

```
