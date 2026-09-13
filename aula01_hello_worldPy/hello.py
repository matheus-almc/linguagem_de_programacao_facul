

#nome = "matheus almeida"
x = 10
nota = 8.0
fezInscricao = True

print("hello world!")
#print(nome)
print(x)
print(nota)
print(fezInscricao)

print(type(x))



print(type(nota))

print(type(fezInscricao))

nome = input()

print(f"seu nome é : {nome}")

print(type(nome))

nota_1 = int(input())
nota_2 = int(input())
nota_3 = int(input())
nota_4 = int(input())
nota_5 = int(input())

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

#observe que utilizamos a função int(), pois, sem ela, o Python entenderia que as notas seriam String
#condição para a aprovação do aluno.

if media >= 6:
    situacao = "aprovado"
    print(f"O aluno {nome} esta: {situacao}")
else :
    situacao = "reprovado"
    print(f"O aluno {nome} foi: {situacao}")
#dadas as notas, mostramos a média final e a situação do aluno.
print(media)
print(situacao)