from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_db_definition import Cliente, Conta

engine = create_engine("sqlite:///:memory")
Session = sessionmaker(bind=engine)
session = Session()
cliente_teste = Cliente(nome="Luana", cpf="222910", endereco="Rua da Saúde"),
query_todos_os_clientes = session.query(Cliente)
query_um_cliente = session.query(Cliente).filter_by(nome="Luana")
query_todas_as_contas = session.query(Conta)
query_conta = session.query(Conta).filter_by(id_cliente=5)
print("### TODOS OS CLIENTES ###")
for cliente in query_todos_os_clientes:
    print(cliente)
print("### UM CLIENTE ###")
print(query_um_cliente.first())
print("### TODAS AS CONTAS ###")
for conta in query_todas_as_contas:
    print(conta)
print("### UMA CONTA ###")
print(query_conta.first())
