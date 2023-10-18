# Faça um programa que leia o total de eleitores e o total de votos dos candidatos A, B e C. O programa deve calcular a porcentagem de votos de cada candidato, bem como a porcentagem de votos anulados. Por fim, o programa deverá indicar se haverá segundo turno e entre quais candidatos. Só haverá segundo turno se o primeiro candidato não obtiver 51% dos votos válidos.

eleitoresTOTAL = float(input('Digite o total de eleitores: '))

eleitoresA = float(input('Digite o total de eleitores A: '))
eleitoresB = float(input('Digite o total de eleitores B: '))
eleitoresC = float(input('Digite o total de eleitores C: '))

eleitoresA_Porcentagem = (eleitoresA / eleitoresTOTAL) * 100
eleitoresB_Porcentagem = (eleitoresB / eleitoresTOTAL) * 100
eleitoresC_Porcentagem = (eleitoresC / eleitoresTOTAL) * 100

votosInvalidos = ((eleitoresTOTAL - (eleitoresA + eleitoresB + eleitoresC)) / eleitoresTOTAL) * 100

if eleitoresA_Porcentagem < 51:
    print('Haverá um segundo turno do candidato A')
elif eleitoresB_Porcentagem < 51:
    print('Haverá um segundo turno do candidato B')
else:
    print('Haverá um segundo turno do candidato C')
