# number = [1,2,4,5,6,7,8,"coco", True, False]
#
# comprimento = len(number)
#
# print(comprimento)
#
# # len() calcula o comprimento da lista ou array
#
# def soma(a,b):
#     resultado = a+b
#     return resultado
# print(soma(3,4))
#
# soma = lambda a,b: a+b
# print(soma(5,6))
#
# def ePar(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
# print(ePar(5))
#
# num = int(input("Digite um numero: "))
#
# if ePar(num):
#     print(f"{num} é um numero par")
# else:
#     print(f"{num} é um numero impar")
#
#



notas = [7.5, 8.0, 6.5, 9.0, 7.0]


def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media


arredondar_media = lambda media: round(media, 2)

media = calcular_media(notas)

media_arredondada = arredondar_media(media)


if media_arredondada >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"


print(notas)
print(media_arredondada)
print(situacao)