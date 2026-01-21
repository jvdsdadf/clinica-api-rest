from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from app.db import Base

class Agendamento(Base):
    __tablename__ = "agendamento"

    idAgendamento = Column(Integer, primary_key=True)
    idPaciente = Column(Integer, ForeignKey("paciente.id_paciente"), nullable=False)
    idProfissional = Column(Integer, ForeignKey("profissional.id_profissional"), nullable=False)

    dataHoraInicio = Column(DateTime, nullable=False)
    dataHoraFimEstimada = Column(DateTime)

    tipoAtendimento = Column(String(100))
    statusAgendamento = Column(String(45))
    observacoes = Column(String(255))
