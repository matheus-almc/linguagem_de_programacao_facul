#criando um conjunto vazio
meu_conjunto = set()

#adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
meu_conjunto.add(40)
meu_conjunto.add(50)

#Imprimindo o conjunto
print("conjunto apos adicionar elementos: ", meu_conjunto)
print("  ")

#verificando se o elemento esta no conjunto
elemento = 20

if elemento in meu_conjunto:
    print(f"Elemento: {elemento} esta no conjunto!")
else:
    print(f"Elemento: {elemento} não está no conjunto!")

#Removendo elemento no conjunto
meu_conjunto.remove(20)

#imprimindo conjunto atualizado
print("conjunto apos remover elemento: 20 ", meu_conjunto)




