from fastapi import FastAPI, HTTPException, status
from models.database import crear_tablas
from models.schemas import EntradaEstudiante, SalidaEstudiante, EntradaMaterial, SalidaMaterial
from models.crud import (
    crear_estudiante_db, obtener_estudiante_por_id_db, obtener_estudiantes_db, actualizar_estudiante_db, eliminar_estudiante_db,
    crear_material_db, obtener_material_por_id_db, obtener_materiales_db, actualizar_material_db, eliminar_material_db
)

app = FastAPI()

crear_tablas()

# ==========================================
# --- RUTAS DE LA API (ESTUDIANTES) ---
# ==========================================

@app.post("/estudiantes", response_model=SalidaEstudiante, status_code=status.HTTP_201_CREATED)
def crear_estudiante(estudiante: EntradaEstudiante):
    resultado = crear_estudiante_db(estudiante)
    if resultado == "duplicado":
        raise HTTPException(status_code=409, detail="La cuenta o correo ya estan registrados en el sistema")
    return resultado

@app.get("/estudiantes", response_model=list[SalidaEstudiante])
def obtener_estudiantes():
    return obtener_estudiantes_db()

@app.get("/estudiantes/{estudiante_id}", response_model=SalidaEstudiante)
def obtener_estudiante(estudiante_id: int):
    estudiante = obtener_estudiante_por_id_db(estudiante_id)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante

@app.put("/estudiantes/{estudiante_id}", response_model=SalidaEstudiante)
def actualizar_estudiante(estudiante_id: int, estudiante: EntradaEstudiante):
    resultado = actualizar_estudiante_db(estudiante_id, estudiante)
    if resultado == "duplicado":
        raise HTTPException(status_code=409, detail="La cuenta o correo ya estan ocupados por otro estudiante")
    if not resultado:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return resultado

@app.delete("/estudiantes/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int):
    exito = eliminar_estudiante_db(estudiante_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return {"mensaje": "Estudiante eliminado correctamente"}


# ==========================================
# --- RUTAS DE LA API (MATERIALES - RETO) ---
# ==========================================

@app.post("/materiales", response_model=SalidaMaterial, status_code=status.HTTP_201_CREATED)
def crear_material(material: EntradaMaterial):
    resultado = crear_material_db(material)
    if resultado == "duplicado":
        raise HTTPException(status_code=409, detail="El codigo SKU ya esta registrado")
    return resultado

@app.get("/materiales", response_model=list[SalidaMaterial])
def obtener_materiales():
    return obtener_materiales_db()

@app.get("/materiales/{material_id}", response_model=SalidaMaterial)
def obtener_material(material_id: int):
    material = obtener_material_por_id_db(material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return material

@app.put("/materiales/{material_id}", response_model=SalidaMaterial)
def actualizar_material(material_id: int, material: EntradaMaterial):
    resultado = actualizar_material_db(material_id, material)
    if resultado == "duplicado":
        raise HTTPException(status_code=409, detail="El codigo SKU ya pertenece a otro material")
    if not resultado:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return resultado

@app.delete("/materiales/{material_id}")
def eliminar_material(material_id: int):
    exito = eliminar_material_db(material_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return {"mensaje": "Material eliminado correctamente"}