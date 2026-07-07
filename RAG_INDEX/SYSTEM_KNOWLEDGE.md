# ORCA System Knowledge Base

## Overview
ORCA is a comprehensive enterprise management system designed to handle operations across various modules including Inventory, Booking, Attendance, Production, Payment, Administration, AI Chat, Notifications, Reports, and Analytics.

## Core Modules
1. **Frontend-Web**: A React and Vite-based web application providing the user interface for all modules.
2. **Orca-Backend**: A Java Spring Boot application exposing RESTful APIs, handling business logic, data persistence (PostgreSQL), and security.
3. **AI-Service**: A Python FastAPI service that integrates with AI providers (Gemini, Vertex) to handle conversational logic, task generation, and automated workflows.

## Technology Stack
- **Frontend**: React, TypeScript, Vite, TailwindCSS (assumed), Axios.
- **Backend**: Java 17+, Spring Boot, Spring Security, Hibernate/JPA, PostgreSQL, Maven.
- **AI Service**: Python 3.12+, FastAPI, Uvicorn, httpx.
- **Infrastructure**: Docker, Docker Compose.

## Purpose of this RAG Index
This Knowledge Base is designed to provide an LLM-friendly semantic graph of the entire ORCA monorepo. The `vector_documents/` folder contains chunked embeddings of all source code, allowing AI agents to perform highly accurate Retrieval-Augmented Generation for code generation, bug fixing, and business logic explanation.
