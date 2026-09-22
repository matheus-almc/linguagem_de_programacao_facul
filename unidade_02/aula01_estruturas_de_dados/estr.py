# Estrutura de dados - Strings
texto = "Explorando a diversidade de linguagens de programação com Python. matheus almeida egg kkkkk"
print(f"Tamanho do texto: {len(texto)}")

print(f"Python in texto: {'Python' in texto}")

print(f"quantidade de do mesmo elemento no texto: {texto.count('o')}")

print(f"as 5 primeiras letras sao: {texto[:10]}")

print("  ")

# tuplas

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"tipo do objeto vogais: {type(vogais)}")
for p, x in enumerate(vogais):
 
 print(f"Posição = {p}, valor = {x}")