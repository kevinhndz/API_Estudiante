from pydantic import BaseModel, Field

# Aplica para POST y PUT 
class Revision(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    cuenta: str = Field(min_length=3, max_length=30)
    carrera: str = Field(min_length=3, max_length=100)
    telefono: str = Field(min_length=7, max_length=15)  
    correo: str = Field(min_length=5, max_length=120)
    edad: int = Field(ge=17, le=35)
    estado_civil : str = Field(min_length=6, max_length = 10)


# Para PATCH
class RevisonEditada(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=100)
    cuenta: str | None = Field(default=None, min_length=3, max_length=30)
    carrera: str | None = Field(default=None, min_length=3, max_length=100)
    telefono: str | None = Field(default=None, min_length=7, max_length=15)  
    correo: str | None = Field(default=None, min_length=5, max_length=120)
    edad: int | None = Field(default=None, ge=15, le=100)
    estado_civil : str | None = Field(defualt = None,min_length = 6, max_length = 10)