from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, ForeignKey, Column, Float


class Estudiantes(DeclarativeBase):
    __tablename__ = "Estudiantes"
    
    id = Column(Integer,primary_key = True)
    nombre = Column(String)
    telefono = Column(String)
    cuenta = Column(String, unique= True)
    correo = Column(String, unique= True)
    direccion = Column (String)
    estado_civil = Column(String)
    edad = Column (Integer)
    modalidad = Column(String)
    id_beca = Column(Integer, ForeignKey("Becas.id"))
    id_carrera = Column(Integer, ForeignKey("Carreras.id"))
    id_usuario = Column(Integer, ForeignKey("Usuarios.id"))
    
    

class Profesores(DeclarativeBase):
    __tablename__ = "Profesores"
    
    id = Column(Integer,primary_key = True)
    nombre = Column(String)
    telefono = Column(String)
    correo = Column(String, unique= True)
    direccion = Column (String)
    estado_civil = Column(String)
    edad = Column (Integer)
    modalidad = Column(String)
    codigo_empleado = Column(String , unique= True)
    salario = Column(Float)
    id_usuario = Column(Integer, ForeignKey("Usuarios.id"))
    
    

class Carreras(DeclarativeBase):
    __tablename__ = "Carreras"
    
    id = Column(Integer, primary_key = True)
    nombre = Column (String)
    duracion = Column(String)
    cantidad_clases = Column (Integer)
    
class Usuarios(DeclarativeBase):
    __tablename__ = "Usuarios"
    
    id = Column(Integer, primary_key = True)
    user = Column(String)
    password = Column(String)
    rol = Column(String)
    
    
class Becas(DeclarativeBase):
    __tablename__ = "Becas"
    
    id = Column(Integer, primary_key = True)
    tipo_beca = Column(String)
    porcentaje_descuento = Column(Float)
    duracion = Column(Integer)
    
    
class Clases(DeclarativeBase):
    __tablename__ = "Clases"
    
    id = Column(Integer, primary_key = True)
    nombre = Column (String)
    creditos = Column(Integer)
    codigo = Column(String)
    modalidad = Column(String)
    dia = Column(String)
    horario = Column(String)

class RecursosHumanos(DeclarativeBase):
    __tablename__ = "RRHH"
    
    id = Column(Integer,primary_key = True)
    nombre = Column(String)
    telefono = Column(String)
    correo = Column(String, unique= True)
    direccion = Column (String)
    codigo_empleado = Column(Integer, unique= True)
    id_usuario = Column(Integer, ForeignKey("Usuarios.id"))
    
    
class Nomina(DeclarativeBase):
    __tablename__ = "Nomina"
    
    id = Column(Integer, primary_key = True)
    id_profesor = Column(Integer, ForeignKey("Profesores.id"))
    idHr = Column(Integer,ForeignKey("RRHH.id") )


class Seguros(DeclarativeBase):
    
    __tablename__ = "Seguros"
        
    id = Column(Integer, primary_key = True)
    tipo_seguro = Column(String)
    porcentaje_descuento = Column(Float)
    contrato = Column(String)
    
    
# ----- CLUSTERS DE INTERSECCIONES MUCHOS A MUCHOS -------

class Insc_Estudiante_Clase(DeclarativeBase):
    ___tablename__ = "Inscripcion_Estudiante_Clase"
    
    id = Column(Integer, primary_key= True)
    id_estudiante = Column(Integer, ForeignKey("Estudiantes.id"))
    id_clase = Column(Integer, ForeignKey("Clases.id"))

class Insc_Profesor_Clase(DeclarativeBase):
    ___tablename__ = "Inscripcion_Profesor_Clase"
    
    id = Column(Integer, primary_key= True)
    id_profesor = Column(Integer, ForeignKey("Profesores.id"))
    id_clase = Column(Integer, ForeignKey("Clases.id"))


class Insc_Profesor_Carrera(DeclarativeBase):
    ___tablename__ = "Inscripcion_Profesor_Carrera"
    
    id = Column(Integer, primary_key= True)
    id_profesor = Column(Integer, ForeignKey("Profesores.id"))
    id_carrea = Column(Integer, ForeignKey("Carreras.id"))
    
class Insc_Profesor_Carrera(DeclarativeBase):
    ___tablename__ = "Inscripcion_Profesor_Seguro"
    
    id = Column(Integer, primary_key= True)
    id_profesor = Column(Integer, ForeignKey("Profesores.id"))
    id_seguro = Column(Integer, ForeignKey("Seguros.id"))
    
    

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    