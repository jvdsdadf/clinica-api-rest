from __future__ import annotations
from sqlalchemy.orm import Session
from app.models.profissional import Profissional
from app.schemas.profissional import ProfissionalCreate, ProfissionalUpdate
from app.repositories.profissional_repository import ProfissionalRepository


class ProfissionalService:
    @staticmethod
    def create(db: Session, payload: ProfissionalCreate) -> Profissional:
        obj = Profissional(**payload.model_dump())
        return ProfissionalRepository.create(db, obj)

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100) -> list[Profissional]:
        return ProfissionalRepository.list(db, skip=skip, limit=limit)

    @staticmethod
    def get(db: Session, obj_id: int) -> Profissional | None:
        return ProfissionalRepository.get_by_id(db, obj_id)

    @staticmethod
    def update(db: Session, obj_id: int, payload: ProfissionalUpdate) -> Profissional | None:
        obj = ProfissionalRepository.get_by_id(db, obj_id)
        if not obj:
            return None

        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(obj, k, v)

        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def delete(db: Session, obj_id: int) -> bool:
        obj = ProfissionalRepository.get_by_id(db, obj_id)
        if not obj:
            return False
        ProfissionalRepository.delete(db, obj)
        return True
