from __future__ import annotations
from datetime import datetime, date
from pydantic import BaseModel, ConfigDict


class AgendamentoBase(BaseModel):
    data_hora: datetime
    tipo_atendimento: str
    status: str
    id_paciente: int
    id_profissional: int


class AgendamentoCreate(AgendamentoBase):
    pass


class AgendamentoUpdate(BaseModel):
    data_hora: datetime | None = None
    tipo_atendimento: str | None = None
    status: str | None = None
    id_paciente: int | None = None
    id_profissional: int | None = None


class AgendamentoOut(AgendamentoBase):
    model_config = ConfigDict(from_attributes=True)
    id_agendamento: int
