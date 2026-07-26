import sqlite3
from database import DB_NAME
from schemas import EntradaEstudiante

def crear_estudiante_db(estudiante: EntradaEstudiante):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    query = "INSERT INTO estudiantes (nombre, cuenta, carrera, correo, edad) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (estudiante.nombre, estudiante.cuenta, estudiante.carrera, estudiante.correo, estudiante.edad))
    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return {
        "id": nuevo_id,
        "nombre": estudiante.nombre,
        "cuenta": estudiante.cuenta,
        "carrera": estudiante.carrera,
        "correo": estudiante.correo,
        "edad": estudiante.edad
    }

def obtener_estudiantes_db():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, cuenta, carrera, correo, edad FROM estudiantes")
    filas = cursor.fetchall()
    conexion.close()
    lista_estudiantes = []
    for fila in filas:
        estudiante_diccionario = {
            "id": fila[0],
            "nombre": fila[1],
            "cuenta": fila[2],
            "carrera": fila[3],
            "correo": fila[4],
            "edad": fila[5]
        }
        lista_estudiantes.append(estudiante_diccionario)
    return lista_estudiantes

def obtener_estudiante_por_id_db(estudiante_id: int):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, cuenta, carrera, correo, edad FROM estudiantes WHERE id = ?", (estudiante_id,))
    fila = cursor.fetchone()
    conexion.close()
    if fila is None:
        return None
    return {
        "id": fila[0],
        "nombre": fila[1],
        "cuenta": fila[2],
        "carrera": fila[3],
        "correo": fila[4],
        "edad": fila[5]
    }

def actualizar_estudiante_db(estudiante_id: int, estudiante: EntradaEstudiante):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    query = "UPDATE estudiantes SET nombre = ?, cuenta = ?, carrera = ?, correo = ?, edad = ? WHERE id = ?"
    cursor.execute(query, (estudiante.nombre, estudiante.cuenta, estudiante.carrera, estudiante.correo, estudiante.edad, estudiante_id))
    conexion.commit()
    filas_modificadas = cursor.rowcount
    conexion.close()
    if filas_modificadas == 0:
        return None
    return {
        "id": estudiante_id,
        "nombre": estudiante.nombre,
        "cuenta": estudiante.cuenta,
        "carrera": estudiante.carrera,
        "correo": estudiante.correo,
        "edad": estudiante.edad
    }

def eliminar_estudiante_db(estudiante_id: int):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM estudiantes WHERE id = ?", (estudiante_id,))
    conexion.commit()
    filas_borradas = cursor.rowcount
    conexion.close()
    if filas_borradas > 0:
        return True
    else:
        return False