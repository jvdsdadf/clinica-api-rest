from __future__ import annotations
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.paciente_repository import PacienteRepository
from app.schemas.paciente import PacienteCreate, PacienteUpdate
from app.models.paciente import Paciente


class PacienteService:
    def __init__(self, db: Session):
        self.repo = PacienteRepository(db)

    def listar(self) -> list[Paciente]:
        return self.repo.listar()

    def buscar_por_id(self, id_paciente: int) -> Paciente:
        paciente = self.repo.buscar_por_id(id_paciente)
        if not paciente:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")
        return paciente

    def criar(self, payload: PacienteCreate) -> Paciente:
        # Exemplo de regra de negócio: cpf obrigatório e com tamanho mínimo
        if payload.cpf and len(payload.cpf) < 11:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="CPF inválido")
        return self.repo.criar(payload)

    def atualizar(self, id_paciente: int, payload: PacienteUpdate) -> Paciente:
        paciente = self.buscar_por_id(id_paciente)
        return self.repo.atualizar(paciente, payload)

    def remover(self, id_paciente: int) -> None:
        paciente = self.buscar_por_id(id_paciente)
        self.repo.remover(paciente)
