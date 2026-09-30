import seaborn as sns
import matplotlib.pyplot as plt


# Definindo o estilo dos gráficos
# Opções: darkgrid, whitegrid, dark, white, ticks
sns.set(style="whitegrid")


# Carregando o conjunto de dados "tips"
df_tips = sns.load_dataset('tips')


# Criando uma figura com 3 gráficos
fig, ax = plt.subplots(1, 3, figsize=(15, 5))


# Gráfico 1 - Média dos valores
sns.barplot(
    data=df_tips,
    x='sex',
    y='total_bill',
    ax=ax[0]
)


# Gráfico 2 - Soma dos valores
sns.barplot(
    data=df_tips,
    x='sex',
    y='total_bill',
    ax=ax[1],
    estimator=sum
)


# Gráfico 3 - Quantidade de registros
sns.barplot(
    data=df_tips,
    x='sex',
    y='total_bill',
    ax=ax[2],
    estimator=len
)


# Ajustando o espaço entre os gráficos
plt.tight_layout()


# Exibindo os gráficos
plt.show()