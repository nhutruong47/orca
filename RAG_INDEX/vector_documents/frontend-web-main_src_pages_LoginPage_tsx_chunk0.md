# Knowledge Document: LoginPage.tsx (Chunk 1/8)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/LoginPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "dashboard",
  "tags": [
    "dashboard",
    "authorization"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, authorization

## Source Code Chunk
```tsx
import { useState, useEffect, type FormEvent } from 'react';
import { Link, useLocation, useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import orcaLogo from '../assets/orca-logo.png';

const COFFEE_BRANDS = [
    { name: 'Trung Nguyên Legend', desc: 'Thương hiệu cà phê số 1 Việt Nam', emoji: 'TN' },
    { name: 'Highlands Coffee', desc: 'Chuỗi cà phê hiện đại hàng đầu', emoji: 'HC' },
    { name: 'Phúc Long Heritage', desc: 'Di sản cà phê & trà Việt', emoji: 'PL' },
    { name: 'The Coffee House', desc: 'Không gian cà phê sáng tạo', emoji: 'CH' },
    { name: 'Cà Phê Đắk Lắk', desc: 'Thủ phủ cà phê Tây Nguyên', emoji: 'DL' },
    { name: 'Lavazza (Italy)', desc: 'Hương vị Espresso đỉnh cao', emoji: 'LV' },
];

const COFFEE_BRAND_LOGOS = [
    {
        key: 'trung-nguyen',
        top: 'TRUNG',
        bottom: 'NGUYEN',
        src: 'https://cdn.haitrieu.com/wp-content/uploads/2022/01/Logo-Trung-Nguyen-Ori.png'
    },
    {
        key: 'highlands',
        top: 'Highlands',
        bottom: 'COFFEE',
        src: 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Highlands_Coffee_5G.svg'
    },
    {
        key: 'phuc-long',
        top: 'PHUC',
        bottom: 'LONG',
        src: 'https://congtyquatang.com.vn/wp-content/uploads/2026/04/logo-phuc-long-vector-04.jpg'
    },
    {
        key: 'coffee-house',
        top: 'THE',
        bottom: 'COFFEE HOUSE',
        src: 'https://upload.wikimedia.org/wikipedia/commons/9/97/The_Coffee_House_logo.svg'
    },
    {
        key: 'dak-lak',
        top: 'DAKLAK',
        bottom: 'COFFEE',
        src: 'https://upload.wikimedia.org/wikipedia/commons/8/86/Emblem_of_Daklak_Province.svg'
    },
    {
        key: 'lavazza',
        top: 'LAVAZZA',
        bottom: 'ITALY',
        src: 'https://upload.wikimedia.org/wikipedia/commons/0/04/Lavazza_-_logo_%28Italy%2C_1995%29.svg'
    },
];

export default function LoginPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [rememberMe, setRememberMe] = useState(false);
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [activeBrand, setActiveBrand] = useState(0);
    const { login } = useAuth();

```
