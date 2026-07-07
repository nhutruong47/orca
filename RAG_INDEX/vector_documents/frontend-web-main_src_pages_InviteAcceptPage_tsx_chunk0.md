# Knowledge Document: InviteAcceptPage.tsx (Chunk 1/7)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/InviteAcceptPage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "authorization",
  "tags": [
    "authorization"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization

## Source Code Chunk
```tsx
import { useEffect, useState } from 'react';
import { useSearchParams, useNavigate, useLocation, useParams } from 'react-router-dom';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';
import { jwtDecode } from 'jwt-decode';

const API = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8080';

interface InviteTokenPayload {
    email?: string;
    teamId?: string;
    role?: string;
    exp?: number;
}

export default function InviteAcceptPage() {
    const [searchParams] = useSearchParams();
    const token = searchParams.get('token');
    const { code: inviteCode } = useParams<{ code: string }>();
    const navigate = useNavigate();
    const location = useLocation();
    const { isAuthenticated } = useAuth();

    const [loading, setLoading] = useState(false);
    const [done, setDone] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [tokenInfo, setTokenInfo] = useState<InviteTokenPayload | null>(null);
    const [joinedTeamName] = useState('');

    const isCodeMode = !!inviteCode;

    useEffect(() => {
        if (isCodeMode) return; // Code mode doesn't need token validation
        if (!token) {
            setError('Đường dẫn không hợp lệ — thiếu token.');
            return;
        }
        try {
            const decoded = jwtDecode<InviteTokenPayload>(token);
            if (decoded.exp && decoded.exp * 1000 < Date.now()) {
                setError('Link mời đã hết hạn (sau 7 ngày).');
                return;
            }
            setTokenInfo(decoded);
        } catch {
            setError('Token không hợp lệ hoặc đã bị chỉnh sửa.');
        }
    }, [token, isCodeMode]);

    const handleAccept = async () => {
        if (!isAuthenticated) {
            navigate(`/login?returnUrl=${encodeURIComponent(location.pathname + location.search)}`);
            return;
        }
        try {
            setLoading(true);
            const jwt = sessionStorage.getItem('token');
            const headers = { Authorization: `Bearer ${jwt}` };

            if (isCodeMode) {
                setError('Luồng tham gia bằng mã mời chung đã bị vô hiệu hóa. Vui lòng yêu cầu chủ nhóm gửi lời mời qua email.');
                return;
            } else {
                // Join by token
                await axios.post(
                    `${API}/api/teams/invites/accept`,

```
