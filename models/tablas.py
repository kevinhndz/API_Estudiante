from sqlalchemy import Column,Integer, String, ForeignKey
from models.almacen import MiClaseBase


class TablaEstudiantes(MiClaseBase):
    __tablename__ = "Tabla Estudiantes"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    cuenta = Column(String, unique = True)
    carrera = Column(Integer, ForeignKey('Tabla Carreras.id'))
    telefono = Column(String)
    correo= Column(String, unique=True)
    edad = Column(Integer)
    estado_civil = Column(String, nullable = True)   #nullable=True le indica a la base de datos que el campo acepta valores vacios o nulos.
    
    
class TablaCarreras (MiClaseBase):
    __tablename__ = "Tabla Carreras"
    
    id = Column(Integer, primary_key=True)
    nombre_carrera = Column(String, unique = True)
    