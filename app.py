from fastapi import FastAPI
from routers import carreras, estudiantes


app = FastAPI(title="API Programacion2")

app.include_router(estudiantes.router)
app.include_router(carreras.router)




        
    
    
    
        

    
    
    
