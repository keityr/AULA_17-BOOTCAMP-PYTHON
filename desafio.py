#Criar conexao com engine com o banco de dados

from sqlalchemy import create_engine

engine = create_engine('sqlite:///empresa.db', echo=True)

print('Conexão bem sucedida')


from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey


Base = declarative_base()


#Criar a estrutura da tabela usando abstração da declarative_base()


class Fornecedor(Base):

    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cnpj = Column(Integer)
    email = Column(String)
    telefone = Column(Integer)
    cidade = Column(String)


class Produto(Base):

    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float)
    estoque = Column(Integer)
    categoria = Column(String)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

#Consolida a relação entre Fornecedor e Produto
    fornecedor = relationship("Fornecedor")

Base.metadata.create_all(engine)
print('Tabelas Criadas com sucesso')

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


    
fornecedores_lista = [
    Fornecedor(nome="Fornecedor A", cnpj="00.111.222/0001-33", email="a@exemplo.com", telefone="11999990000", cidade="São Paulo"),
    Fornecedor(nome="Fornecedor B", cnpj="11.222.333/0001-44", email="b@exemplo.com", telefone="21999991111", cidade="Rio de Janeiro"),
    Fornecedor(nome="Fornecedor C", cnpj="22.333.444/0001-55", email="c@exemplo.com", telefone="31999992222", cidade="Belo Horizonte"),
    Fornecedor(nome="Fornecedor D", cnpj="33.444.555/0001-66", email="d@exemplo.com", telefone="41999993333", cidade="Curitiba"),
    Fornecedor(nome="Fornecedor E", cnpj="44.555.666/0001-77", email="e@exemplo.com", telefone="51999994444", cidade="Porto Alegre"),
]

with Session() as sessions:
    sessions.add_all(fornecedores_lista)
    sessions.commit()

produtos_lista = [
        Produto(nome="Caderno", descricao="Caderno universitário 200 folhas", preco=15.90, estoque=100, categoria="Papelaria", fornecedor_id=1),
        Produto(nome="Caneta", descricao="Caneta esferográfica azul", preco=1.50, estoque=300, categoria="Papelaria", fornecedor_id=4),
        Produto(nome="Mouse", descricao="Mouse óptico USB", preco=45.00, estoque=50, categoria="Informática", fornecedor_id=4),
        Produto(nome="Teclado", descricao="Teclado ABNT2 com fio", preco=65.00, estoque=40, categoria="Informática", fornecedor_id=1),
        Produto(nome="Garrafa Térmica", descricao="Garrafa térmica 1L inox", preco=89.90, estoque=25, categoria="Utilidades", fornecedor_id=1),
    ]


with Session() as sessions:
    sessions.add_all(produtos_lista)
    sessions.commit()

# for produto in session.query(Produto).all():
#     print(f"Produto: {produto.nome}, Fornecedor: {produto.fornecedor.nome}")

from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
# Supondo que engine já foi definido anteriormente e os modelos Produto e Fornecedor foram definidos conforme o exemplo anterior.

Session = sessionmaker(bind=engine)
session = Session()

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id
).group_by(Fornecedor.nome).all()

for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")