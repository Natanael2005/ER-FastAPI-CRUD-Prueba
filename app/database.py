import os
import threading
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

# Carga variables de entorno desde .env (si existe)
load_dotenv()

# Construcción de la URL (DSN) para PostgreSQL
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "Felipe1416")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
POSTGRES_DB   = os.environ.get("POSTGRES_DB", "postgres")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "5432")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# -------------------------------------------------------------------
# Patrón Singleton para engine y pool de sesiones
# -------------------------------------------------------------------
class DatabaseConnectionPool:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize_pool()
        return cls._instance

    def _initialize_pool(self):
        # Se inicializa una sola vez
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def get_session(self) -> Session:
        # Devuelve una nueva sesión ligada al mismo engine/pool
        return self.SessionLocal()

# -------------------------------------------------------------------
# Base para todos los modelos
# -------------------------------------------------------------------
Base = declarative_base()

# -------------------------------------------------------------------
# Dependency para FastAPI: inyecta y cierra la sesión automáticamente
# -------------------------------------------------------------------
from fastapi import Depends

def get_db():
    """
    Inyecta una sesión de base de datos y la cierra al terminar la petición.
    """
    db_pool = DatabaseConnectionPool()
    db = db_pool.get_session()
    try:
        yield db
    finally:
        db.close()
