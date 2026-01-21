from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.agendamento import AgendamentoCreate, AgendamentoOut, AgendamentoUpdate
from app.services.agendamento_service import AgendamentoService

router = APIRouter(prefix="/agendamentos", tags=["Agendamentos"])


@router.post("", response_model=AgendamentoOut, status_code=status.HTTP_201_CREATED)
def criar_agendamento(payload: AgendamentoCreate, db: Session = Depends(get_db)):
    return AgendamentoService.create(db, payload)


@router.get("", response_model=list[AgendamentoOut])
def listar_agendamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return AgendamentoService.list(db, skip=skip, limit=limit)


@router.get("/{id_agendamento}", response_model=AgendamentoOut)
def buscar_agendamento(id_agendamento: int, db: Session = Depends(get_db)):
    obj = AgendamentoService.get(db, id_agendamento)
    if not obj:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return obj


@router.put("/{id_agendamento}", response_model=AgendamentoOut)
def atualizar_agendamento(id_agendamento: int, payload: AgendamentoUpdate, db: Session = Depends(get_db)):
    obj = AgendamentoService.update(db, id_agendamento, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return obj


@router.delete("/{id_agendamento}", status_code=status.HTTP_204_NO_CONTENT)
def remover_agendamento(id_agendamento: int, db: Session = Depends(get_db)):
    ok = AgendamentoService.delete(db, id_agendamento)
    if not ok:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    return None
