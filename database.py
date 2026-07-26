# este archivo se encarga unicamente de se encarga únicamente de hablar con la base de datos 
# (guardar, leer, borrar en el disco duro)

import sqlite3

# guarda el nombre del archivo de la base de datos
DB_NAME = "estudiantes.db" 

#abre la puerta a la base de datos OJO : (Se manda a llamar cada vez que se necesite hacer un CRUD)
def obtener_conexion():
    conexion = sqlite3.connect(DB_NAME)
    conexion.row_factory = sqlite3.Row
    return conexion


# creamos la tabla llamada estudiates
def crear_tabla():
    with obtener_conexion() as conexion: # esta linea asegura de abrir - procesar- cerrar la bd
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