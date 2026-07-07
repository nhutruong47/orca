# Knowledge Document: ProtectedRoute.tsx (Chunk 1/1)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/components/ProtectedRoute.tsx",
  "language": "tsx",
  "module": "components",
  "business_domain": "Core",
  "tags": [],
  "logical_type": "Component/Page",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in components.
- **Dependencies**: Refer to module imports.
- **Tags**: 

## Source Code Chunk
```tsx
import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

interface ProtectedRouteProps {
  children: React.ReactNode;
}

export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { isAuthenticated, isLoading } = useAuth();
  const location = useLocation();

  if (isLoading) {
    return (
      <div className="loading-screen">
        <div className="loading-spinner" />
        <p>Đang tải...</p>
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return <>{children}</>;
}

```
