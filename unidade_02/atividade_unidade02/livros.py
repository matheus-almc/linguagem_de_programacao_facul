# ============================================================
# SISTEMA SIMPLES DE BIBLIOTECA
# ============================================================
# Este programa permite:
# 1. Criar livros usando uma classe
# 2. Cadastrar livros em uma lista
# 3. Listar todos os livros cadastrados
# 4. Buscar um livro pelo título
# 5. Gerar um gráfico mostrando a quantidade de livros por gênero
# ============================================================


# ------------------------------------------------------------
# IMPORTANDO A BIBLIOTECA MATPLOTLIB
# ------------------------------------------------------------
# O matplotlib é uma biblioteca utilizada para criar gráficos.
#
# "pyplot" possui várias funções para criar e configurar
# gráficos.
#
# O "as plt" é um apelido. Assim podemos escrever plt
# em vez de matplotlib.pyplot.
# ------------------------------------------------------------

import matplotlib.pyplot as plt


# ============================================================
# PASSO 1 - DEFININDO A CLASSE LIVRO
# ============================================================

# Uma classe funciona como um "molde".
#
# Nesse caso, a classe Livro será o molde que vamos utilizar
# para criar vários livros diferentes.


class Livro:

    # --------------------------------------------------------
    # Método construtor
    # --------------------------------------------------------
    # O método __init__ é executado automaticamente quando
    # criamos um novo objeto Livro.
    #
    # Exemplo:
    #
    # livro1 = Livro("Harry Potter", "J.K. Rowling",
    #                "Fantasia", 5)
    #
    # Nesse momento o __init__ será executado.
    # --------------------------------------------------------

    def __init__(self, titulo, autor, genero, quantidade):

        # self.titulo guarda o título do livro
        self.titulo = titulo

        # self.autor guarda o nome do autor
        self.autor = autor

        # self.genero guarda o gênero do livro
        self.genero = genero

        # self.quantidade guarda quantos exemplares
        # desse livro estão disponíveis
        self.quantidade = quantidade


# ============================================================
# PASSO 2 - CRIANDO A LISTA DE LIVROS
# ============================================================

# Criamos uma lista vazia.
#
# Essa lista será utilizada para armazenar os objetos
# da classe Livro que forem cadastrados.

livros = []


# ============================================================
# PASSO 3 - FUNÇÃO PARA CADASTRAR UM LIVRO
# ============================================================

def cadastrar_livro():

    # Pedimos ao usuário o título do livro.
    titulo = input("Digite o título do livro: ")

    # Pedimos o nome do autor.
    autor = input("Digite o autor do livro: ")

    # Pedimos o gênero.
    genero = input("Digite o gênero do livro: ")

    # Pedimos a quantidade.
    #
    # O input() sempre retorna texto (string).
    # Como precisamos trabalhar com números,
    # utilizamos int() para transformar o texto em inteiro.
    quantidade = int(input("Digite a quantidade disponível: "))

    # Criamos um novo objeto da classe Livro.
    novo_livro = Livro(titulo, autor, genero, quantidade)

    # Adicionamos o novo livro dentro da lista "livros".
    livros.append(novo_livro)

    # Informamos ao usuário que o cadastro foi realizado.
    print("\nLivro cadastrado com sucesso!")


# ============================================================
# PASSO 3 - FUNÇÃO PARA LISTAR TODOS OS LIVROS
# ============================================================

def listar_livros():

    # Primeiro verificamos se a lista está vazia.
    if len(livros) == 0:

        print("\nNenhum livro cadastrado.")

        # return encerra a função neste ponto.
        return

    # Se chegamos aqui, significa que existe pelo menos
    # um livro cadastrado.

    print("\n========== LIVROS CADASTRADOS ==========")

    # Percorremos cada livro dentro da lista.
    #
    # Para cada repetição, a variável "livro" representa
    # um objeto da classe Livro.

    for livro in livros:

        print(f"\nTítulo: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Gênero: {livro.genero}")
        print(f"Quantidade disponível: {livro.quantidade}")

    print("\n========================================")


# ============================================================
# PASSO 3 - FUNÇÃO PARA BUSCAR UM LIVRO PELO TÍTULO
# ============================================================

def buscar_livro():

    # Pedimos ao usuário o título que deseja procurar.
    titulo_busca = input("\nDigite o título do livro que deseja buscar: ")

    # Percorremos todos os livros cadastrados.
    for livro in livros:

        # lower() transforma o texto em letras minúsculas.
        #
        # Isso permite fazer uma comparação sem se preocupar
        # com letras maiúsculas e minúsculas.
        #
        # Exemplo:
        #
        # "Harry Potter".lower()
        # resulta em:
        #
        # "harry potter"

        if livro.titulo.lower() == titulo_busca.lower():

            print("\n========== LIVRO ENCONTRADO ==========")

            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Gênero: {livro.genero}")
            print(f"Quantidade disponível: {livro.quantidade}")

            print("======================================")

            # Encontramos o livro, então podemos
            # encerrar a função.
            return

    # Se o for terminou sem encontrar nenhum livro,
    # chegamos aqui.

    print("\nLivro não encontrado.")


# ============================================================
# PASSO 4 - FUNÇÃO PARA GERAR O GRÁFICO
# ============================================================

def gerar_grafico():

    # Antes de criar o gráfico, verificamos se existem livros.

    if len(livros) == 0:

        print("\nNão existem livros cadastrados para gerar o gráfico.")

        return

    # --------------------------------------------------------
    # Criando um dicionário para armazenar os gêneros
    # --------------------------------------------------------
    #
    # A ideia será criar algo parecido com:
    #
    # {
    #     "Fantasia": 10,
    #     "Romance": 5,
    #     "Terror": 3
    # }
    #
    # O número representa a quantidade total de exemplares
    # disponíveis daquele gênero.
    # --------------------------------------------------------

    quantidade_por_genero = {}

    # Percorremos todos os livros cadastrados.

    for livro in livros:

        # Verificamos se o gênero do livro já existe
        # no nosso dicionário.

        if livro.genero in quantidade_por_genero:

            # Se já existe, somamos a quantidade desse livro
            # ao valor que já estava armazenado.

            quantidade_por_genero[livro.genero] += livro.quantidade

        else:

            # Se o gênero ainda não existe no dicionário,
            # criamos a chave e colocamos a quantidade
            # do primeiro livro daquele gênero.

            quantidade_por_genero[livro.genero] = livro.quantidade

    # --------------------------------------------------------
    # Separando os dados do dicionário
    # --------------------------------------------------------

    # Pegamos somente os nomes dos gêneros.
    generos = list(quantidade_por_genero.keys())

    # Pegamos somente as quantidades.
    quantidades = list(quantidade_por_genero.values())

    # --------------------------------------------------------
    # Criando o gráfico
    # --------------------------------------------------------

    # plt.bar() cria um gráfico de barras.
    #
    # O primeiro parâmetro representa o eixo X.
    # O segundo representa o eixo Y.

    plt.bar(generos, quantidades)

    # Define o título do gráfico.

    plt.title("Quantidade de Livros por Gênero")

    # Define o nome do eixo X.

    plt.xlabel("Gênero")

    # Define o nome do eixo Y.

    plt.ylabel("Quantidade de Livros")

    # Rotaciona os nomes dos gêneros para facilitar
    # a leitura caso sejam nomes grandes.

    plt.xticks(rotation=45)

    # Ajusta automaticamente os elementos do gráfico
    # para evitar que os textos fiquem cortados.

    plt.tight_layout()

    # Exibe o gráfico na tela.

    plt.show()


# ============================================================
# CRIANDO ALGUNS LIVROS PARA TESTE
# ============================================================

# Você pode apagar esta parte depois e cadastrar os livros
# manualmente pelo menu.

livro1 = Livro(
    "Harry Potter",
    "J.K. Rowling",
    "Fantasia",
    5
)

livro2 = Livro(
    "O Senhor dos Anéis",
    "J.R.R. Tolkien",
    "Fantasia",
    3
)

livro3 = Livro(
    "Dom Casmurro",
    "Machado de Assis",
    "Romance",
    4
)

livro4 = Livro(
    "It: A Coisa",
    "Stephen King",
    "Terror",
    2
)

# Adicionamos os livros criados na lista.

livros.append(livro1)
livros.append(livro2)
livros.append(livro3)
livros.append(livro4)


# ============================================================
# MENU PRINCIPAL
# ============================================================

# O while True cria um loop infinito.
#
# O menu continuará aparecendo até que o usuário escolha
# a opção "0 - Sair".

while True:

    print("\n")
    print("========================================")
    print("       SISTEMA DE BIBLIOTECA")
    print("========================================")

    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Gerar gráfico")
    print("0 - Sair")

    print("========================================")

    # Pegamos a opção escolhida pelo usuário.

    opcao = input("Digite uma opção: ")

    # --------------------------------------------------------
    # OPÇÃO 1
    # --------------------------------------------------------

    if opcao == "1":

        cadastrar_livro()

    # --------------------------------------------------------
    # OPÇÃO 2
    # --------------------------------------------------------

    elif opcao == "2":

        listar_livros()

    # --------------------------------------------------------
    # OPÇÃO 3
    # --------------------------------------------------------

    elif opcao == "3":

        buscar_livro()

    # --------------------------------------------------------
    # OPÇÃO 4
    # --------------------------------------------------------

    elif opcao == "4":

        gerar_grafico()

    # --------------------------------------------------------
    # OPÇÃO 0
    # --------------------------------------------------------

    elif opcao == "0":

        print("\nPrograma encerrado.")
        break

    # --------------------------------------------------------
    # QUALQUER OUTRA OPÇÃO
    # --------------------------------------------------------

    else:

        print("\nOpção inválida. Tente novamente.")