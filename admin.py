import sqlite3

#para no perder los datos ya registrados admin.py es el administrador, para no instalar un gestor
# al agregar la columna Telefonos SQL asigna NULL a cada registro

conexion = sqlite3.connect("base_datos.db")
cursor = conexion.cursor()

try:

    cursor.execute('ALTER TABLE "Tabla Estudiantes" ADD COLUMN telefono VARCHAR;')
    conexion.commit()
    print("Columna agregada")
except sqlite3.OperationalError as e:
    print(f"OJO: No se pudo agregar la columna (puede que ya exista): {e}")
finally:
   
    conexion.close()