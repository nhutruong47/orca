# Knowledge Document: docker-compose.yml (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/docker-compose.yml",
  "language": "yml",
  "module": "orca-backend-main",
  "business_domain": "admin",
  "tags": [
    "admin"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: admin

## Source Code Chunk
```yml
services:
  postgres:
    image: postgres:16-alpine
    container_name: orca-postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: orca_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: admin
    ports:
      - "5432:5432"
    volumes:
      - orca_postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d orca_db"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  orca_postgres_data:

```
