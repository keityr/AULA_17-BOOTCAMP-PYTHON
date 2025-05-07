from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")

# URI =  create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")

# dialect = create_engine("dialect+driver://username:password@host:port/database")
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)



class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cnpj = Column(Integer)
    
# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


with Session() as sessions:
    nova_dados = Usuario(nome = 'Keity', idade= 29)
    sessions.add(nova_dados)
    novo_fornecedor = Fornecedor(nome= 'Ambev', cnpj=2354555555)
    sessions.add(novo_fornecedor)

    sessions.commit()




