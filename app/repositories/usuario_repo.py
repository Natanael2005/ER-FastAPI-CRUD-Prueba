 # app/repositories/usuario_repo.py
from sqlalchemy.orm import Session
from app.models.usuario import Usuario

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: Usuario):
    db.add(usuario)
    db.commit() 
    db.refresh(usuario)
    return usuario

def update_usuario(db: Session, usuario_id: int, update_data: dict):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        for key, value in update_data.items():
            setattr(usuario, key, value)
        db.commit()
        db.refresh(usuario)
    return usuario

def delete_usuario(db: Session, usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario

# Ejemplo adicional: Buscar usuario por email
def get_usuario_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()
