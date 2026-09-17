notas = []

calculo_de_notas = input("Deseja do calcular a nota do seu aluno (sim/nao)")

while calculo_de_notas == "sim":
    if calculo_de_notas == "sim":
        add_nota = int(input("Informe o nota do aluno: "))
        notas.append(add_nota)
        calculo_de_notas = input("deseja calcular outra nota do aluno (sim/nao)")
    else:
        print(notas)







