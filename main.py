from fastapi import FastAPI
from database import crear_tabla
from schemas import EntradaEstudiante, SalidaEstudiante
import crud

# 1. Creamos la app
app = FastAPI()

# 2. Creamos la tabla si no existe
crear_tabla()


# --- RUTAS DE LA API ---

# 1. CREAR UN ESTUDIANTE (POST)
@app.post("/estudiantes")
def crear_estudiante(estudiante: EntradaEstudiante):
    return crud.crear_estudiante_db(estudiante)


# 2. VER TODOS LOS ESTUDIANTES (GET)
@app.get("/estudiantes")
def obtener_estudiantes():
    return crud.obtener_estudiantes_db()


# 3. VER UN ESTUDIANTE POR ID (GET)
@app.get("/estudiantes/{estudiante_id}")
def obtener_estudiante(estudiante_id: int):
    return crud.obtener_estudiante_por_id_db(estudiante_id)


# 4. ACTUALIZAR UN ESTUDIANTE (PUT)
@app.put("/estudiantes/{estudiante_id}")
def actualizar_estudiante(estudiante_id: int, estudiante: EntradaEstudiante):
    return crud.actualizar_estudiante_db(estudiante_id, estudiante)


# 5. ELIMINAR UN ESTUDIANTE (DELETE)
@app.delete("/estudiantes/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int):
    return crud.eliminar_estudiante_db(estudiante_id)