# Knowledge Document: InviteAcceptPage.tsx (Chunk 2/7)

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
  "chunk_index": 1,
  "total_chunks": 7
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: authorization

## Source Code Chunk
```tsx
oken');
            const headers = { Authorization: `Bearer ${jwt}` };

            if (isCodeMode) {
                setError('Luồng tham gia bằng mã mời chung đã bị vô hiệu hóa. Vui lòng yêu cầu chủ nhóm gửi lời mời qua email.');
                return;
            } else {
                // Join by token
                await axios.post(
                    `${API}/api/teams/invites/accept`,
                    { token },
                    { headers }
                );
            }
            setDone(true);
            setTimeout(() => navigate('/groups'), 2500);
        } catch (err: any) {
            setError(err.response?.data?.error || err.response?.data?.message || 'Không thể tham gia nhóm. Vui lòng thử lại.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{
            minHeight: '100vh',
            background: 'linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '24px',
            fontFamily: "'Inter', sans-serif"
        }}>
            <div style={{
                background: '#ffffff',
                borderRadius: 24,
                boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5)',
                maxWidth: 480,
                width: '100%',
                padding: '48px 40px',
                textAlign: 'center',
                animation: 'fadeInUp 0.4s ease',
                color: '#1a1a1a'
            }}>
                {/* Icon */}
                <div style={{ marginBottom: 28 }}>
                    <div style={{
                        width: 72, height: 72,
                        borderRadius: '50%',
                        background: error ? 'rgba(239,68,68,0.1)' : done ? 'rgba(16,185,129,0.1)' : 'rgba(99,102,241,0.1)',
                        display: 'flex', alignItems: 'center', justifyContent: 'center',
                        margin: '0 auto 20px',
                        fontSize: 36
                    }}>
                        {error ? <ion-icon name="close-circle-outline" style={{ fontSize: '36px', color: '#ef4444' }}></ion-icon>
                            : done ? <ion-icon name="checkmark-circle-outline" style={{ fontSize: '36px', color: '#10b981' }}></ion-icon>

```
