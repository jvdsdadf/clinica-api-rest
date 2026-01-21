from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.profissional import ProfissionalCreate, ProfissionalOut, ProfissionalUpdate
from app.services.profissional_service import ProfissionalService

router = APIRouter(prefix="/profissionais", tags=["Profissionais"])


@router.post("", response_model=ProfissionalOut, status_code=status.HTTP_201_CREATED)
def criar(payload: ProfissionalCreate, db: Session = Depends(get_db)):
    return ProfissionalService.create(db, payload)


@router.get("", response_model=list[ProfissionalOut])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ProfissionalService.list(db, skip=skip, limit=limit)


@router.get("/{id_profissional}", response_model=ProfissionalOut)
def buscar(id_profissional: int, db: Session = Depends(get_db)):
    obj = ProfissionalService.get(db, id_profissional)
    if not obj:
        raise HTTPException(status_code=404, detail="Profissional não encontrado")
    return obj


@router.put("/{id_profissional}", response_model=ProfissionalOut)
def atualizar(id_profissional: int, payload: ProfissionalUpdate, db: Session = Depends(get_db)):
    obj = ProfissionalService.update(db, id_profissional, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Profissional não encontrado")
    return obj


@router.delete("/{id_profissional}", status_code=status.HTTP_204_NO_CONTENT)
def remover(id_profissional: int, db: Session = Depends(get_db)):
    ok = ProfissionalService.delete(db, id_profissional)
    if not ok:
        raise HTTPException(status_code=404, detail="Profissional não encontrado")
    return None
