from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.almacen import abrir_puerta_bd
from models.tablas import TablaEstudiantes
from models.filtro_seguridad import Revision, RevisonEditada


router = APIRouter(
    prefix="/estudiantes",   
    # ahora no hay que escribir /estudiantes ya que este archivo.py solo es para eso
    tags=["Estudiantes"]     
    # usamos esta lista para que la instancia de FASTAPI la tome
)
# ----- CRUD DE ESTUDIANTES ------------------


#------CREAR UN NUEVO ESTUDIANTE--------
#antes de porbar este endpoint aunque se mande 1 estudiante tiene que mandarse en forma de lista, sino va dar error

@router.post('/')
def crear_nuevo_estudiante(
    json_de_url: List[Revision], 
    base_datos: Session = Depends(abrir_puerta_bd)
):
    numero_estuidantes = 0
    for json in json_de_url:
        datos_enviados = base_datos.query(TablaEstudiantes).filter(TablaEstudiantes.cuenta == json.cuenta).first()
        numero_estuidantes = numero_estuidantes + 1
        
        if datos_enviados is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El estudiante con la cuenta {json.cuenta} ya existe."
            )
        else:
        
            datos_capturados = TablaEstudiantes(
                nombre=json.nombre,
                cuenta=json.cuenta,
                carrera=json.carrera,
                telefono=json.telefono,
                correo=json.correo,
                edad=json.edad,
                estado_civil = json.estado_civil
            )
            
            base_datos.add(datos_capturados)
    
    base_datos.commit()
    
    return f"PSDTA: Se han registrado {numero_estuidantes} estuidante(s) con exito!"
    
#------VER TODOS LOS ESTUDIANTES--------
@router.get('/')
def ver_todos(base_datos: Session = Depends(abrir_puerta_bd)):
    consultemos_primero = base_datos.query(TablaEstudiantes).all()
    if not consultemos_primero:
        raise HTTPException(
            status_code = status.HTTP_405_METHOD_NOT_ALLOWED,
            detail = f"No hay estudiantes registrados aun!"
        )
    else:
        lo_que_hay = base_datos.query(TablaEstudiantes).all()
        quantity = 0
        for student in lo_que_hay:
            quantity+=1
        return {
        "mensaje": f"Se encontraron {quantity} estudiantes en la base de d",
        "estudiantes": lo_que_hay
    }
            
    


#-----VER ESTUDIANTE POR :* ID * --------

@router.get('/{id}')
def ver_estudiante_por_id(
    
    id: int,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    
    id_enviado = base_datos.query(TablaEstudiantes).filter(TablaEstudiantes.id== id).first()
    
    if id_enviado is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Error! El Numero de cuenta : {id} no ha sido encontrado en el sistema"
        )
    else:
         return base_datos.query(TablaEstudiantes).get(id)
   


#------EDITAR UN ESTUDIANTE--------
@router.put('/{id}')
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
@router.delete('/{id}')
def eliminar_estudiante(
    
    id:int,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    caja_a_borrar = base_datos.query(TablaEstudiantes).get(id)
    base_datos.delete(caja_a_borrar)
    base_datos.commit()
    return {"mensaje": f"Estudiante con ID: {id} eliminado con exito! "}


#------CAMBIAR UN CAMPO DE UN ESTUDIANTE POR *ID*--------
@router.patch('/{id}')
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
@router.get('/cuenta/{cuenta}')
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

@router.get("/carrera/{carrera}")
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
    
    
    #------ELIMINAR A TODOS LOS ESTUDIANTES DE LA CARRERA INGRESADA -------- 
@router.delete("/carrera/eliminar/{carrera}")
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
    