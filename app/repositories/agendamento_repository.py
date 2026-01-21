from __future__ import annotations
from sqlalchemy.orm import Session

from app.models.agendamento import Agendamento


class AgendamentoRepository:
    @staticmethod
    def create(db: Session, agendamento: Agendamento) -> Agendamento:
        db.add(agendamento)
        db.commit()
        db.refresh(agendamento)
        return agendamento

    @staticmethod
    def get_by_id(db: Session, agendamento_id: int) -> Agendamento | None:
        return db.query(Agendamento).filter(Agendamento.id_agendamento == agendamento_id).first()

    @staticmethod
    def list(db: Session, skip: int = 0, limit: int = 100) -> list[Agendamento]:
        return db.query(Agendamento).offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, agendamento: Agendamento) -> Agendamento:
        db.commit()
        db.refresh(agendamento)
        return agendamento

    @staticmethod
    def delete(db: Session, agendamento: Agendamento) -> None:
        db.delete(agendamento)
        db.commit()
