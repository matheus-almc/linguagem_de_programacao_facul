import matplotlib.pyplot as plt
import random


# Criando dois conjuntos de dados aleatórios
dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)


# Criando o gráfico
plt.plot(dados1, dados2)  # pyplot gerencia a figura e o eixo


# Exibindo o gráfico
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


# Criando os dados
dados = {
    'Produto': ['A', 'B', 'C'],
    'qtde_vendida': [33, 50, 45]
}


# Criando o DataFrame
df = pd.DataFrame(dados)


# Criando um gráfico de barras
df.plot(
    x='Produto',
    y='qtde_vendida',
    kind='bar'
)

plt.show()


# Criando um gráfico de pizza
df.plot(
    x='Produto',
    y='qtde_vendida',
    kind='pie'
)

plt.show()


# Criando um gráfico de linhas
df.plot(
    x='Produto',
    y='qtde_vendida',
    kind='line'
)

plt.show()