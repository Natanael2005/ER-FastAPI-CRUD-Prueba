# app/services/usuario_service.py
from app.repositories import usuario_repo
from app.database import SessionLocal
from app.models.usuario import Usuario

def get_usuario_service(usuario_id: int):
    db = SessionLocal()
    try:
        usuario = usuario_repo.get_usuario(db, usuario_id)
    finally:
        db.close()
    return usuario

def get_usuarios_service(skip: int = 0, limit: int = 100):
    db = SessionLocal()
    try:
        usuarios = usuario_repo.get_usuarios(db, skip, limit)
    finally:
        db.close()
    return usuarios

def create_usuario_service(usuario_data: dict):
    db = SessionLocal()
    try:
        nuevo_usuario = Usuario(**usuario_data)
        usuario = usuario_repo.create_usuario(db, nuevo_usuario)
    finally:
        db.close()
    return usuario

def update_usuario_service(usuario_id: int, update_data: dict):
    db = SessionLocal()
    try:
        usuario = usuario_repo.update_usuario(db, usuario_id, update_data)
    finally:
        db.close()
    return usuario

def delete_usuario_service(usuario_id: int):
    db = SessionLocal()
    try:
        usuario = usuario_repo.delete_usuario(db, usuario_id)
    finally:
        db.close()
    return usuario

def get_usuario_by_email_service(email: str):
    db = SessionLocal()
    try:
        usuario = usuario_repo.get_usuario_by_email(db, email)
    finally:
        db.close()
    return usuario
