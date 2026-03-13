# Digital Wallet

Este proyecto es una aplicación de billetera digital integrada con un backend en FastAPI y un frontend (próximamente).

## Estructura del Proyecto

```text
digital-wallet/
├── README.md           # Este archivo
├── docker-compose.yml  # Configuración de Docker para todo el proyecto
├── .gitignore          # Archivos ignorados por Git
├── backend/            # Directorio del Backend (FastAPI)
│   ├── app/            # Código fuente
│   ├── alembic/        # Migraciones de base de datos
│   ├── Dockerfile      # Configuración de imagen para el backend
│   └── .env            # Variables de entorno (no trackeado por Git)
└── frontend/           # Directorio del Frontend (Próximamente)
```

## Requisitos Previos

- Docker y Docker Compose
- Python 3.10+ (opcional, para desarrollo local sin Docker)

## Configuración y Ejecución

### 1. Variables de Entorno
Asegúrate de tener un archivo `.env` en la carpeta `backend/`. Existe un archivo `.env.example` en esa misma carpeta que puedes usar como base:

```bash
cp backend/.env.example backend/.env
```

### 2. Levantar el proyecto con Docker
Desde la raíz del proyecto, ejecuta:

```bash
docker compose up --build
```

### 3. Puertos de Acceso

- **API/Documentación**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Base de Datos (MySQL)**: `localhost:3307` 

> [!IMPORTANT]
> Se ha configurado el puerto **3307** para la base de datos externa para evitar conflictos con instalaciones locales de MySQL que suelen usar el puerto 3306.

## Desarrollo

### Base de Datos
Si necesitas conectarte a la base de datos desde un cliente externo (como DBeaver o TablePlus):
- **Host**: `127.0.0.1`
- **Puerto**: `3307`
- **Usuario**: `wallet_user`
- **Password**: `wallet_password` (según `.env`)

### Próximos Pasos
- [ ] Implementar autenticación JWT.
- [ ] Crear modelos para Usuarios, Billeteras y Transacciones.
- [ ] Iniciar el desarrollo del Frontend.
