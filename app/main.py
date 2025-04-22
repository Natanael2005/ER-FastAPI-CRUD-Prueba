from fastapi import FastAPI
from app.controllers import usuario_controller
from app.database import DatabaseConnectionPool, Base

# Crear tablas en la base de datos usando el engine del Singleton
pool = DatabaseConnectionPool()
Base.metadata.create_all(bind=pool.engine)

app = FastAPI(title="Proyecto Backend con FastAPI y PostgreSQL")

# Montamos el router de usuarios bajo /usuarios
app.include_router(
    usuario_controller.router,
    prefix="/usuarios",
    tags=["Usuarios"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
