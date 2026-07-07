# Knowledge Document: README.md (Chunk 7/8)

## Metadata
```json
{
  "file_path": "orca-backend-main/README.md",
  "language": "md",
  "module": "orca-backend-main",
  "business_domain": "inventory",
  "tags": [
    "inventory",
    "payment",
    "workspace",
    "notification",
    "chat",
    "production",
    "admin",
    "authentication",
    "security",
    "authorization"
  ],
  "logical_type": "Generic",
  "chunk_index": 6,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
commended engineering gates:

- Backend unit/integration tests must pass.
- Frontend lint and production build must pass.
- No generated artifacts such as `target/`, `dist/`, `node_modules/`, `.class`, `.log`, or `.err` should be committed.
- No credentials or private keys should be committed.
- API changes should include DTO, service, and frontend service updates when applicable.

## Deployment

### Backend Docker Build

From the repository root:

```bash
docker build -t orca-backend backend
```

Run with an environment file:

```bash
docker run -p 8080:8080 --env-file .env orca-backend
```

The backend Dockerfile starts the application with the `prod` Spring profile.

### Frontend Build

```powershell
cd frontend
npm run build
```

The production output is generated in:

```text
frontend/dist/
```

### Production Checklist

- Configure PostgreSQL connection variables.
- Configure JWT, OAuth2, SMTP, AI service, and VNPAY secrets.
- Set `FRONTEND_URL` to the deployed frontend domain.
- Set `VITE_API_BASE_URL` to the deployed backend API URL.
- Verify OAuth callback URL in Google Cloud Console.
- Verify VNPAY return URL.
- Run backend tests and frontend build before release.
- Review startup logs after deployment.

## Security Guidelines

- Never commit real passwords, SMTP credentials, OAuth secrets, JWT secrets, payment secrets, or AI API keys.
- Rotate any secret that was committed or shared.
- Use a strong production `JWT_SECRET`.
- Keep production database credentials outside source code.
- Restrict OAuth redirect URLs to trusted domains only.
- Keep CORS and `FRONTEND_URL` explicit per environment.
- Avoid exposing raw SQL, stack traces, or internal exception details in API responses.

## Development Standards

Backend conventions:

- Keep controllers thin and delegate business logic to services.
- Use DTOs at API boundaries instead of exposing entities directly.
- Keep persistence logic inside repositories.
- Use service-level methods for transactional workflows.
- Prefer explicit validation and meaningful domain errors.
- Add tests for authentication, authorization, payment, order, and task workflows.

Frontend conventions:

- Keep route-level logic in `pages/`.
- Keep shared UI in `components/`.
- Keep API calls in `services/`.
- Keep reusable types in `types/`.
- Use environment variables for API URLs.

```
