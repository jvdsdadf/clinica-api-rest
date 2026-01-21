from __future__ import annotations
from sqlalchemy.orm import Session
from app.models.agendamento import Agendamento
from app.schemas.agendamento import AgendamentoCreate, AgendamentoUpdate
from app.repositories.agendamento_repository import AgendamentoRepository


class AgendamentoService:
    @staticmethod
    def create(db: Session, payload: AgendamentoCreate) -> Agendamento:
        obj = Agendamento(**payload.model_dump())
        return AgendamentoRepository.create(db, obj)

    @staticmethod
    def get(db: Session, agendamento_id: int) -> Agendamento | None:
        return AgendamentoRepository.get_by_id(db, agendamento_id)

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100) -> list[Agendamento]:
        return AgendamentoRepository.list(db, skip=skip, limit=limit)

    @staticmethod
    def update(db: Session, agendamento_id: int, payload: AgendamentoUpdate) -> Agendamento | None:
        obj = AgendamentoRepository.get_by_id(db, agendamento_id)
        if not obj:
            return None

        data = payload.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(obj, k, v)

        return AgendamentoRepository.update(db, obj)

    @staticmethod
    def delete(db: Session, agendamento_id: int) -> bool:
        obj = AgendamentoRepository.get_by_id(db, agendamento_id)
        if not obj:
            return False
        AgendamentoRepository.delete(db, obj)
        return True
