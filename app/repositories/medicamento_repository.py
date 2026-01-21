from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.medicamento import Medicamento

class MedicamentoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, medicamento: Medicamento) -> Medicamento:
        self.db.add(medicamento)
        self.db.commit()
        self.db.refresh(medicamento)
        return medicamento

    def get_by_id(self, medicamento_id: int) -> Optional[Medicamento]:
        return (
            self.db.query(Medicamento)
            .filter(Medicamento.idMedicamento == medicamento_id)
            .first()
        )

    def list(self, skip: int = 0, limit: int = 50) -> List[Medicamento]:
        return (
            self.db.query(Medicamento)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update(self, medicamento: Medicamento) -> Medicamento:
        self.db.commit()
        self.db.refresh(medicamento)
        return medicamento

    def delete(self, medicamento: Medicamento) -> None:
        self.db.delete(medicamento)
        self.db.commit()

    def exists_by_anvisa(self, codigo_anvisa: str, ignore_id: Optional[int] = None) -> bool:
        q = self.db.query(Medicamento).filter(Medicamento.codigoANVISA == codigo_anvisa)
        if ignore_id is not None:
            q = q.filter(Medicamento.idMedicamento != ignore_id)
        return self.db.query(q.exists()).scalar()
