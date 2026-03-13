# Digital Wallet API

Base backend del proyecto Digital Wallet API construida con FastAPI, SQLAlchemy, MySQL, Alembic y Docker.

## Objetivo de este stage

Este stage deja preparado el proyecto con una arquitectura por capas, configuracion por variables de entorno, conexion base a MySQL y un endpoint de salud.

## Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- Alembic
- Docker

## Estructura

```text
backend/
|-- alembic/
|-- app/
|   |-- core/
|   |-- models/
|   |-- repositories/
|   |-- routers/
|   |-- schemas/
|   `-- services/
|-- tests/
|-- .env.example
|-- alembic.ini
|-- docker-compose.yml
|-- Dockerfile
`-- requirements.txt
```

## Variables de entorno

1. Copiar el archivo de ejemplo:

```bash
cp .env.example .env
```

2. Ajustar valores si fuera necesario.

## Levantar el proyecto con Docker

```bash
docker compose up --build
```

La API queda disponible en:

- `http://localhost:8000`
- `http://localhost:8000/docs`
- `http://localhost:8000/health`

## Ejecutar tests

```bash
docker compose run --rm api pytest
```

## Endpoint disponible

### GET `/health`

Respuesta esperada:

```json
{
  "status": "ok",
  "service": "Digital Wallet API",
  "version": "0.1.0"
}
```

## Proximos pasos sugeridos

- Crear entidades `User`, `Wallet` y `Transaction`
- Agregar migraciones iniciales con Alembic
- Incorporar autenticacion y logica de negocio
