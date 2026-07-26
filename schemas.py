from pydantic import BaseModel, Field

# Datos generales
class DatosEstudiante(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    cuenta: str = Field(min_length=3, max_length=30)
    carrera: str = Field(min_length=2, max_length=100)
    correo: str = Field(min_length=5, max_length=120)
    edad: int = Field(ge=15, le=100)

# Lo que entra (sin ID)
class EntradaEstudiante(DatosEstudiante):
    pass

# Lo que sale (con ID)
class SalidaEstudiante(DatosEstudiante):
    id: int









"""

BaseModel: Es la "clase padre" o plantilla general de Pydantic que nos permite
definir que datos va a recibir o devolver nuestra API.

Field: Es una funcion que sirve para poner reglas de validacion y limites a cada campo 
(por ejemplo: tamaño minimo de texto, numero minimo, etc.)

"""