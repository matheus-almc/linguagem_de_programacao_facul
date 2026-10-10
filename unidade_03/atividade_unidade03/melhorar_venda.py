
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==================================================
# EXPERIMENTO: MELHORAR O DESEMPENHO DE VENDAS
# ==================================================

# PASSO 1: CONECTAR AO BANCO DE DADOS SQLITE

conexao = sqlite3.connect("dados_vendas.db")
cursor = conexao.cursor()

# Criar a tabela caso ela ainda não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
""")

# Verificar se a tabela já possui dados
cursor.execute("SELECT COUNT(*) FROM vendas1")
quantidade_registros = cursor.fetchone()[0]

# Inserir os dados somente se a tabela estiver vazia
if quantidade_registros == 0:
    dados = [
        ("2023-01-01", "Produto A", "Eletrônicos", 1500.00),
        ("2023-01-05", "Produto B", "Roupas", 350.00),
        ("2023-02-10", "Produto C", "Eletrônicos", 1200.00),
        ("2023-03-15", "Produto D", "Livros", 200.00),
        ("2023-03-20", "Produto E", "Eletrônicos", 800.00),
        ("2023-04-02", "Produto F", "Roupas", 400.00),
        ("2023-05-05", "Produto G", "Livros", 150.00),
        ("2023-06-10", "Produto H", "Eletrônicos", 1000.00),
        ("2023-07-20", "Produto I", "Roupas", 600.00),
        ("2023-08-25", "Produto J", "Eletrônicos", 700.00),
        ("2023-09-30", "Produto K", "Livros", 300.00),
        ("2023-10-05", "Produto L", "Roupas", 450.00),
        ("2023-11-15", "Produto M", "Eletrônicos", 900.00),
        ("2023-12-20", "Produto N", "Livros", 250.00)
    ]

    cursor.executemany("""
        INSERT INTO vendas1
        (data_venda, produto, categoria, valor_venda)
        VALUES (?, ?, ?, ?)
    """, dados)

    conexao.commit()
    print("Dados de vendas cadastrados no banco!")

else:
    print("O banco já possui dados. Nenhuma duplicação foi realizada.")


# PASSO 2: EXPLORAR E PREPARAR OS DADOS

df_vendas = pd.read_sql_query(
    "SELECT * FROM vendas1",
    conexao
)

# Converter a coluna de datas para o formato adequado
df_vendas["data_venda"] = pd.to_datetime(
    df_vendas["data_venda"]
)

print("\n========== DADOS DE VENDAS ==========")
print(df_vendas)

print("\n========== INFORMAÇÕES DOS DADOS ==========")
df_vendas.info()

print("\n========== ESTATÍSTICAS DAS VENDAS ==========")
print(df_vendas["valor_venda"].describe())

# Verificar valores ausentes
print("\n========== VALORES AUSENTES ==========")
print(df_vendas.isnull().sum())


# PASSO 3: ANALISAR OS DADOS

faturamento_total = df_vendas["valor_venda"].sum()
media_vendas = df_vendas["valor_venda"].mean()
maior_venda = df_vendas.loc[
    df_vendas["valor_venda"].idxmax()
]
menor_venda = df_vendas.loc[
    df_vendas["valor_venda"].idxmin()
]

# Faturamento por categoria
vendas_categoria = (
    df_vendas.groupby("categoria")["valor_venda"]
    .sum()
    .sort_values(ascending=False)
)

# Faturamento por mês
df_vendas["mes"] = df_vendas["data_venda"].dt.month

vendas_mensais = (
    df_vendas.groupby("mes")["valor_venda"]
    .sum()
    .sort_index()
)

print("\n========== RESULTADOS DA ANÁLISE ==========")
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Média por venda: R$ {media_vendas:.2f}")
print(f"Quantidade de vendas: {len(df_vendas)}")

print(
    f"Maior venda: {maior_venda['produto']} - "
    f"R$ {maior_venda['valor_venda']:.2f}"
)

print(
    f"Menor venda: {menor_venda['produto']} - "
    f"R$ {menor_venda['valor_venda']:.2f}"
)

print("\nFaturamento por categoria:")
print(vendas_categoria)

print("\nFaturamento por mês:")
print(vendas_mensais)


# PASSO 4: CRIAR VISUALIZAÇÕES

sns.set_theme(style="whitegrid")

# Gráfico 1: faturamento por categoria
plt.figure(figsize=(8, 5))

sns.barplot(
    x=vendas_categoria.index,
    y=vendas_categoria.values
)

plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.savefig("faturamento_categoria.png")
plt.show()


# Gráfico 2: evolução mensal das vendas
plt.figure(figsize=(9, 5))

sns.lineplot(
    x=vendas_mensais.index,
    y=vendas_mensais.values,
    marker="o"
)

plt.title("Faturamento Mensal de 2023")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig("faturamento_mensal.png")
plt.show()


# Gráfico 3: distribuição dos valores das vendas
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df_vendas,
    x="valor_venda",
    bins=6,
    kde=True
)

plt.title("Distribuição dos Valores das Vendas")
plt.xlabel("Valor da venda (R$)")
plt.ylabel("Quantidade de vendas")
plt.tight_layout()
plt.savefig("distribuicao_vendas.png")
plt.show()


# PASSO 5: CONCLUSÃO

print("\n========== CONCLUSÃO ==========")

categoria_destaque = vendas_categoria.idxmax()
faturamento_destaque = vendas_categoria.max()

mes_destaque = vendas_mensais.idxmax()
faturamento_mes = vendas_mensais.max()

print(
    f"A categoria com maior faturamento foi "
    f"{categoria_destaque}, com R$ {faturamento_destaque:.2f}."
)

print(
    f"O mês com maior faturamento foi {mes_destaque}, "
    f"com R$ {faturamento_mes:.2f}."
)

print(
    "A empresa pode analisar as estratégias utilizadas "
    "nos períodos de melhor desempenho e avaliar ações "
    "para aumentar as vendas das demais categorias."
)

# Fechar a conexão com o banco de dados
conexao.close()
print("\nConexão com o banco de dados encerrada.")
