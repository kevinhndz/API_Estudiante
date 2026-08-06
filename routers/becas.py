from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from models.almacen import MiClaseBase, motor,abrir_puerta_bd
from models.filtro_seguridad import RevisarBecas
from models.tablas import Becas
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/becas",
    tags = ["Becas"]
 
)


@router.get("/")
def ver_becas_disponibles(
    base_datos: Session = Depends(abrir_puerta_bd)
):
    consultar_becas = base_datos.query(Becas).all()
    contador = 0
    
    if not consultar_becas:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "No hay becas registradas aun!"
        )
    else:
        for beca in consultar_becas:
            contador+=1
        
        return {  "Aviso": f"Se encontraron {contador} becas en el sistema",
                  "Becas": consultar_becas
                }
            
            
@router.post("/")
def crear_beca(
    
    json: RevisarBecas,
    base_datos: Session = Depends(abrir_puerta_bd)
    
):
    check_beca = base_datos.query(Becas).filter(Becas.tipo_beca.ilike(f"%{json.tipo_beca}%")).first()
    
    if check_beca is None:
        
        new_data = Becas(
             
              tipo_beca = json.tipo_beca,
              porcentaje_descuento = json.porcentaje_descuento,
              duracion = json.duracion  
        )
        
        base_datos.add(new_data)
        base_datos.commit()
        base_datos.refresh(new_data)
        return {
    "Mensaje": f"{json.tipo_beca} creada con exito!",
    "id": new_data.id  
}
    else:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"{json.tipo_beca} ya se encuentra registrada"
        )
        
    
    