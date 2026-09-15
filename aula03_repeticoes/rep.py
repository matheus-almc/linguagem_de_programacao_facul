# strings = ["poca", "bosta", "lixo", "pano"]
# numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "  "]
#
#
#
# for palavras in strings:
#     print(palavras)
#
# for numeros in numero:
#     print(numeros)


# number = int(input("digite um numero: "))
#
# while number != 0:
#     if number % 2 == 0:
#         print(f"O numero {number} é par")
#         number = int(input("digite um numero: "))
#     else:
#         print(f"O numero {number} é impar")
#         number = int(input("digite um numero: "))

# for x in range(9):
#     print(x)

# for y in range(1, 6):
#     print(y)

# for z in range(1, 11, 3):
#     print(z)

# for number in range(1, 11):
#     if number % 2 == 0:
#         print(f"primeiro par: {number}")
#         break

# for numero in range(1, 11):
#     if numero == 5:
#         continue
#
#     print(numero)

filmes = [
    "Filme1",
    "Filme2",
    "Filme3",
    "Filme4",
    "Filme5"
]

print("== Classificação de Filmes ==")

for filme in filmes:
    while True:
        classificacao = input(
            f"{filme} de 1 a 5? ou 0 para parar"
        )

        if classificacao == "0":
            print(f"{filme}: Interrompida")
        break

    classificacao = int(classificacao)

    if classificacao < 1 or classificacao > 5:
        print("digite um numero de 1 a 5")
        classificacao
    else:
        print(f"{filme} com classificacao {classificacao} estrelas\n")
        classificacao
        break

print("programa encerrado")
