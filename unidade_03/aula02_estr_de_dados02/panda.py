# Importando a biblioteca Pandas
import pandas as pd


# Criando uma lista de valores
data = [10, 20, 30, 40, 50]


# Criando uma Series a partir da lista
series1 = pd.Series(data)


# Imprimindo a Series
print(series1)


# Resultado esperado:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

import pandas as pd


# Criando um dicionário com pares chave-valor
data = {
    'A': 100,
    'B': 200,
    'C': 300,
    'D': 400,
    'E': 500
}


# Criando uma Series a partir do dicionário
series2 = pd.Series(data)


# Imprimindo a Series
print(series2)


# Resultado esperado:
# A    100
# B    200
# C    300
# D    400
# E    500
# dtype: int64