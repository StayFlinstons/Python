numero = int(input("Digite um número: "))
indice = 0

for i in range(1, numero):
    indice += 1
    if (numero / indice ) % 2 == 0:
        print(f"O número {numero} não é primo")
    else:
        print(f"O número {numero} é primo")