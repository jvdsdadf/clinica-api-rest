from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.schemas.medicamento import MedicamentoCreate, MedicamentoUpdate, MedicamentoOut
from app.services.medicamento_service import MedicamentoService

router = APIRouter(prefix="/medicamentos", tags=["Medicamentos"])

@router.post("", response_model=MedicamentoOut, status_code=status.HTTP_201_CREATED)
def criar_medicamento(payload: MedicamentoCreate, db: Session = Depends(get_db)):
    return MedicamentoService(db).create(payload)

@router.get("", response_model=List[MedicamentoOut])
def listar_medicamentos(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return MedicamentoService(db).list(skip=skip, limit=limit)

@router.get("/{medicamento_id}", response_model=MedicamentoOut)
def Buscar_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    return MedicamentoService(db).get(medicamento_id)

@router.put("/{medicamento_id}", response_model=MedicamentoOut)
def Atualizar_medicamento(medicamento_id: int, payload: MedicamentoUpdate, db: Session = Depends(get_db)):
    return MedicamentoService(db).update(medicamento_id, payload)

@router.delete("/{medicamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def Deletar_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    MedicamentoService(db).delete(medicamento_id)
    return None
