import pandas as pd


# Criar um dicionário com nomes e idades
dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]
}


# Criar uma Series a partir do dicionário
serie_idades = pd.Series(
    dados['Idade'],
    index=dados['Nome']
)


# Exibir a Series de idades
print("Série de Idades:")
print(serie_idades)


# Calcular a média das idades
media_idades = serie_idades.mean()


# Exibir a média
print("\nMédia de Idades:", media_idades)


# Resultado esperado:
#
# Série de Idades:
# Alice    25
# Bob      30
# Carol    22
# David    35
# Eve      28
# dtype: int64
#
# Média de Idades: 28.0