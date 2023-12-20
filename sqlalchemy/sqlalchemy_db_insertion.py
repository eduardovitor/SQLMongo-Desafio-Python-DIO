from sqlalchemy import create_engine
from sqlalchemy_db_definition import Cliente, Conta
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

cliente = Cliente(
    nome="Júnior",
    cpf="617299",
    endereco="Rua da Paz"
)

session.add(cliente)
session.commit()
