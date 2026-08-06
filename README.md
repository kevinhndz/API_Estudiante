# 📚 API de Gestión Académica

Proyecto de API REST desarrollado en **FastAPI** + **PostgreSQL** (Supabase) para gestionar estudiantes, profesores, carreras y más.

---

## 🌿 Dos Versiones

### Rama `main` (Avanzada)
- Base de datos PostgreSQL en Supabase
- Múltiples tablas relacionadas , agregue mas tablas para jugar con los endpoints y hacerlo mas complejo y profesional.
- Migraciones con Alembic
- Ideal para aprender arquitectura profesional

### Rama `Version2` (Simple)
- Base de datos SQLite
- CRUD básico
- Ideal para aprender SQL puro

---

## 🚀 Instalación Rápida (Rama `main`)

### Paso 1: Descargar el repositorio

```bash
git clone https://github.com/kevinhndz/API_Estudiante.git
cd API_Estudiante
git checkout main
```

### Paso 2: Crear entorno virtual

```bash
python -m venv venv
```

Activar (Windows):
```bash
venv\Scripts\activate
```

Activar (Mac/Linux):
```bash
source venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```
 

**Este paso es diferente para cada persona porque cada uno necesita su propia base de datos.**

### 1. Ir a [supabase.com](https://supabase.com) y crea una cuenta gratuita
### 2. Crea un nuevo proyecto (toma ~2 minutos)


### 3. Presiona Connect
![GET Todos](img/paso1.png)


### 4. Elegir la opcion correcta

Asegurate que elijas la opcion Direct Connection String -> y de ahi -> Direct Connection
de ahi desliza un poco...

![GET Todos](img/paso2.png)

### 5. En el dashboard, copia la URL de conexion PostgreSQL

Si se fijan bien, hay una URL, ver en imagen. Copia eso, se ve algo asi:

postgres:TU_PASSWORD@db.TU_ID.supabase.co:5432/postgres

![GET Todos](img/paso3.png)



### 6.  En la raiz del proyecto clonado, crea un archivo `.env`:


```env
DATABASE_URL=postgresql://postgres:TU_PASSWORD@db.TU_ID.supabase.co:5432/postgres
```

Reemplaza:
- `TU_PASSWORD` = La contraseña que est
- `TU_ID` = El ID único de tu proyecto


### Paso 7: Crear las tablas en la BD

```bash
alembic revision --autogenerate -m "Crear tablas iniciales"
alembic upgrade head
```

### Paso 6: Ejecutar la API

```bash
uvicorn app:app --reload
```

🎉 **La API esta en:** `http://127.0.0.1:8000`

---

## 📂 Estructura del Proyecto

```
en proceso **
```

---

## 📖 Documentación Interactiva

Una vez que la API este corriendo, accede a:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

Ahi se ven TODOS los endpoints automaticamente.

---

## 🛠️ Herramientas Utilizadas

- **FastAPI** - Framework web
- **SQLAlchemy** - ORM para base de datos
- **PostgreSQL** - Base de datos
- **Supabase** - Hosting de PostgreSQL
- **Alembic** - Versionado de migraciones
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor

---

## ❓ Preguntas Frecuentes

### ¿Necesito Supabase?
**Sí, para rama `main`.** 

### ¿Puedo usar otra base de datos?
Sí, modifica el  `DATABASE_URL` en  el `.env`:

```env
# MySQL
DATABASE_URL=mysql+pymysql://usuario:password@localhost/dbname

# SQLite (local)
DATABASE_URL=sqlite:///./test.db
```

### ¿Cómo veo los datos en Supabase?
En el dashboard → Table Editor → Selecciona la tabla → Ves los datos en tiempo real.

### ¿Qué es Alembic?
Sistema de control de versiones para bases de datos. Trackea cambios en la estructura sin perder datos.
Es como un Github2.0 que vive en el codigo.

---

 
## 📝 Detalles Técnicos
 
### ¿Qué es SQLAlchemy?
 
SQLAlchemy es un ORM (Object-Relational Mapping). En lugar de escribir SQL directamente, defino mis tablas como clases de Python. Eso hace que el código sea más limpio y seguro.
 



## 📸 Primero, lo primero. Crear la base de datos (Aqui mi logica en papel)
- **Porque es necesario?:** Porque sin una estructura no se codea/ piensa bien.
- **Menos Errores:** Con una estructura , menos errores, mas rapido se trabaja.
- **Se recomineda:** . Se recomienda crear la base de Datos PRIMERO, antes de hacer una Rest API.


![ESTRUCTURA!](img/testingpic.jpg)


## 📸  Aqui , el schema hecho con Diagramas, mas visible!

![ESTRUCTURA!](img/dbpi.png)



## 📸 Mapa Mental de como se Mueven los Datos

![ESTRUCTURA!](img/STRUCTURE.png)
 

## 📸 Evidencias de Pruebas en Postman (CRUD) Solo con el modulo estudiantes 

A continuación se muestran las pruebas de funcionamiento enviadas a los endpoints con sus correspondientes códigos de estado HTTP (`200 OK`): 

PSDTA: Ya que estas en mi repositorio, y deseas correr esta API y probarla, puedes acceder a esta documentacion:
Solo necesitaras POSTAMAN y seguir las instrucciones de la documentacion.

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

![GET por ID](img/GETUNICO.png)

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



---
# Preguntas y Respuestas del Proyecto


### 1. ¿Cuál es la diferencia entre POST y PUT?

POST es para crear estudiantes nuevos. Cada vez que hago un POST, se crea un registro nuevo y el servidor le asigna un ID automático. PUT es para editar un estudiante que ya existe. Ahí tengo que meter el ID en la URL tipo `/estudiantes/3` para saber cuál voy a modificar.

---

### 2. ¿Por qué la cuenta y el correo se definieron como UNIQUE?

Porque la cuenta es como el número de cédula del estudiante, no puede haber dos iguales. Lo mismo con el correo, cada persona tiene uno diferente. Si alguien intenta crear un estudiante con una cuenta que ya existe, la base de datos rechaza el registro y tira error.

---

### 3. ¿Qué ventaja ofrece SQLite en una práctica de aprendizaje?

Porque SQLite no necesita un servidor aparte corriendo. Toda la BD está en un archivo que puedo llevar de un lado a otro. Es rápido para programas pequeños y para aprender. Si hago un proyecto grande en producción ya usaría PostgreSQL o MySQL, pero para esto SQLite está perfecto.

---

### 4. ¿Qué sucede si se envía una edad de 10 años? Explique el código recibido.

La idea era validar eso con Pydantic. Idealmente configuraría algo así para que solo acepte edades entre 17 y 80. Si se intenta mandar algo fuera de rango, la API devuelve error 422 diciendo que los datos no son válidos.

---

### 5. ¿Por qué no debe concatenarse directamente información del usuario en una consulta SQL?

Ese `?` es importante para la seguridad. Si concateno directo los datos del usuario en la consulta, un atacante puede hacer SQL Injection, que es inyectar código malicioso. Con el `?` la base de datos sabe que es un dato, no código. Así nadie puede meter un comando tipo `DROP TABLE` para borrar todo.

---

### 6. ¿Qué diferencia existe entre el Body superior y el inferior?

Lo que escribo en el Body antes de dar "Send" es lo que envío al servidor. Después el servidor me responde con otro Body. Generalmente me devuelve lo que envié más el ID que generó. Por ejemplo, si envío los datos de Carlos, me devuelve los mismos datos pero con `"id": 1`.

---

### 7. ¿Cuándo se utiliza POST y cuándo PUT?

POST es cuando creo un registro nuevo sin saber qué ID va a tener. La dirección es `/estudiantes` sin ID. PUT es cuando edito algo que ya existe y sé cuál es el ID, entonces voy a `/estudiantes/3` para editar el estudiante número 3.

---

### 8. ¿Qué significa 201 Created?

Es un código HTTP que devuelve el servidor. El 200 OK significa que salió bien pero no creó nada nuevo. El 201 Created significa que salió bien Y además se creó un recurso nuevo. Entonces cuando hago POST debería recibir 201, no 200.

---

### 9. ¿Por qué GET normalmente no necesita Body?

Porque GET es solo para pedir información, no para enviar datos nuevos. Los datos que necesito los meto en la URL, como `/estudiantes/3` o en parámetros como `?nombre=Carlos`. Como no estoy mandando mucho, no necesito Body. Si intentas mandar Body en un GET, el servidor lo ignora.

---

### 10. ¿Qué indica una respuesta 409?

El 409 Conflict aparece cuando intento crear algo que causa conflicto. En mi API, si intento crear un estudiante con una cuenta o correo que ya existe, recibo 409 porque viola el constraint UNIQUE que puse. Otros códigos que manejo son 400 (datos mal), 404 (no existe) y 500 (error del servidor).


## 👨‍💻 Autor

Kevin Hernández - [GitHub](https://github.com/kevinhndz)

---