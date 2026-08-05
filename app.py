from fastapi import FastAPI , Depends, HTTPException,status
from sqlalchemy.orm import Session

# importanciones de mis archivos

from almacen import motor, MiClaseBase,abrir_puerta_bd # mi motor, platnilla, mi conexion
from tablas import TablaEstudiantes # la tablas (s)
from filtro_seguridad import Revision, RevisonEditada # el guardia de seguridad pydantic


app = FastAPI()



# ----- CRUD DE ESTUDIANTES ------------------


#------CREAR UN NUEVO ESTUDIANTE--------

@app.post('/estudiantes')
def crear_nuevo_estudiante(
    json_de_url: Revision, 
    base_datos: Session = Depends(abrir_puerta_bd)
):
    datos_enviados = base_datos.query(TablaEstudiantes).filter(TablaEstudiantes.cuenta == json_de_url.cuenta).first()
    
    if datos_enviados is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El estudiante con esta cuenta ya existe."
        )
    else:
        # Capturar y guardar los datos enviados
        datos_capturados = TablaEstudiantes(
            nombre=json_de_url.nombre,
            cuenta=json_de_url.cuenta,
            carrera=json_de_url.carrera,
            telefono=json_de_url.telefono,
            correo=json_de_url.correo,
            edad=json_de_url.edad,
            estado_civil = json_de_url.estado_civil
        )
        
        base_datos.add(datos_capturados)
        base_datos.commit()
        base_datos.refresh(datos_capturados)
        
        return  f"{json_de_url.nombre} ha sido registrado con exito!"
    
#------VER TODOS LOS ESTUDIANTES--------
@app.get('/estudiantes')
def ver_todos(base_datos: Session = Depends(abrir_puerta_bd)):
    return base_datos.query(TablaEstudiantes).all()


#-----VER ESTUDIANTE POR :*  ID * --------

@app.get('/estudiantes/{id}')
def ver_estudiante_por_id(
    
    id: int,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    
    id_enviado = base_datos.query(TablaEstudiantes).filter(TablaEstudiantes.id== id).first()
    
    if id_enviado is not None:
        raise HTTPException(
            status = status.HTTP_404_NOT_FOUND,
            detail = f"Error! El Numero de cuenta : {id} no ha sido encontrado en el sistema"
        )
    else:
         return base_datos.query(TablaEstudiantes).get(id)
   


#------EDITAR UN ESTUDIANTE--------
@app.put('/estudiantes/{id}')
def actualizar_registro(
     id: int,
     json_corregio: Revision,
     base_datos: Session = Depends(abrir_puerta_bd)
    
):
    #Primero traemos el registro a editar y lo guardamos en datos_actuales
    datos_actuales = base_datos.query(TablaEstudiantes).get(id)
    
    #cambiamos los valores
    datos_actuales.nombre = json_corregio.nombre
    datos_actuales.cuenta = json_corregio.cuenta
    datos_actuales.carrera = json_corregio.carrera
    datos_actuales.telefono = json_corregio.telefono
    datos_actuales.correo = json_corregio.correo
    datos_actuales.edad = json_corregio.edad
    datos_actuales.estado_civil = json_corregio.estado_civil
    base_datos.commit()
    base_datos.refresh(datos_actuales)
    return datos_actuales



#------ELIMINAR UN ESTUDIANTE POR *ID* --------
@app.delete('/estudiantes/{id}')
def eliminar_estudiante(
    
    id:int,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    caja_a_borrar = base_datos.query(TablaEstudiantes).get(id)
    base_datos.delete(caja_a_borrar)
    base_datos.commit()
    return {"mensaje": f"Estudiante con ID: {id} eliminado con exito! "}


#------CAMBIAR UN CAMPO DE UN ESTUDIANTE POR *ID*--------
@app.patch('/estudiantes/{id}')
def editar_un_campo(
    id: int,
    json_enviado: RevisonEditada,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    caja_actual = base_datos.query(TablaEstudiantes).get(id)
    
    # 1. Seguridad por si el registro no existe
    if caja_actual is None:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: Usuario con numero de id: {id} no ha sido encontrado"
        )
    
    if json_enviado.nombre is not None:
        caja_actual.nombre = json_enviado.nombre
    
    if json_enviado.cuenta is not None:
        caja_actual.cuenta = json_enviado.cuenta
        
    if json_enviado.carrera is not None:
        caja_actual.carrera = json_enviado.carrera
        
    if json_enviado.telefono is not None:
        caja_actual.telefono = json_enviado.telefono
    
    if json_enviado.correo is not None:
        caja_actual.correo = json_enviado.correo
    
    if json_enviado.edad is not None:
        caja_actual.edad = json_enviado.edad
    
    if json_enviado.estado_civil is not None:
        caja_actual.estado_civil = json_enviado.estado_civil

    base_datos.commit()
    base_datos.refresh(caja_actual)  
    
    return caja_actual


    #-------- Retos adicionales ---------
    
    
    #------VER UN ESTUDIANTE POR NUMERO DE CUENTA--------
@app.get('/estudiantes/cuenta/{cuenta}')
def filtrar_por_cuenta(
    
    cuenta: str,
    base_datos: Session = Depends(abrir_puerta_bd)
    
):
    cuenta_a_buscar = base_datos.query(TablaEstudiantes).filter(TablaEstudiantes.cuenta == cuenta).first()
    
    # Si el estudiante SI tiene informacion (no es None)
    if cuenta_a_buscar is not None:
        return cuenta_a_buscar
       
    else:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error: Usuario con número de cuenta: {cuenta} no ha sido encontrado"
        )
        

 #------VER UN ESTUDIANTE POR CARRERA--------

@app.get("/estudiantes/carrera/{carrera}")
def filtrar_por_carrera(
    carrera: str,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    inscritos_en_esa_carrera = base_datos.query(TablaEstudiantes).filter(TablaEstudiantes.carrera.ilike(f"%{carrera}%")).all()
    

    
    if not inscritos_en_esa_carrera:  # esta la lista vacia?
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"No hay estudiantes registrados para la carrera: {carrera}"
        )
    else:
        return inscritos_en_esa_carrera
    
    
    #------ELIMINAR UN ESTUDIANTE POR CARRERA-------- 
@app.delete("/estudiantes/carrera/eliminar/{carrera}")
def eliminar_por_carrera(
    carrera: str,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    carrera_enviada = base_datos.query(TablaEstudiantes).filter(TablaEstudiantes.carrera.ilike(f"%{carrera}%")).all()
    
    if not carrera_enviada:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = f"La carrera {carrera} no se encontro en la base de datos"
        )
    else:
        contador = 0
        for student in carrera_enviada:
            contador += 1
            base_datos.delete(student)
        
        
        base_datos.commit()
        return {"mensaje": f"Se elimnaron {contador} estudiantes de la carrera de: {carrera}"}
    
        
    
    
    
        

    
    
    
