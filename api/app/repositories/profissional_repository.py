from __future__ import annotations
from sqlalchemy.orm import Session
from app.models.profissional import Profissional


class ProfissionalRepository:
    @staticmethod
    def create(db: Session, obj: Profissional) -> Profissional:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_by_id(db: Session, obj_id: int) -> Profissional | None:
        return db.query(Profissional).filter(Profissional.id_profissional == obj_id).first()

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100) -> list[Profissional]:
        return db.query(Profissional).offset(skip).limit(limit).all()

    @staticmethod
    def delete(db: Session, obj: Profissional) -> None:
        db.delete(obj)
        db.commit()
