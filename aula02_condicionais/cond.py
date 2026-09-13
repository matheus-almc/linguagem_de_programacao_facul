chovendo = input("Esta chovendo ?? (sim/nao)")

if chovendo == "sim":
    print("Esta chovendo sim")
else:
    print("Esta chovendo nao")

idade = int(input("informe a sua idade bebe"))

if idade < 18:
    print("Voce é um bebe")
elif idade >= 18 and idade < 65:
    print("Ta na hora de aprender errando meu jovem adulto")
else:
    print("Nunca e tarde pra nada meu velho")

quantidade_ingressos = 10

if quantidade_ingressos > 0:
    print("Ingressos estão disponíveis.")
else:
    print("Todos os ingressos estão esgotados.")