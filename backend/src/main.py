from fastapi import FastAPI
from backend.services.inventory_system.app.database import Base, engine
from backend.services.cards_service.src.api import router as cards_router

app = FastAPI()
from fastapi import FastAPI


app.include_router(cards_router, prefix="/cards_service", tags=["Cards Service"])

@app.get("/")
def root():
    return {"message": "API funcionando!"}

Base.metadata.create_all(bind=engine)

