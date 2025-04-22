import os
import threading
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

# Carga variables de entorno desde .env (si existe)
load_dotenv()

# Construcción de la URL (DSN) para PostgreSQL
db_user = os.environ.get("POSTGRES_USER", "postgres")
db_pass = os.environ.get("POSTGRES_PASSWORD", "Felipe1416")
db_host = os.environ.get("POSTGRES_HOST", "localhost")
db_name = os.environ.get("POSTGRES_DB", "postgres")
db_port = os.environ.get("POSTGRES_PORT", "5432")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
)

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
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def get_session(self) -> Session:
        return self.SessionLocal()

Base = declarative_base()


def get_db():
    """
    Dependency: inyecta una sesión de la base de datos y la cierra al terminar la petición.
    """
    db_pool = DatabaseConnectionPool()
    db = db_pool.get_session()
    try:
        yield db
    finally:
        db.close()