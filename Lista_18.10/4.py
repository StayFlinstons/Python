# ESCREVER UM ALGORITMO QUE LEIA UMA QUANTIDADE 
# DESCONHECIDA DE NÚMEROS EM UM VETOR (NO MÁXIMO 
# 200) E CONTE QUANTOS DELES ESTÃO NOS SEGUINTES 
# INTERVALOS: [0,25], [26,50], [51,75] E [76,100]. 
# A ENTRADA DE DADOS DEVE TERMINAR QUANDO FOR LIDO 
# UM NÚMERO NEGATIVO OU MAIOR QUE 100. 

quantidade = int(input('Digite a quantaide de números na lista (No máximo 200): '))
lista = []

if quantidade > 200:
    quantidade = int(input('Ultrapassou o limite de 200, digite novamente: '))
else:
    for i in range(quantidade):
        numeros = int(input(f'Digite o {i+1}° número: '))
        lista.append(numeros)
        
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

for numero in lista:
    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1

print(f"Números no intervalo [0, 25]: {intervalo_0_25}")
print(f"Números no intervalo [26, 50]: {intervalo_26_50}")
print(f"Números no intervalo [51, 75]: {intervalo_51_75}")
print(f"Números no intervalo [76, 100]: {intervalo_76_100}")