import pandas as pd


# URL da página que contém a tabela
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"


# Lê as tabelas existentes na página
dfs = pd.read_html(url)


# Verifica o tipo do resultado
print(type(dfs))


# Verifica quantas tabelas foram encontradas
print(len(dfs))


# Pegando a primeira tabela da lista
df_bancos = dfs[0]


# Mostra a quantidade de linhas e colunas
print(df_bancos.shape)


# Mostra o tipo de dado de cada coluna
print(df_bancos.dtypes)


# Mostra as primeiras linhas do DataFrame
print(df_bancos.head())