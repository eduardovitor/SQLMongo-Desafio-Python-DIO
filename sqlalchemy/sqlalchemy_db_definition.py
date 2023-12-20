from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///:memory", echo=True)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))

    def __repr__(self):
        return f'Cliente: \n Nome: {self.nome} \n Endereco: {self.endereco}'


class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente.id"))
    cliente = relationship("Cliente")

    def __repr__(self):
        return f"""Conta:
        Tipo: {self.tipo}
        Agência: {self.agencia}
        Número: {self.num}"""


Base.metadata.create_all(engine)
