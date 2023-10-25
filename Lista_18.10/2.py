# FAÇA UM ALGORITMO QUE LEIA 10 VALORES INTEIROS 
# ARMAZENANDO-OS EM UM VETOR E DEPOIS CALCULE A SOMA 
# E A MÉDIA DOS VALORES LIDOS E APRESENTE O RESULTADO NA 
# TELA.

lista = []
soma = 0
for i in range(10):
    numero = int(input(f'Digite o {i+1}° número: '))
    lista.append(numero)
    soma += numero

print('Lista', *lista, sep=' - ', end=';\n')
print(f'A soma dos números digitados: {soma}')
print(f'A Média dos números digitados: {soma/(i+1)}')
