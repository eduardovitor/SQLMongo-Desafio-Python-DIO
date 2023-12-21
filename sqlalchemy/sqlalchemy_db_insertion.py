from sqlalchemy import create_engine
from sqlalchemy_db_definition import Cliente, Conta
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

clientes = [
    Cliente(
        nome="Fernando",
        cpf="777321",
        endereco="Rua da Consolação"
    ),
    Cliente(
        nome="Luana",
        cpf="222910",
        endereco="Rua da Saúde"
    ),
    Cliente(
        nome="Juliano",
        cpf="999345",
        endereco="Rua da Carne"
    ),
    Cliente(
        nome="Rafaella",
        cpf="556712",
        endereco="Rua da Esperança"
    ),
]

contas = [
    Conta(
        tipo="Corrente",
        agencia="0001",
        num="1",
        cliente=clientes[0]
    ),
    Conta(
        tipo="Corrente",
        agencia="0001",
        num="2",
        cliente=clientes[1]
    ),
    Conta(
        tipo="Corrente",
        agencia="0001",
        num="3",
        cliente=clientes[2]
    ),
    Conta(
        tipo="Corrente",
        agencia="0001",
        num="4",
        cliente=clientes[3]
    )
]

session.add_all(clientes)
session.add_all(contas)
session.commit()
