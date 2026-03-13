# Agent Context — Digital Wallet API

## Project Overview

This project is a backend-focused application that simulates a digital wallet system.

Users can:

- register
- login
- have an associated wallet
- deposit funds
- transfer money
- view transaction history

The repository includes a backend API and a simple frontend demo.

---

# Tech Stack

Backend

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Alembic
- JWT authentication
- Docker

Frontend

- React
- Vite
- TailwindCSS

---

# Architecture Rules

The backend follows a layered architecture.

Routers  
Handle HTTP requests and responses only.

Services  
Contain business logic.

Repositories  
Handle database access.

Models  
Represent database entities.

Schemas  
Define request and response validation.

Never place business logic in routers.

---

# Database Entities

User  
Wallet  
Transaction

Relationships:

User → Wallet (1:1)  
Wallet → Transactions (1:n)

---

# Coding Rules

- Keep code simple and readable
- Initialize variables at the beginning of blocks
- Avoid unnecessary subqueries
- Use clear naming
- Do not duplicate logic across services
- Follow existing project structure

---

# API Conventions

All endpoints return JSON.

Protected endpoints require:

Authorization: Bearer {token}

Error responses must be consistent.

---

# Frontend Role

The frontend is only a demo UI for the backend API.

Do not introduce unnecessary frontend complexity.

---

# Goals

Maintain a clean, maintainable backend architecture and avoid breaking existing functionality.