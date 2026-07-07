# Knowledge Document: README.md (Chunk 2/8)

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
  "chunk_index": 1,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
 Vite
- React Router
- Axios
- STOMP/SockJS
- Recharts
- Lucide React
- ESLint

Infrastructure and deployment:

- Docker for backend packaging
- Nginx-based frontend container support
- Vercel-compatible frontend routing config
- Environment-driven production configuration

## Repository Structure

```text
orca/
|-- backend/
|   |-- src/
|   |   |-- main/
|   |   |   |-- java/org/example/backend/
|   |   |   |   |-- config/       # Application, WebSocket, bootstrap config
|   |   |   |   |-- controller/   # REST API controllers
|   |   |   |   |-- dto/          # API request/response DTOs
|   |   |   |   |-- entity/       # JPA entities
|   |   |   |   |-- exception/    # Global exception handling
|   |   |   |   |-- repository/   # Spring Data repositories
|   |   |   |   |-- security/     # JWT, OAuth2, filters, security rules
|   |   |   |   `-- service/      # Business services
|   |   |   `-- resources/       # Spring application profiles
|   |   `-- test/                # Backend tests
|   |-- Dockerfile
|   |-- mvnw
|   |-- mvnw.cmd
|   `-- pom.xml
|-- frontend/
|   |-- public/                  # Static public assets
|   |-- src/
|   |   |-- assets/              # Frontend assets
|   |   |-- components/          # Shared UI components
|   |   |-- context/             # React providers
|   |   |-- pages/               # Route-level pages
|   |   |-- services/            # API and integration clients
|   |   |-- types/               # Shared TypeScript types
|   |   `-- utils/               # Utility functions
|   |-- Dockerfile
|   |-- nginx.conf
|   |-- package.json
|   |-- package-lock.json
|   `-- vite.config.ts
|-- docker-compose.yml            # Local PostgreSQL service
|-- data/                        # Legacy local H2 database files
|-- .legacy/                     # Archived pre-restructure folders
|-- .gitignore
`-- README.md
```

## System Architecture

```text
Browser
  |
  | HTTP / WebSocket
  v
React Frontend
  |
  | REST API / JWT / STOMP
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

```
