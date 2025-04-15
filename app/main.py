# app/main.py
from fastapi import FastAPI
from app.controllers import usuario_controller
from app.database import engine, Base
import app.models  # Se asegura de que todos los modelos se importen para la creación de tablas

# Crear las tablas en la base de datos PostgreSQL
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Proyecto Backend con FastAPI")

# Incluir el router de usuario con el prefijo /usuarios
app.include_router(usuario_controller.router, prefix="/usuarios", tags=["Usuarios"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
