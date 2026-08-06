from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()



DATABASE_URL = os.getenv("DATABASE_URL")

# enciendo la conexion
motor = create_engine(DATABASE_URL)
# creo eventos temporales para abrir la base de datos las llaves fisicas
FabricaLlaves = sessionmaker(bind=motor)
#darle superpoderes a mis clases para que puedan manifestarse como tablas
MiClaseBase = declarative_base()


# creando la conexion unica que se reparte en recepcion.py

def abrir_puerta_bd():
    base_datos = FabricaLlaves() # le doy las llaves fisicas a la variable base_datos  para poder abrir y cerrar
    
    try: # entrega la sesion activa al endpoint
        yield base_datos
    finally:
        base_datos.close()  # cierra la sesion de un solo
    


