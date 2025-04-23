# app/services/usuario_service.py
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

from app.models.usuario import Usuario
from app.repositories.usuario_repo import (
    get_usuario,
    get_usuarios,
    create_usuario as repo_create_usuario,
    update_usuario as repo_update_usuario,
    delete_usuario as repo_delete_usuario,
    get_usuario_by_email as repo_get_usuario_by_email,
)
from app.common.messages import EMAIL_ALREADY_EXISTS
from app.common.response import error_response
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate


def get_usuario_service(db: Session, usuario_id: int) -> Optional[Usuario]:
    return get_usuario(db, usuario_id)


def get_usuarios_service(db: Session, skip: int = 0, limit: int = 100) -> List[Usuario]:
    return get_usuarios(db, skip, limit)


def create_usuario_service(
    db: Session,
    usuario_data: UsuarioCreate
) -> Usuario:
    """
    Crea un nuevo usuario a partir de un schema UsuarioCreate.
    Captura violaciones de unicidad en el email.
    """
    nuevo = Usuario(**usuario_data.model_dump())
    try:
        return repo_create_usuario(db, nuevo)
    except IntegrityError:
        # Lanzamos un 400 con nuestro formato de error
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_response(message=EMAIL_ALREADY_EXISTS).dict()
        )


def update_usuario_service(
    db: Session,
    usuario_id: int,
    update_data: UsuarioUpdate
) -> Optional[Usuario]:
    update_dict = update_data.model_dump(exclude_unset=True)
    try:
        return repo_update_usuario(db, usuario_id, update_dict)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_response(message=EMAIL_ALREADY_EXISTS).dict()
        )


def delete_usuario_service(db: Session, usuario_id: int) -> bool:
    return repo_delete_usuario(db, usuario_id)


def get_usuario_by_email_service(db: Session, email: str) -> Optional[Usuario]:
    return repo_get_usuario_by_email(db, email)
