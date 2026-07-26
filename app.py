from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session

# importanciones de mis archivos

from almacen import motor, MiClaseBase,abrir_puerta_bd # mi motor, platnilla, mi conexion
from tablas import TablaEstudiantes # la tablas (s)
from filtro_seguridad import Revision, RevisonEditada # el guardia de seguridad pydantic


app = FastAPI()

# crear la base de datos por si no existe
MiClaseBase.metadata.create_all(bind = motor)


#metodo post

@app.post('/estudiantes')
def crear_nuevo_estudiante(
    json_de_url: Revision, 
    base_datos: Session = Depends(abrir_puerta_bd)
    
    ):
    
    # capturar esos datos json
    #cuenta correo edad
    datos_capturados = TablaEstudiantes(
        
        nombre = json_de_url.nombre,
        cuenta = json_de_url.cuenta,
        correo = json_de_url.correo,
        edad = json_de_url.edad
        
    )
    
    # una vez capturados necesito guardar esos datos en algun lugar
    
    base_datos.add(datos_capturados)
    base_datos.commit()
    base_datos.refresh(datos_capturados)
    return datos_capturados
    
# metodo get
@app.get('/estudiantes')
def ver_todos(base_datos: Session = Depends(abrir_puerta_bd)):
    return base_datos.query(TablaEstudiantes).all()

#metodo get, pero filtrado con ruta dinamica

@app.get('/estudiantes/{id}')
def ver_estudiante_por_id(
    
    id: int,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    return base_datos.query(TablaEstudiantes).get(id)




