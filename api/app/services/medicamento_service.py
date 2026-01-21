from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional
from app.models.medicamento import Medicamento
from app.repositories.medicamento_repository import MedicamentoRepository
from app.schemas.medicamento import MedicamentoCreate, MedicamentoUpdate

class MedicamentoService:
    def __init__(self, db: Session):
        self.repo = MedicamentoRepository(db)

    def create(self, data: MedicamentoCreate) -> Medicamento:
        if data.codigoANVISA and self.repo.exists_by_anvisa(data.codigoANVISA):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um medicamento com esse codigoANVISA.",
            )

        obj = Medicamento(**data.model_dump(exclude_unset=True))
        return self.repo.create(obj)

    def get(self, medicamento_id: int) -> Medicamento:
        obj = self.repo.get_by_id(medicamento_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medicamento não encontrado.",
            )
        return obj

    def list(self, skip: int = 0, limit: int = 50) -> List[Medicamento]:
        return self.repo.list(skip=skip, limit=limit)

    def update(self, medicamento_id: int, data: MedicamentoUpdate) -> Medicamento:
        obj = self.get(medicamento_id)

        payload = data.model_dump(exclude_unset=True)
        if "codigoANVISA" in payload and payload["codigoANVISA"]:
            if self.repo.exists_by_anvisa(payload["codigoANVISA"], ignore_id=medicamento_id):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Já existe um medicamento com esse codigoANVISA.",
                )

        for k, v in payload.items():
            setattr(obj, k, v)

        return self.repo.update(obj)

    def delete(self, medicamento_id: int) -> None:
        obj = self.get(medicamento_id)
        self.repo.delete(obj)
