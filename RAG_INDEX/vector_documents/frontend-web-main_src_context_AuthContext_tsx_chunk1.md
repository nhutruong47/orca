# Knowledge Document: AuthContext.tsx (Chunk 2/2)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/context/AuthContext.tsx",
  "language": "tsx",
  "module": "context",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in context.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
    setUser(userInfo);
        sessionStorage.setItem('user', JSON.stringify(userInfo));
    }, []);

    const register = useCallback(async (data: RegisterRequest) => {
        const response = await authService.register(data);
        sessionStorage.setItem('token', response.token);
        setToken(response.token);

        const userInfo = await authService.getMe();
        setUser(userInfo);
        sessionStorage.setItem('user', JSON.stringify(userInfo));
    }, []);

    const logout = useCallback(() => {
        sessionStorage.removeItem('token');
        sessionStorage.removeItem('user');
        setToken(null);
        setUser(null);
    }, []);

    const fetchUser = useCallback(async () => {
        try {
            const userInfo = await authService.getMe();
            setUser(userInfo);
            sessionStorage.setItem('user', JSON.stringify(userInfo));
        } catch (error) {
            console.error('Failed to fetch user:', error);
        }
    }, []);

    const userId = user?.id ?? '';

    return (
        <AuthContext.Provider value={{ user, userId, token, isAuthenticated, isLoading, login, register, logout, fetchUser }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth(): AuthContextType {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}

```
