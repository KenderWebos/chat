# Arquitectura de FastAPI

## Desglose de los Componentes Clave

1. **main.py**
   Es el cerebro. Aquí instancias la aplicación de FastAPI, configuras los Middlewares (CORS, logs) y conectas los routers principales.
   * **Equivalente Spring Boot:** La clase con la anotación `@SpringBootApplication`.

2. **api/ (Los Controllers)**
   En lugar de un archivo gigante, usas `APIRouter`. Cada recurso (usuarios, productos, pedidos) tiene su propio archivo de rutas.
   * **Equivalente Spring Boot:** Clases con `@RestController`.

3. **schemas/ vs models/**
   * **models/**: Define cómo se guardan los datos en la tabla (definición de SQLAlchemy). Son tus `@Entity`.
   * **schemas/**: Define cómo se reciben o envían los datos vía JSON (definición de Pydantic). Son tus DTOs.
   * *Nota:* FastAPI usa los schemas para generar automáticamente la documentación Swagger.

4. **crud/ o repositories/**
   Aquí es donde escribes las consultas a la base de datos. FastAPI fomenta que la lógica de persistencia esté separada de la ruta.
   * **Equivalente Spring Boot:** Interfaces/Clases de Spring Data JPA.

5. **core/**
   Aquí guardas la lógica de seguridad (JWT), la configuración de variables de entorno y constantes globales.
   * **Equivalente Spring Boot:** El paquete `config` o `security`.

---

## Flujo de una Petición (Request Lifecycle)

1. **Request**: Llega un JSON al endpoint definido en `api/`.
2. **Validation**: FastAPI usa el **Schema** (Pydantic) para validar que el JSON sea correcto. Si los tipos no coinciden, devuelve un error 422 automáticamente.
3. **Logic**: El router llama a una función en **Services** o **CRUD**.
4. **Database**: El CRUD llama al **Model** para interactuar con la base de datos.
5. **Response**: Los datos se transforman de un Model a un Schema de salida para enviarse al cliente como JSON.