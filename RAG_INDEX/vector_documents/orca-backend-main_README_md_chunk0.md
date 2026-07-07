# Knowledge Document: README.md (Chunk 1/8)

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
  "chunk_index": 0,
  "total_chunks": 8
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in orca-backend-main.
- **Dependencies**: Refer to module imports.
- **Tags**: inventory, payment, workspace, notification, chat, production, admin, authentication, security, authorization

## Source Code Chunk
```md
# ORCA Platform

ORCA is a full-stack operations management platform for team-based production and collaboration workflows. The system provides workspaces for teams, task planning, inventory, orders, notifications, chat, AI-assisted planning, authentication, and payment upgrade flows.

This repository is organized as a monorepo with a Spring Boot backend and a React/Vite frontend.

## Table of Contents

- [Business Scope](#business-scope)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Development Commands](#development-commands)
- [Testing and Quality Gates](#testing-and-quality-gates)
- [Deployment](#deployment)
- [Security Guidelines](#security-guidelines)
- [Development Standards](#development-standards)
- [Maintenance Notes](#maintenance-notes)

## Business Scope

ORCA supports operational teams that need a shared workspace for planning, execution, communication, and order coordination.

Core capabilities:

- User registration, login, JWT authentication, and Google OAuth2 callback support.
- Team and group management with invitation flow.
- Task creation, assignment, checklist tracking, and progress monitoring.
- Goal planning and AI-assisted parsing/planning workflows.
- Inventory management and inter-group order coordination.
- Marketplace and order management screens.
- Chat, notification, and presence services.
- VNPAY sandbox/mock payment flow for plan upgrades.
- Admin workspace for operational management.

## Technology Stack

Backend:

- Java 21
- Spring Boot 3.4.x
- Spring Web
- Spring Security
- JWT with JJWT
- OAuth2 Client and Resource Server
- Spring Data JPA / Hibernate
- WebSocket / STOMP
- PostgreSQL for local development and production
- H2 for isolated tests
- Maven Wrapper

Frontend:

- React 19
- TypeScript
- Vite
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

```
