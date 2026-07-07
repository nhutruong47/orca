# ORCA Architecture

## High-Level Topology
ORCA follows a standard 3-tier microservice-inspired architecture pattern:

1. **Client Tier**: `frontend-web-main`
   - Single Page Application (SPA) built with React.
   - Communicates with Backend via REST API over HTTP/HTTPS.

2. **Application Tier**: 
   - `orca-backend-main`: Primary Java Spring Boot monolithic service handling core business logic, database access, and authentication.
   - `ai-service`: Python FastAPI microservice handling LLM routing, AI prompt management, and natural language tasks.

3. **Data Tier**:
   - PostgreSQL Relational Database (managed via Hibernate/JPA in Spring Boot).

## Communication Flow
- **User -> Frontend**: HTTPS requests loading React static assets.
- **Frontend -> Backend**: RESTful API calls carrying JWT tokens for authentication.
- **Backend -> AI Service**: Internal HTTP requests for AI-based workflows (e.g., chat processing, automated data extraction).
- **Backend -> Database**: JDBC/JPA connections executing SQL queries.

## Design Patterns
- **Backend**: MVC (Model-View-Controller) layered architecture (Controller -> Service -> Repository).
- **Frontend**: Component-based UI with centralized state management (Context API/Hooks).
- **AI Service**: Functional API routing with dependency injection for LLM providers.
