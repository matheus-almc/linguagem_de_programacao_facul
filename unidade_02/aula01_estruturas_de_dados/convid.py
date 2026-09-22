#Tupla de convidados
convidados = ("Matheus", "Almeida", "Egg", "Python",)

#lista de confirmados
confirmados = ["Matheus", "Almeida"]

#identificar quem ainda nao confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram presença:")
for pessoa in nao_confirmados:
    print(f"{pessoa} ainda não confirmou presença.")

# Enviar lembretes aos não confirmados    
print("\nEnviando lembretes aos não confirmados")