from fastapi import APIRouter, HTTPException, Depends, status
from typing import List, Any
from sqlalchemy.orm import Session
from app.services.usuario_service import (
    get_usuarios_service,
    get_usuario_service,
    create_usuario_service,
    update_usuario_service,
    delete_usuario_service,
)
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioOut
from app.database import get_db
from app.common.response import ResponseModel, success_response, error_response
from app.common.messages import USER_NOT_FOUND, SUCCESS_OPERATION

router = APIRouter()

@router.get(
    "/",
    response_model=ResponseModel[List[UsuarioOut]],
    summary="Listar usuarios"
)
def read_usuarios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> ResponseModel[List[UsuarioOut]]:
    usuarios = get_usuarios_service(db, skip, limit)
    return success_response(usuarios)


@router.get(
    "/{usuario_id}",
    response_model=ResponseModel[UsuarioOut],
    summary="Obtener usuario por ID"
)
def read_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
) -> ResponseModel[UsuarioOut]:
    usuario = get_usuario_service(db, usuario_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_response(message=USER_NOT_FOUND).dict(),
        )
    return success_response(usuario)


@router.post(
    "/",
    response_model=ResponseModel[UsuarioOut],
    status_code=status.HTTP_201_CREATED,
    summary="Crear nuevo usuario"
)
def create_usuario(
    usuario_in: UsuarioCreate,
    db: Session = Depends(get_db),
) -> ResponseModel[UsuarioOut]:
    nuevo = create_usuario_service(db, usuario_in)
    return success_response(nuevo, SUCCESS_OPERATION)


@router.put(
    "/{usuario_id}",
    response_model=ResponseModel[UsuarioOut],
    summary="Actualizar usuario existente"
)
def update_usuario(
    usuario_id: int,
    usuario_in: UsuarioUpdate,
    db: Session = Depends(get_db),
) -> ResponseModel[UsuarioOut]:
    actualizado = update_usuario_service(db, usuario_id, usuario_in)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_response(message=USER_NOT_FOUND),
        )
    return success_response(actualizado)


@router.delete(
    "/{usuario_id}",
    response_model=ResponseModel[Any],
    summary="Eliminar usuario"
)
def delete_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
) -> ResponseModel[Any]:
    borrado = delete_usuario_service(db, usuario_id)
    if not borrado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_response(message=USER_NOT_FOUND).dict(),
        )
    return success_response(None)