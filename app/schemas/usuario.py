# app/schemas/usuario.py
from pydantic import BaseModel, EmailStr

# Modelo base con los campos comunes
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

# Modelo para la creación de un usuario (hereda de UsuarioBase)
class UsuarioCreate(UsuarioBase):
    pass

# Modelo para la actualización de un usuario (los campos son opcionales)
class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: EmailStr | None = None

# Modelo para la salida, incluye id
class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True  # Permite leer los datos de objetos ORM (SQLAlchemy)
