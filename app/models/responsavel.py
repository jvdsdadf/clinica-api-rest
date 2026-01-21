from sqlalchemy import Column, Integer, String
from app.db import Base

class Responsavel(Base):
    __tablename__ = "responsavel"

    idResponsavel = Column(Integer, primary_key=True)
    nomeCompleto = Column(String(255), nullable=False)
    CPF = Column(String(14))
    RG = Column(String(20))
    telefonePrincipal = Column(String(20))
    parentesco = Column(String(45))
