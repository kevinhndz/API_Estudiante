import sqlite3
import os

os.makedirs("datos_sqlite", exist_ok=True)

DB_NAME = "datos_sqlite/estudiantes.db" 

def obtener_conexion():
    conexion = sqlite3.connect(DB_NAME)
    conexion.row_factory = sqlite3.Row
    return conexion

def crear_tablas():
    with obtener_conexion() as conexion:
        # Tabla de estudiantes original
        conexion.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cuenta TEXT NOT NULL UNIQUE,
            carrera TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            edad INTEGER NOT NULL
        )
        """)
        
        conexion.execute("""
        CREATE TABLE IF NOT EXISTS materiales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            codigo_sku TEXT NOT NULL UNIQUE,
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL
        )
        """)