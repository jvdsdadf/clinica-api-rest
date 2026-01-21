from sqlalchemy import Column, Integer, String
from app.db import Base

class Medicamento(Base):
    __tablename__ = "medicamento"

    idMedicamento = Column(Integer, primary_key=True)
    nomeGenerico = Column(String(45))
    nomeComercial = Column(String(45))
    concentracaoPadrao = Column(String(45))
    formaFarmaceuticaPadrao = Column(String(45))
    laboratorio = Column(String(45))
    codigoANVISA = Column(String(45))
