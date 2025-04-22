from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.services import usuario_service
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioOut
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[UsuarioOut])
def read_usuarios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return usuario_service.get_usuarios_service(db, skip, limit)

@router.get("/{usuario_id}", response_model=UsuarioOut)
def read_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = usuario_service.get_usuario_service(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=UsuarioOut)
def create_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    return usuario_service.create_usuario_service(db, usuario.model_dump())

@router.put("/{usuario_id}", response_model=UsuarioOut)
def update_usuario(
    usuario_id: int,
    update_data: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    usuario = usuario_service.update_usuario_service(
        db,
        usuario_id,
        update_data.model_dump(exclude_unset=True)
    )
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.delete("/{usuario_id}", response_model=UsuarioOut)
def delete_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = usuario_service.delete_usuario_service(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario