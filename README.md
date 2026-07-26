# 📚 API de Gestión de Estudiantes

Proyecto de API REST desarrollado en **FastAPI** con **SQLite3** para gestionar información de estudiantes. La API permite crear, leer, actualizar y eliminar registros de estudiantes mediante endpoints HTTP.

---

## ⚙️ Cómo Instalar y Ejecutar

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/kevinhndz/API_Estudiante.git
cd API_Estudiante
```

### Paso 2: Crear el entorno virtual

```bash
python -m venv venv
```

Activar el entorno virtual:

**En Windows:**
```bash
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### Paso 3: Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar el servidor

```bash
uvicorn main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000` 🚀

---

## 📂 Estructura del Proyecto

```
API_Estudiante/
├── main.py              # Archivo principal con los endpoints
├── database.py          # Configuración y conexión de la BD
├── schemas.py           # Modelos de validación con Pydantic
├── crud.py              # Funciones para operaciones en la BD
├── estudiantes.db       # Base de datos SQLite
├── requirements.txt     # Dependencias del proyecto
└── img/                 # Capturas de las pruebas
    ├── POST.png
    ├── GET.png
    ├── GET_UNICO.png
    ├── PUT.png
    └── DELETE.png
```

---

## 📸 Evidencias de Pruebas en Postman (CRUD)

A continuación se muestran las pruebas de funcionamiento enviadas a los endpoints con sus correspondientes códigos de estado HTTP (`200 OK`):

### 1. Crear Estudiante (`POST /estudiantes`)

Registra un nuevo estudiante enviando los datos requeridos en formato JSON en el cuerpo (`Body`) de la petición.

![POST Estudiante](img/POST.png)

**Ejemplo de solicitud:**
```json
{
  "nombre": "Carlos Gomez",
  "cuenta": "20231001",
  "carrera": "Sistemas",
  "correo": "carlos@gmail.com",
  "edad": 21
}
```

---

### 2. Consultar Lista General (`GET /estudiantes`)

Obtiene el arreglo completo con todos los estudiantes registrados almacenados en la base de datos.

![GET Todos](img/GET.png)

**Respuesta esperada:** Un arrglo de objetos con todos los estudiantes

---

### 3. Consultar Estudiante por ID (`GET /estudiantes/{id}`)

Filtra y devuelve de forma individual la información del estudiante que coincida con el identificador en la URL.

![GET por ID](img/GET_UNICO.png)

**Ejemplo:** `GET /estudiantes/1`

**Respuesta:** Objeto JSON con los datos del estudiante específico

---

### 4. Actualizar Estudiante (`PUT /estudiantes/{id}`)

Modifica de forma completa la información del estudiante asociado al ID enviado en el parámetro.

![PUT Actualizar](img/PUT.png)

**Ejemplo:** `PUT /estudiantes/3`

**Cambios realizados:**
- Nombre: "Juan Pérez Editado"
- Correo: "juan@yahoo.com"

---

### 5. Eliminar Estudiante (`DELETE /estudiantes/{id}`)

Remueve de forma permanente de la base de datos el registro perteneciente al identificador proporcionado.

![DELETE Eliminar](img/DELETE.png)

**Ejemplo:** `DELETE /estudiantes/3`

**Respuesta:** `true` (confirmación de eliminación exitosa)

---

## 📝 Detalles Técnicos

### ¿Qué es una API?

Una **API** es básicamente un "contrato" entre el servidor y el cliente. Le permite al profesor (o a cualquiera) comunicarse con mi aplicación enviando peticiones HTTP y recibir datos en formato JSON.

### Operaciones CRUD

El proyecto implementa las 4 operaciones básicas:

| Operación | Verbo HTTP | Qué hace |
|---|---|---|
| **Crear** | `POST` | Agregar un nuevo estudiante |
| **Leer** | `GET` | Obtener datos de estudiantes |
| **Actualizar** | `PUT` | Modificar un estudiante existente |
| **Eliminar** | `DELETE` | Borrar un estudiante |

### Por que SQLite

- **Fácil de usar:** No necesita un servidor externo
- **Portátil:** Todo está en un solo archivo `.db`
- **Perfecto para proyectos pequeños:** Rápido y sin complicaciones

### Seguridad: Prevención de SQL Injection

En el archivo `crud.py` usé consultas parametrizadas para evitar ataques:

```python
cursor.execute("SELECT * FROM estudiantes WHERE id = ?", (estudiante_id,))
```

De esta forma, la base de datos trata la entrada como datos, nunca como codigo SQL.

---

## ✅ Lo que Incluye

✔️ 5 endpoints funcionales (POST, GET, GET por ID, PUT, DELETE)  
✔️ Base de datos SQLite integrada  
✔️ Validación de datos con Pydantic  
✔️ Consultas seguras (sin SQL Injection)  
✔️ Capturas de prueba en Postman  

---

## 📷 Pruebas Realizadas

Todas las operaciones fueron probadas en **Postman** y estan documentadas con capturas en la seccion de **Evidencias**.