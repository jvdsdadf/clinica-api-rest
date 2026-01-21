from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional

class PacienteCreate(BaseModel):
    nomecompleto: str
    datanascimento: Optional[date] = None
    cpf: Optional[str] = None
    rg: Optional[str] = None
    email: Optional[str] = None
    telefonePrincipal: Optional[str] = None

    endereco_logradouro: Optional[str] = None
    endereco_numero: Optional[str] = None
    endereco_bairro: Optional[str] = None
    endereco_cidade: Optional[str] = None
    enderecoUF: Optional[str] = None
    enderecoCEP: Optional[str] = None

    alergiasConhecidas: Optional[str] = None
    historicoMedicoProgresso: Optional[str] = None

    idResponsavel: Optional[int] = None

class PacienteUpdate(BaseModel):
    nomecompleto: Optional[str] = None
    datanascimento: Optional[date] = None
    cpf: Optional[str] = None
    rg: Optional[str] = None
    email: Optional[str] = None
    telefonePrincipal: Optional[str] = None

    endereco_logradouro: Optional[str] = None
    endereco_numero: Optional[str] = None
    endereco_bairro: Optional[str] = None
    endereco_cidade: Optional[str] = None
    enderecoUF: Optional[str] = None
    enderecoCEP: Optional[str] = None

    alergiasConhecidas: Optional[str] = None
    historicoMedicoProgresso: Optional[str] = None

    idResponsavel: Optional[int] = None

class PacienteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_paciente: int
    nomecompleto: str
    datanascimento: Optional[date] = None
    cpf: Optional[str] = None
    rg: Optional[str] = None
    email: Optional[str] = None
    telefonePrincipal: Optional[str] = None
    idResponsavel: Optional[int] = None
