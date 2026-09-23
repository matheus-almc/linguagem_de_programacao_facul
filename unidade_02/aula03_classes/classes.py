# Define uma classe chamada Pessoa.
# O metodo __init__  é um construtor, chamado quando um objeto da classe é criado.
# Ele inicializa os atributos da classe.

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

       # O metodo cumprimentar retorna uma saudação com o nome da pessoa.
    def cumprimentar(self):
            return f"ola meu nome é {self.nome}"

       # O metodo aniversário aumenta a idade da pessoa em 1.
    def aniversario(self):
            self.idade += 1

       # Cria uma instância da classe “Pessoa” com os valores “João”, 30 e “Masculino” para nome, idade e genero respectivamente
pessoa1 = Pessoa("Matheus almeida camargo", 30, "Masculino")

       # Chama o metodo “cumprimentar” na instância pessoa1 e imprime a saudação.
print(pessoa1.cumprimentar())

       # Acessa o atributo idade da instância pessoa1 e imprime sua idade.\
print(f"Idade: {pessoa1.idade}") #saida idade: 30

      # Chama o metodo “aniversário” na instância pessoa1 para aumentar sua idade em 1.
pessoa1.aniversario()

      # Acessa o atributo idade atualizado da instância pessoa1 e imprime a nova idade.
print(f"Nova idade: {pessoa1.idade}") # Saída: “Nova idade: 31”
