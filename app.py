from fastapi import FastAPI
from routers import estudiantes


app = FastAPI(title="API Programacion2")

app.include_router(estudiantes.router)




        
    
    
    
        

    
    
    
