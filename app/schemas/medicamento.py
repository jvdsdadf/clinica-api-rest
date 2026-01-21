from pydantic import BaseModel, ConfigDict
from typing import Optional

class MedicamentoBase(BaseModel):
    nomeGenerico: Optional[str] = None
    nomeComercial: Optional[str] = None
    concentracaoPadrao: Optional[str] = None
    formaFarmaceuticaPadrao: Optional[str] = None
    laboratorio: Optional[str] = None
    codigoANVISA: Optional[str] = None

class MedicamentoCreate(MedicamentoBase):
    pass

class MedicamentoUpdate(MedicamentoBase):
    pass

class MedicamentoOut(MedicamentoBase):
    idMedicamento: int
    model_config = ConfigDict(from_attributes=True)
