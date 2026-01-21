from sqlalchemy import Column, Integer, String, Date
from app.db import Base

class Profissional(Base):
    __tablename__ = "profissional"

    id_profissional = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    datanascimento = Column(Date, nullable=True)
    telefone_principal = Column(String(20), nullable=True)
    profissao = Column(String(100), nullable=False)
    crm = Column(String(30), nullable=True, unique=True, index=True)