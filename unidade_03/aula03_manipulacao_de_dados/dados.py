import pandas as pd
import requests


# URL da API do Banco Central
url = (
    "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados"
    "?formato=json"
    "&dataInicial=01/01/2025"
    "&dataFinal=31/12/2025"
)


# Fazendo a requisição
resposta = requests.get(url)

# Verificando se houve erro
resposta.raise_for_status()

# Convertendo a resposta para JSON
dados = resposta.json()

# Criando o DataFrame
df_selic = pd.DataFrame(dados)

# Exibindo informações
print(df_selic.info())

# Mostrando os primeiros registros
print(df_selic.head())

from datetime import date
from datetime import datetime as dt

# Obtém a data atual
data_extracao = date.today()

# Adiciona a data de extração em uma nova coluna
df_selic['data_extracao'] = data_extracao

# Adiciona o responsável pela extração
df_selic['responsavel'] = "Autor"

# Exibe informações sobre o DataFrame
print(df_selic.info())

# Exibe as primeiras linhas
print(df_selic.head())

df_selic.loc[0]

# Resultado:
# data              04/06/1986
# valor              0.065041
# data_extracao      2023-11-02
# responsavel        Autor
# Name: 0, dtype: object


df_selic.loc[[0, 20, 70]]

# Resultado:
#
#     data        valor      data_extracao    responsavel
# 0   04/06/1986  0.065041   2023-11-02       Autor
# 20  02/07/1986  0.068301   2023-11-02       Autor
# 70  10/09/1986  0.131315   2023-11-02       Autor