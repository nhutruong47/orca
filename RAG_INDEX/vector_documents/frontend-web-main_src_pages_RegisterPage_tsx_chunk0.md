# Knowledge Document: RegisterPage.tsx (Chunk 1/5)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/RegisterPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "dashboard",
  "tags": [
    "dashboard"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 5
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard

## Source Code Chunk
```tsx
import { useEffect, useState, type FormEvent } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import orcaLogo from '../assets/orca-logo.png';

export default function RegisterPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [rememberMe, setRememberMe] = useState(false);
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const { register } = useAuth();
    const navigate = useNavigate();
    const [searchParams] = useSearchParams();
    const returnUrl = searchParams.get('returnUrl') || '/dashboard';

    useEffect(() => {
        const remembered = localStorage.getItem('orca_remember_username');
        if (remembered) {
            setUsername(remembered);
            setRememberMe(true);
        }
    }, []);

    const friendlyRegisterError = (message?: string) => {
        const text = (message || '').toLowerCase();
        if (text.includes('tồn tại') || text.includes('unique') || text.includes('constraint') || text.includes('duplicate')) {
            return 'Tên đăng nhập đã tồn tại. Vui lòng chọn tên khác.';
        }
        if (text.includes('sql') || text.includes('could not execute statement') || text.includes('public.')) {
            return 'Không thể đăng ký tài khoản. Vui lòng thử lại với tên đăng nhập khác.';
        }
        return message || 'Đăng ký thất bại. Vui lòng thử lại.';
    };

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        setError('');

        if (!username.trim() || !password.trim() || !confirmPassword.trim()) {
            setError('Vui lòng nhập đầy đủ thông tin!');
            return;
        }

        if (password.length < 6) {
            setError('Mật khẩu phải có ít nhất 6 ký tự!');
            return;
        }

        if (password !== confirmPassword) {
            setError('Mật khẩu xác nhận không khớp!');
            return;
        }

        setIsLoading(true);
        try {
            await register({ username, password });
            if (rememberMe) {

```
