from sqlalchemy import Column, Integer, Date, ForeignKey, Text, Date
from app.db import Base

class Prescricao(Base):
    __tablename__ = "prescricao"

    idPrescricao = Column(Integer, primary_key=True)
    idPaciente = Column(Integer, ForeignKey("paciente.id_paciente"))
    idProfissional = Column(Integer, ForeignKey("profissional.id_profissional"))
    idPlanoTratamento = Column(Integer)

    dataPrescricao = Column(Date)
    validadePrescricao = Column(Date)
    observacoesGerais = Column(Text)
