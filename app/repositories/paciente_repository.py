from __future__ import annotations
from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate, PacienteUpdate


class PacienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def listar(self) -> list[Paciente]:
        return self.db.query(Paciente).order_by(Paciente.id_paciente.desc()).all()

    def buscar_por_id(self, id_paciente: int) -> Paciente | None:
        return self.db.query(Paciente).filter(Paciente.id_paciente == id_paciente).first()

    def criar(self, payload: PacienteCreate) -> Paciente:
        paciente = Paciente(**payload.model_dump())
        self.db.add(paciente)
        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def atualizar(self, paciente: Paciente, payload: PacienteUpdate) -> Paciente:
        dados = payload.model_dump(exclude_unset=True)
        for k, v in dados.items():
            setattr(paciente, k, v)

        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def remover(self, paciente: Paciente) -> None:
        self.db.delete(paciente)
        self.db.commit()
