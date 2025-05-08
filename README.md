
# 📦 Projeto: Sistema de Cadastro de Produtos e Fornecedores

Este projeto consiste em um script Python que utiliza **SQLAlchemy** para criar e manipular um banco de dados SQLite com duas tabelas: `fornecedores` e `produtos`. Ele realiza inserções de dados e uma consulta agregada com `JOIN`. Foi realizado para fins de estudo, para fixar conceitos e entender o poder e importância do uso de uma ORM

## 🛠 Tecnologias

- Python 3
- SQLAlchemy (ORM)
- SQLite

## 🧱 Estrutura do Banco de Dados

### 🔹 Tabela `fornecedores`
Contém informações dos fornecedores:
- `id`: chave primária
- `nome`
- `cnpj`
- `email`
- `telefone`
- `cidade`

### 🔹 Tabela `produtos`
Contém informações dos produtos, com relacionamento para um fornecedor:
- `id`: chave primária
- `nome`
- `descricao`
- `preco`
- `estoque`
- `categoria`
- `fornecedor_id`: chave estrangeira referenciando `fornecedores.id`

## 🔗 Relacionamento

- Cada **produto** está associado a **um fornecedor** (`fornecedor_id`).
- A relação é estabelecida com `ForeignKey` e `relationship` entre os modelos.

## 📥 Inserção de Dados

- São inseridos 5 fornecedores.
- São inseridos 5 produtos, todos vinculados ao **Fornecedor A** (com `fornecedor_id = 1`).

## 📊 Consulta com Join e Agregação

O script executa uma consulta para **somar o preço total de produtos agrupados por fornecedor**:

```python
resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto).group_by(Fornecedor.id).all()
```

Resultado exibido no console:

```
Fornecedor: Fornecedor A, Total Preço: 218.9
```

## ✅ Como Executar

1. Instale o SQLAlchemy:
   ```bash
   pip install sqlalchemy
   ```
2. Execute o script Python.

---
