from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.repositories import usuario_repo


def get_usuario_service(db: Session, usuario_id: int):
    return usuario_repo.get_usuario(db, usuario_id)


def get_usuarios_service(db: Session, skip: int = 0, limit: int = 100):
    return usuario_repo.get_usuarios(db, skip, limit)


def create_usuario_service(db: Session, usuario_data: dict):
    nuevo_usuario = Usuario(**usuario_data)
    return usuario_repo.create_usuario(db, nuevo_usuario)


def update_usuario_service(db: Session, usuario_id: int, update_data: dict):
    return usuario_repo.update_usuario(db, usuario_id, update_data)


def delete_usuario_service(db: Session, usuario_id: int):
    return usuario_repo.delete_usuario(db, usuario_id)


def get_usuario_by_email_service(db: Session, email: str):
    return usuario_repo.get_usuario_by_email(db, email)