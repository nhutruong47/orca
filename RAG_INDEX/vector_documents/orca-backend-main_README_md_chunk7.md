# Knowledge Document: README.md (Chunk 8/8)

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
  "chunk_index": 7,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
service-level methods for transactional workflows.
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
- `data/` contains legacy local H2 database files. The active app database is PostgreSQL.
- Runtime logs, build outputs, dependency folders, and generated files are ignored.
- If frontend dependencies were cleaned, run `npm install` again inside `frontend/`.
- If backend build output was cleaned, Maven will regenerate `backend/target/`.

## License

No license has been declared yet. Add a license before distributing or publishing this repository.

<!-- trigger deploy -->

```
