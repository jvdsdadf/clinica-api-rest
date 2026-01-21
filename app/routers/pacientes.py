from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.services.paciente_service import PacienteService
from app.schemas.paciente import PacienteCreate, PacienteUpdate, PacienteOut

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])


@router.get("", response_model=list[PacienteOut])
def listar_pacientes(db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.listar()


@router.get("/{id_paciente}", response_model=PacienteOut)
def buscar_paciente(id_paciente: int, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.buscar_por_id(id_paciente)


@router.post("", response_model=PacienteOut, status_code=status.HTTP_201_CREATED)
def criar_paciente(payload: PacienteCreate, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.criar(payload)


@router.put("/{id_paciente}", response_model=PacienteOut)
def atualizar_paciente(id_paciente: int, payload: PacienteUpdate, db: Session = Depends(get_db)):
    service = PacienteService(db)
    return service.atualizar(id_paciente, payload)


@router.delete("/{id_paciente}", status_code=status.HTTP_204_NO_CONTENT)
def remover_paciente(id_paciente: int, db: Session = Depends(get_db)):
    service = PacienteService(db)
    service.remover(id_paciente)
    return None
