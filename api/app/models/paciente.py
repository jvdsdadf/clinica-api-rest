from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Date
from app.db import Base

class Paciente(Base):
    __tablename__ = "paciente"

    id_paciente = Column(Integer, primary_key=True)
    nomecompleto = Column(String(255), nullable=False)
    datanascimento = Column(Date)
    cpf = Column(String(14), unique=True)
    rg = Column(String(20))
    email = Column(String(255))
    telefonePrincipal = Column(String(20))

    endereco_logradouro = Column(String(255))
    endereco_numero = Column(String(10))
    endereco_bairro = Column(String(100))
    endereco_cidade = Column(String(100))
    enderecoUF = Column(String(2))
    enderecoCEP = Column(String(9))

    alergiasConhecidas = Column(Text)
    historicoMedicoProgresso = Column(Text)

    idResponsavel = Column(Integer, ForeignKey("responsavel.idResponsavel"))
