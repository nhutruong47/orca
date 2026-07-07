# Knowledge Document: README.md (Chunk 5/8)

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
  "chunk_index": 4,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
QL connection variables.
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
- Avoid hardcoding production URLs or credentials.

Branch and commit recommendations:

- Use feature branches for new functionality.
- Keep commits focused and reviewable.
- Include tests or build verification for behavior changes.
- Do not mix formatting-only changes with business logic changes unless intentional.

## Maintenance Notes

- `.legacy/` contains archived folders from the previous project layout. It is ignored by Git and should not be used for active development.
Default backend URL:

```text
http://localhost:8080
```

Start PostgreSQL first:

```powershell
docker compose up -d postgres
```

Run backend with the local PostgreSQL profile:

```powershell
cd backend
.\mvnw.cmd spring-boot:run "-Dspring-boot.run.profiles=local"
```

Default local PostgreSQL connection:

```text
jdbc:postgresql://localhost:5432/orca_db
user: postgres
password: admin
```

### Start Frontend


```
