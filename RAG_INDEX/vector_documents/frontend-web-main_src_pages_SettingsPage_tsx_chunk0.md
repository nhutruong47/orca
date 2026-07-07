# Knowledge Document: SettingsPage.tsx (Chunk 1/4)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/SettingsPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 4
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security

## Source Code Chunk
```tsx
import { useTheme } from '../context/ThemeContext';
import { useAuth } from '../context/AuthContext';
import './SettingsPage.css';

export default function SettingsPage() {
    const { theme, toggleTheme } = useTheme();
    const { user } = useAuth();
    const displayName = user?.fullName || user?.username || 'ORCA Roaster';
    const displayEmail = user?.email || (user?.username ? `${user.username}@orca-roastery.vn` : 'member@orca-roastery.vn');
    const displayRole = user?.role === 'ADMIN' ? 'Master Roaster' : 'Roastery Member';

    return (
        <div className="settings-page">
            <section className="settings-hero">
                <span>Settings</span>
                <h1>Quản lý tài khoản</h1>
                <p>Cá nhân hóa trải nghiệm rang xay và quản lý các thiết lập bảo mật cho tài khoản ORCA của bạn.</p>
            </section>

            <div className="settings-account-layout">
                <section className="settings-profile-card">
                    <div className="settings-card-top">
                        <span className="settings-pill">Thông tin cá nhân</span>
                        <button type="button">
                            <span className="material-symbols-outlined">edit</span>
                            Chỉnh sửa
                        </button>
                    </div>
                    <h2>Thông tin cơ bản</h2>
                    <div className="settings-info-grid">
                        <div>
                            <span>Họ và tên</span>
                            <strong>{displayName}</strong>
                        </div>
                        <div>
                            <span>Email đăng ký</span>
                            <strong>{displayEmail}</strong>
                        </div>
                        <div>
                            <span>Số điện thoại</span>
                            <strong>+84 902 123 456</strong>
                        </div>
                        <div>
                            <span>Vai trò</span>
                            <strong className="settings-dot-role">{displayRole}</strong>
                        </div>
                    </div>
                    <div className="settings-verification">
                        <img src="/coffee-hero.png" alt="Roastery verification" />
                        <div>

```
