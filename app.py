from fastapi import FastAPI
from routers import becas


app = FastAPI(title="API Programacion2")

app.include_router(becas.router)





        
    
    
    
        

    
    
    
