# app/controllers/usuario_controller.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.services import usuario_service
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioOut

router = APIRouter()

@router.get("/", response_model=List[UsuarioOut])
def read_usuarios(skip: int = 0, limit: int = 100):
    return usuario_service.get_usuarios_service(skip=skip, limit=limit)

@router.get("/{usuario_id}", response_model=UsuarioOut)
def read_usuario(usuario_id: int):
    usuario = usuario_service.get_usuario_service(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=UsuarioOut)
def create_usuario(usuario: UsuarioCreate):
    return usuario_service.create_usuario_service(usuario.model_dump())

@router.put("/{usuario_id}", response_model=UsuarioOut)
def update_usuario(usuario_id: int, update_data: UsuarioUpdate):
    usuario = usuario_service.update_usuario_service(usuario_id, update_data.model_dump(exclude_unset=True))
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/{usuario_id}", response_model=UsuarioOut)
def delete_usuario(usuario_id: int):
    usuario = usuario_service.delete_usuario_service(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/email/{email}", response_model=UsuarioOut)
def read_usuario_by_email(email: str):
    usuario = usuario_service.get_usuario_by_email_service(email)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario  