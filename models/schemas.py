from pydantic import BaseModel, Field

# --- ESQUEMAS ESTUDIANTES ---
class DatosEstudiante(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    cuenta: str = Field(min_length=3, max_length=30)
    carrera: str = Field(min_length=2, max_length=100)
    correo: str = Field(min_length=5, max_length=120)
    edad: int = Field(ge=15, le=100)

class EntradaEstudiante(DatosEstudiante):
    pass

class SalidaEstudiante(DatosEstudiante):
    id: int

# --- ESQUEMAS MATERIALES (RETO) ---
class DatosMaterial(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    codigo_sku: str = Field(min_length=3, max_length=20)
    categoria: str = Field(min_length=3, max_length=50)
    cantidad: int = Field(ge=0)

class EntradaMaterial(DatosMaterial):
    pass

class SalidaMaterial(DatosMaterial):
    id: int