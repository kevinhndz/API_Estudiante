from sqlalchemy import Column,Integer, String
from almacen import MiClaseBase


class TablaEstudiantes(MiClaseBase):
    __tablename__ = "Tabla Estudiantes"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cuenta = Column(String, unique = True)
    correo= Column(String, unique=True)
    edad = Column(Integer)
    
    
    