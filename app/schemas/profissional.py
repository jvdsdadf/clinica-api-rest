from datetime import date
from pydantic import BaseModel, Field


class ProfissionalCreate(BaseModel):
    nomecompleto: str = Field(..., min_length=2, max_length=255)
    cpf: str

    profissao: str = Field(..., min_length=2, max_length=100)
    crm: str | None = Field(default=None, max_length=30)

    datanascimento: date | None = None
    telefone_principal: str | None = Field(default=None, max_length=20)


class ProfissionalUpdate(BaseModel):
    nomecompleto: str | None = Field(default=None, min_length=2, max_length=255)
    cpf: str | None = None

    profissao: str | None = Field(default=None, min_length=2, max_length=100)
    crm: str | None = Field(default=None, max_length=30)

    datanascimento: date | None = None
    telefone_principal: str | None = Field(default=None, max_length=20)


class ProfissionalOut(ProfissionalCreate):
    id_profissional: int

    class Config:
        from_attributes = True  # Pydantic v2
