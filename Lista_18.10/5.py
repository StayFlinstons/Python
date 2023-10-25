# FAÇA UM ALGORITMO QUE LEIA UMA SEQUÊNCIA DE 20 
# NÚMEROS E OS IMPRIMA NA ORDEM INVERSA À DA LEITURA.

lista = []
for i in range(20):
    numero = int(input(f'Digite o {i+1}° número: '))
    lista.append(numero)
    
print('Lista inversa:')
print(*list(reversed(lista)), sep=' - ', end=';')