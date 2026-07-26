from pydantic import BaseModel, Field

# POST, PUT   -> 1 CLASS, PATCH  -> 1 UNIQUE CLASS ya que pydantic solamente revisa esos 3 https


#aplica para post y put 
class Revision(BaseModel):
    nombre: str = Field(min_length=3,max_length=100)
    cuenta: str = Field(min_length=3,max_length=30)
    carrera: str = Field(min_length=3, max_length=100)
    correo: str = Field(min_length=5,max_length=120)
    edad: int = Field(ge=15, le=100)
 

# para patch
class RevisonEditada(BaseModel):
    nombre: str | None = None
    cuenta: str | None = None
    carrera: str | None = None
    correo: str | None = None
    edad: int | None = None
    

