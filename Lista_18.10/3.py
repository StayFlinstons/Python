# ESCREVA UM ALGORITMO QUE LEIA 50 VALORES EM UM VETOR 
# E ENCONTRE O MAIOR E O MENOR DELES. MOSTRE O 
# RESULTADO

lista = []
for i in range(50):
    numero = int(input(f'Digite o {i+1}° número: '))
    lista.append(numero)
    
print(f'Maior número digitado: {max(lista)}\nMenor número digitado: {min(lista)}')