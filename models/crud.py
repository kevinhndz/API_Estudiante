import sqlite3
from models.database import obtener_conexion
from models.schemas import EntradaEstudiante, EntradaMaterial

# --- CRUD ESTUDIANTES ---

def crear_estudiante_db(estudiante: EntradaEstudiante):
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO estudiantes (nombre, cuenta, carrera, correo, edad) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, (estudiante.nombre, estudiante.cuenta, estudiante.carrera, estudiante.correo, estudiante.edad))
            conexion.commit()
            nuevo_id = cursor.lastrowid
            
            # Reutilizamos los datos de entrada y añadimos el ID
            respuesta = estudiante.model_dump()
            respuesta["id"] = nuevo_id
            return respuesta
    except sqlite3.IntegrityError:
        return "duplicado" # Esto nos ayudará a lanzar el error 409

def obtener_estudiantes_db():
    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        filas = cursor.fetchall()
        # Gracias a row_factory, podemos convertir la fila directo a dict
        return [dict(fila) for fila in filas]

def obtener_estudiante_por_id_db(estudiante_id: int):
    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estudiantes WHERE id = ?", (estudiante_id,))
        fila = cursor.fetchone()
        if fila:
            return dict(fila)
        return None

def actualizar_estudiante_db(estudiante_id: int, estudiante: EntradaEstudiante):
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            query = "UPDATE estudiantes SET nombre = ?, cuenta = ?, carrera = ?, correo = ?, edad = ? WHERE id = ?"
            cursor.execute(query, (estudiante.nombre, estudiante.cuenta, estudiante.carrera, estudiante.correo, estudiante.edad, estudiante_id))
            conexion.commit()
            
            if cursor.rowcount == 0:
                return None
            
            respuesta = estudiante.model_dump()
            respuesta["id"] = estudiante_id
            return respuesta
    except sqlite3.IntegrityError:
        return "duplicado"

def eliminar_estudiante_db(estudiante_id: int):
    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id = ?", (estudiante_id,))
        conexion.commit()
        return cursor.rowcount > 0


# --- CRUD MATERIALES (RETO) ---

def crear_material_db(material: EntradaMaterial):
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO materiales (nombre, codigo_sku, categoria, cantidad) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (material.nombre, material.codigo_sku, material.categoria, material.cantidad))
            conexion.commit()
            nuevo_id = cursor.lastrowid
            
            respuesta = material.model_dump()
            respuesta["id"] = nuevo_id
            return respuesta
    except sqlite3.IntegrityError:
        return "duplicado"

def obtener_materiales_db():
    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materiales")
        filas = cursor.fetchall()
        return [dict(fila) for fila in filas]

def obtener_material_por_id_db(material_id: int):
    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materiales WHERE id = ?", (material_id,))
        fila = cursor.fetchone()
        return dict(fila) if fila else None

def actualizar_material_db(material_id: int, material: EntradaMaterial):
    try:
        with obtener_conexion() as conexion:
            cursor = conexion.cursor()
            query = "UPDATE materiales SET nombre = ?, codigo_sku = ?, categoria = ?, cantidad = ? WHERE id = ?"
            cursor.execute(query, (material.nombre, material.codigo_sku, material.categoria, material.cantidad, material_id))
            conexion.commit()
            
            if cursor.rowcount == 0:
                return None
            
            respuesta = material.model_dump()
            respuesta["id"] = material_id
            return respuesta
    except sqlite3.IntegrityError:
        return "duplicado"

def eliminar_material_db(material_id: int):
    with obtener_conexion() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM materiales WHERE id = ?", (material_id,))
        conexion.commit()
        return cursor.rowcount > 0