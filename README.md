# chat
a simple modular chat with sockets for projects

nombre-del-proyecto/
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada (SpringApplication)
│   ├── api/                 # Capa de transporte (Controllers)
│   │   ├── api_v1/          # Versionamiento de la API
│   │   │   ├── endpoints/   # Rutas específicas (Routers)
│   │   │   └── api.py       # Unión de todos los routers
│   ├── core/                # Configuración global (Security, Config, Env)
│   ├── crud/                # Operaciones básicas de DB (Repositories)
│   ├── models/              # Entidades de Base de Datos (SQLAlchemy/SQLModel)
│   ├── schemas/             # DTOs y validación (Pydantic models)
│   ├── services/            # Lógica de negocio compleja
│   └── db/                  # Sesión de base de datos y migraciones
├── tests/                   # Pruebas unitarias e integración
├── .env                     # Variables de entorno
├── docker-compose.yml
└── pyproject.toml           # Gestión de dependencias (Pom.xml / build.gradle)
