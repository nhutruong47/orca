# Knowledge Document: README.md (Chunk 4/8)

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
  "chunk_index": 3,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
secret

MAIL_USERNAME=smtp_username
MAIL_PASSWORD=smtp_password_or_app_password

FRONTEND_URL=https://your-frontend-domain.com

AI_SERVICE_API_KEY=ai_service_api_key

VNPAY_PAY_URL=https://sandbox.vnpayment.vn/paymentv2/vpcpay.html
VNPAY_TMN_CODE=vnpay_tmn_code
VNPAY_HASH_SECRET=vnpay_hash_secret
VNPAY_RETURN_URL=https://your-backend-domain.com/api/payments/vnpay/return
```

Neon example:

```env
DB_URL=jdbc:postgresql://ep-example-123456.ap-southeast-1.aws.neon.tech/orca_db?sslmode=require
DB_USERNAME=your_neon_user
DB_PASSWORD=your_neon_password
DB_POOL_SIZE=5
```

Frontend:

```env
VITE_API_BASE_URL=http://localhost:8080
```

## Development Commands

Backend:

```powershell
cd backend
.\mvnw.cmd spring-boot:run
.\mvnw.cmd test
.\mvnw.cmd clean package
```

Frontend:

```powershell
cd frontend
npm install
npm run dev
npm run lint
npm run build
npm run preview
```

## Testing and Quality Gates

Minimum checks before merging or deploying:

```powershell
cd backend
.\mvnw.cmd test
```

```powershell
cd frontend
npm run lint
npm run build
```

Recommended engineering gates:

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


```
