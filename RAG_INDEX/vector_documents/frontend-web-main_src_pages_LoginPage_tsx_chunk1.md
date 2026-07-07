# Knowledge Document: LoginPage.tsx (Chunk 2/8)

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
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: dashboard, authorization

## Source Code Chunk
```tsx
onst [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const [rememberMe, setRememberMe] = useState(false);
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [activeBrand, setActiveBrand] = useState(0);
    const { login } = useAuth();
    const navigate = useNavigate();
    const location = useLocation();
    const [searchParams] = useSearchParams();
    const locationState = location.state as { from?: { pathname?: string; search?: string; hash?: string } } | null;
    const fromLocation = locationState?.from;

    const stateReturnUrl = fromLocation
        ? `${fromLocation.pathname || ''}${fromLocation.search || ''}${fromLocation.hash || ''}`
        : '';
    const returnUrl = searchParams.get('returnUrl') || stateReturnUrl || '/dashboard';

    useEffect(() => {
        const rememberedUser = localStorage.getItem('orca_remember_username');
        const rememberedPass = localStorage.getItem('orca_remember_password');
        if (rememberedUser) {
            setUsername(rememberedUser);
            setRememberMe(true);
        }
        if (rememberedPass) {
            setPassword(rememberedPass);
        }
    }, []);

    // Auto-rotate brands
    useEffect(() => {
        const timer = setInterval(() => {
            setActiveBrand(prev => (prev + 1) % COFFEE_BRANDS.length);
        }, 3000);
        return () => clearInterval(timer);
    }, []);

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        setError('');

        if (!username.trim() || !password.trim()) {
            setError('Vui lòng nhập đầy đủ thông tin!');
            return;
        }

        setIsLoading(true);
        try {
            await login({ username, password });
            if (rememberMe) {
                localStorage.setItem('orca_remember_username', username.trim());
                localStorage.setItem('orca_remember_password', password.trim());
            } else {
                localStorage.removeItem('orca_remember_username');
                localStorage.removeItem('orca_remember_password');
            }
            navigate(returnUrl, { replace: true });
        } catch (err: unknown) {
            if (err && typeof err === 'object' && 'response' in err) {

```
