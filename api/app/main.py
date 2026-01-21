from fastapi import FastAPI
from app.db import Base, engine
from app.routers.pacientes import router as pacientes_router
from app.routers.agendamentos import router as agendamentos_router
from app.routers.profissionais import router as profissionais_router
from app.routers.medicamentos import router as medicamentos_router

app = FastAPI(
    title="Clinic API",
    version="1.0.0",
    description="API para gerenciamento de clínica",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  
        "docExpansion": "none",           
        "filter": True,                   
        "tryItOutEnabled": False,        
        "displayRequestDuration": True
    }
)

Base.metadata.create_all(bind=engine)

app.include_router(pacientes_router)
app.include_router(agendamentos_router)
app.include_router(profissionais_router)
app.include_router(medicamentos_router)

@app.get(
    "/health",
    tags=["Sistema"],
    summary="Status da API",
    description="Verifica se a aplicação está online"
)
def health():
    return {"status": "ok"}
