# Knowledge Document: README.md (Chunk 3/8)

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
  "chunk_index": 2,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
P
  v
Spring Boot Backend
  |
  | JPA
  v
Database

External integrations:
- Google OAuth2
- SMTP mail provider
- AI service
- VNPAY sandbox/payment gateway
```

Backend layers:

- `controller`: exposes HTTP endpoints and delegates use cases.
- `service`: contains business logic and orchestration.
- `repository`: handles persistence through Spring Data JPA.
- `entity`: defines persistence models.
- `dto`: defines API boundary objects.
- `security`: centralizes authentication, authorization, JWT, and OAuth2 behavior.

Frontend layers:

- `pages`: route-level experiences.
- `components`: reusable UI and layout primitives.
- `services`: API clients and integration helpers.
- `context`: app-level state providers such as authentication and theme.
- `types`: shared domain and API types.

## Getting Started

### Prerequisites

- Java 21
- Node.js 20 or newer
- npm
- Docker, optional
- PostgreSQL, required for production-like deployment

### Start Backend

Start PostgreSQL first:

```powershell
docker compose up -d postgres
```

```powershell
cd backend
.\mvnw.cmd spring-boot:run
```

Default backend URL:

```text
http://localhost:8080
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

```
