#Variavel lista que armazena as notas
notas = []

#Variavel que atribui o nome do aluno
nomeDoAluno = input("insira o nome do aluno: ")

#variavel que armazena a condicao do da estrutura de repeticao while
calculo_de_notas = input("Deseja do calcular a nota do seu aluno (sim/nao) ")

#estrutura de repetição que continua enquanto calculo_de_notas for igual a "sim"
while calculo_de_notas == "sim":

        #Variavel que armazena a nota do aluno
        add_nota = int(input("Informe o nota do aluno: "))

        #metodo que adiciona o valor da variavel add_nota lista notas
        notas.append(add_nota)

        #atualiza a variável que controla a repetição
        calculo_de_notas = input("deseja calcular outra nota do aluno (sim/nao): ")

#funcao para calcular a media da nota
def calcular_media(notas):
        total = sum(notas)
        quantidade = len(notas)
        return total / quantidade

#funcao para aprovacao da nota
def aprovacao(media):
        if media >= 7:
                return "Aprovado"
        else:
               return "Reprovado"


#verifica se a lista notas possui elementos
if notas:

#variavel que armazena o retorno da funcao calcular_notas
 media = calcular_media(notas)

#variavel que armazena o retorno da funcao aprovacao
 resultado = aprovacao(media)

#print que exibe o final do algoritimo e a saida dos dados
 print(
        f"Aluno: {nomeDoAluno}\n"
        f"Nota do aluno: {notas}\n"
        f"media do aluno: {media}\n"
        f"Resultado do aluno: {resultado}\n"
)

#condicional caso nao tenha nenhum elemento na lista notas
else:
 print("nenhuma nota registrada")










