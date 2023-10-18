# 17. Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive).

# i = 0
# while i < 80:
#     num = int(input('Digite um número: '))
#     if num >= 10 and num <= 150:
#         print(num, 'Está no intervalo')
# i += 1


# 18. Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de
# idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.

# i = 0
# while i <= 75:
#    idade = int(input('Digite uma idade: ')) 
#    if idade >= 18:
#        print('{} é maior de idade'.format(idade))
#    else:
#        print('{} É menor de idade'.format(idade))
# i +=1

# 19. Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e se ela é homem ou mulher. No
# final informe total de homens e de mulheres.

# i = 0
# f = 0
# m = 0
# while i < 56:
#     sexo = input('Digite "M" para Homem e "F" para Mulher ')
#     if sexo == 'F' or sexo == 'f':
#         f += 1
#         print('Total de Homens: {} e total de mulheres: {}'.format(m, f))

#     elif sexo == 'm' or sexo == 'M':
#         m += 1
#         print('Total de Homens: {} e total de mulheres: {}'.format(m, f))
#     i += 1

#21. Escrever um algoritmo que leia os dados de “N” pessoas (nome, sexo, idade e saúde) e informe se está apta ou não
#para cumprir o serviço militar obrigatório. Informe os totais.

# n=0
# while n==0:
#     nome=input('Seu nome: ')
#     sexo=int(input('Digite 1 para Masc e 2 para Fem: '))
#     idade=int(input('Digite sua idade: '))
#     saude=int(input('COMO ESTÁ A SUA SAÚDE: Digite 1 para Bom e 0 para ruim: '))
#     if (sexo==1) and (idade>=17) and (idade<=22) and (saude==1):
#         print('Você está apto para cumprir com o serviço militar')
#     else:
#         print('Você não poderá participar do serviço militar')


#22. screver um algoritmo que leia o nome e o sexo
#de 56 pessoas e informe o nome e se ela é homem ou mulher
#No final informe total de homens e de mulheres

#Faça um algoritmo que receba o preço de custo e o preço de venda de 40 produtos. Mostre como resultado se
#houve lucro, prejuízo ou empate para cada produto. Informe media de preço de custo e do preço de venda.

# p=0
# while p <=40:
#     precocusto=float(input('Preço de custo '))
#     precovenda=float(input('Preço de venda '))
#     if precocusto<precovenda:
#         print('Você obteve lucro ')
#     elif precocusto<precovenda:
#         print('Você teve prejuízo ')
#     else:
#         print('Você não obteve lucro nem prejuízo! ')
# p+=1

#23. Faça um algoritmo que receba um número e mostre uma mensagem caso este número sege maior que 80, menor
#que 25 ou igual a 40

# n=float(input('Digite um número: '))
# if (n>80) or (n<25) or (n==40):
#     print("Este número está no intervalo")

#24. Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número.

# n=0
# while n==0:
#     num=float(input('Digite um número: '))
#     if num>0:
#         print('numero positivo! ')
#     elif num<0:
#         print('Numero negativo! ')
#     else:
#         print('Numero zero')