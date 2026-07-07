# Knowledge Document: README.md (Chunk 6/8)

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
  "chunk_index": 5,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
d URL:

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

```powershell
cd frontend
npm install
npm run dev
```

Default frontend URL:

```text
http://localhost:5173
```

## Environment Variables

Production secrets must be provided through environment variables or a secret manager. Do not commit real secrets to the repository.

Backend:

```env
DB_URL=jdbc:postgresql://host:5432/database
DB_USERNAME=database_user
DB_PASSWORD=database_password
DB_POOL_SIZE=5

JWT_SECRET=replace_with_a_long_random_secret

GOOGLE_CLIENT_ID=google_oauth_client_id
GOOGLE_CLIENT_SECRET=google_oauth_client_secret

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


```
