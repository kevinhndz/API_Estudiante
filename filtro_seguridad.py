from pydantic import BaseModel

# POST, PUT   -> 1 CLASS, PATCH  -> 1 UNIQUE CLASS ya que pydantic solamente revisa esos 3 https


#aplica para post y put 
class Revision(BaseModel):
    nombre: str
    cuenta: str
    correo: str
    edad: int


class RevisonEditada(BaseModel):
    nombre: str | None = None
    cuenta: str | None = None
    correo: str | None = None
    edad: int | None = None
    

