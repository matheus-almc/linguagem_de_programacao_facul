# print(10 > 5)

# print(5 > 10)

# print(10 == 10)

# print(5 != 10)

#Guardanso informações em variáveis

idade = 18
eMaiorDeIdade = idade >= 18
print(eMaiorDeIdade)

print(True and True)

print(True or False)

idade = int(input('Qual a sua idade? '))
if idade < 18:
    print('recomendo o filme 1')
elif idade >= 18 and idade < 65:
    print('recomendo o filme 2')
else:
    print('recomendo o filme 3')

    quantidadesDeIngressos = 10

    if quantidadesDeIngressos > 0:
        print('ingresso disponível')
    else:
        print('ingresso indisponível')