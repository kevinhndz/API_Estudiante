from fastapi import FastAPI, APIRouter,HTTPException, status, Depends
from models.almacen import  motor, MiClaseBase, abrir_puerta_bd
from models.filtro_seguridad import Revision, RevisionClase, RevisonEditada
from models.tablas import TablaCarreras, TablaEstudiantes
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = "/carreras",
    tags = ["Carreras"]
)

@router.post("/")
def registar_carrera(
    json_recibido: RevisionClase,
    base_datos: Session = Depends(abrir_puerta_bd)
):
    datos_extraidos = base_datos.query(TablaCarreras).filter(TablaCarreras.nombre == json_recibido.nombre).first()
    
    if datos_extraidos is None:
        new_data = TablaCarreras(
            nombre = json_recibido.nombre,
            duracion = json_recibido.duracion,
            cantidad = json_recibido.cantidad
        )
        base_datos.add(new_data)
        base_datos.commit()
        base_datos.refresh(new_data)
        return f" Se registro la carrera de {json_recibido.nombre} con exito!"
    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"La carrera {json_recibido.nombre} ya esta registrada.."
        )
    
        
    
    
