# app/schemas/usuario.py
from pydantic import BaseModel, EmailStr

# Modelo base con los campos comunes
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr

# Modelo para crear un nuevo usuario
class UsuarioCreate(UsuarioBase):
    pass

# Modelo para actualizar un usuario existente
class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: EmailStr | None = None

# Modelo para la salida de usuario con el ID
class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True