# 13. Faça um algoritmo que receba um número e mostre uma mensagem caso este número seja maior que 10

# num = int(input('Digite um número: '))
# if num > 10:
#    print('Seu número é maior que 10')
#  else:
#      print('Seu número é menor que 10')

# 14. Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior.

# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite um número: '))
#  if num1 > num2:
#      print('O número {} é maior que {}' .format(num1, num2))
# else:
#     print('O número {} é maior que {}' .format(num2, num1))

# 15. Faça um algoritmo que receba um número e diga se este número está no intervalo entre 100 e 200.

#  num = int(input('Digite um número: '))
# if  (num>=100) and (num<=200):
#      print('O número {} está no intervalo entre 100 e 200'.format(num))
# else:
#     print('O número {} não está no intervalo entre 100 e 200'.format(num))

# 16. Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a sua
# média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e Recuperação
# (media entre 5.1 a 6.9).

# nome = input('Digite seu nome: ')
# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))
# media = (nota1+nota2+nota3)/3
# if media >=7:
#     print('{} sua média foi {}, aprovado!'.format(nome, media))
# elif media <=5 :
#     print('{} sua média foi {}, reprovado!'.format(nome, media))
# else:
#     print('{} sua média foi {}, recuperação!'.format(nome, media))

# 26. Faça um algoritmo que leia um número de 1 a 5 e escreva por extenso. Caso o usuário digite um número que não
# esteja neste intervalo, exibir mensagem: número inválido.

# num = int(input('Digite um número: '))
# if num == 1:
#     print('Um')
# elif num == 2:
#     print('Dois')
# elif num == 3:
#     print('Três')
# elif num == 4:
#     print('Quatro')
# elif num == 5:
#     print('Cinco')
# else:
#     print('Número inválido')

# 27. A concessionária de veículos “CARANGO” está vendendo os seus veículos com desconto. Faça um algoritmo que
# calcule e exiba o valor do desconto e o valor a ser pago pelo cliente. O desconto deverá ser calculado sobre o valor
# do veículo de acordo com o combustível (álcool – 25%, gasolina – 21% ou diesel –14%). Com valor do veículo zero
# encerra entrada de dados. Informe total de desconto e total pago pelos clientes.

# valor = float(input('Digite o valor: '))
# tipo = int(input('1 = Álcool, 2 = Gasolina, 3 = Diesel '))
# if tipo == 1:
#     valor = valor - (valor * 0.25)
#     print('Valor do veículo a álcool R${}'.format(valor))
# elif tipo == 2:
#     valor = valor - (valor * 0.21)
#     print('Valor do veículo a gasolina R${}'.format(valor))
# else:
#     valor = valor - (valor * 0.14)
#     print('Valor do veículo a diesel R${}'.format(valor))

# 28. Escrever um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários de acordo com os
# seguintes critérios:
# a) 50% para aqueles que ganham menos do que três salários mínimos;
# b) 20% para aqueles que ganham entre três até dez salários mínimos;
# c) 15% para aqueles que ganham acima de dez até vinte salários mínimos;
# d) 10% para os demais funcionários.

# sa_min = int(input('Digite quantos salário mínimo recebe: '))
# salario = float(input('Digite seu salario: '))
# if sa_min <= 3:
#     salario = salario * 1.5
#     print('Seu salário atual corresponde a R${}'.format(salario))
# elif (sa_min > 3) and  (sa_min <= 10):
#     salario = salario * 1.2
#     print('Seu salário atual corresponde a R${}'.format(salario))
# elif (sa_min > 10) and (sa_min <=20):
#     salario = salario * 1.15
#     print('Seu salário atual corresponde a R${}'.format(salario))
# else:
#     salario = salario * 1.10
#     print('Seu salário atual corresponde a R${}'.format(salario))

# 32. Dados três valores A, B e C, em que A e B são números reais e C é um caractere, pede-se para imprimir o resultado
# da operação de A por B se C for um símbolo de operador aritmético; caso contrário deve ser impressa uma
# mensagem de operador não definido. Tratar erro de divisão por zero.

# a  = int(input('Digite um número: '))
# b  = int(input('Digite um número: '))
# c  = input('Digite um caractere: ')
# if c == '+':
#     a = a + b
#     print(a)
# elif c == '-':
#     a = a - b
#     print(a)
# elif c == '/':
#     a = a / b
#     print(a)
# elif c == '*':
#     a = a * b
#     print(a)

# 34. A escola “APRENDER” faz o pagamento de seus professores por hora/aula. Faça um algoritmo que calcule e exiba o
# salário de um professor. Sabe-se que o valor da hora/aula segue a tabela abaixo:
# Professor Nível 1 R$12,00 por hora/aula
# Professor Nível 2 R$17,00 por hora/aula
# Professor Nível 3 R$25,00 por hora/aula

# aula = int(input('Quantas aulas: '))
# nivel = int(input('Professor nivel 1, 2 ou 3 '))
# if nivel == 1:
#     x = 12 * aula
#     print('Valor R${}'.format(x))
# elif nivel == 2:
#     x = 17 * aula
#     print('Valor R${}'.format(x))
# elif nivel == 3:
#     x = 25 * aula
#     print('Valor R${}'.format(x))

# 35. Elabore um algoritmo que, dada a idade de um nadador. Classifique-o em uma das seguintes categorias:
# Infantil A = 5 - 7 anos
# Infantil B = 8 - 10 anos
# juvenil A = 11- 13 anos
# juvenil B = 14 - 17 anos
# Sênior = 18 - 25 anos
# Apresentar mensagem “idade fora da faixa etária” quando for outro ano não contemplado.

# idade = int(input("Digite a idade do nadador: "))

# if idade >= 5 and idade <= 7:
#     categoria = "Infantil A"
# elif idade >= 8 and idade <= 10:
#     categoria = "Infantil B"
# elif idade >= 11 and idade <= 13:
#     categoria = "Juvenil A"
# elif idade >= 14 and idade <= 17:
#     categoria = "Juvenil B"
# elif idade >= 18 and idade <= 25:
#     categoria = "Sênior"
# else:
#     categoria = "Idade fora da faixa etária"

# print("O nadador está na categoria:", categoria)

# 36. Faça um algoritmo que calcule o valor da conta de luz de uma pessoa. Sabe-se que o cálculo da conta de luz segue
# a tabela abaixo:
# Tipo de Cliente Valor do KW/h
# 1 (Residência) 0,60
# 2 (Comércio) 0,48
# 3 (Indústria) 1,29

# tipo_cliente = int(input("Digite o tipo de cliente (1 - Residência, 2 - Comércio, 3 - Indústria): "))
# consumo_energia = float(input("Digite o consumo de energia em KW/h: "))

# if tipo_cliente == 1:
#     valor_kw_h = 0.60
#     valor_conta = consumo_energia * valor_kw_h
#     print("O valor da conta de luz é: R$", valor_conta)
# elif tipo_cliente == 2:
#     valor_kw_h = 0.48
#     valor_conta = consumo_energia * valor_kw_h
#     print("O valor da conta de luz é: R$", valor_conta)
# elif tipo_cliente == 3:
#     valor_kw_h = 1.29
#     valor_conta = consumo_energia * valor_kw_h
#     print("O valor da conta de luz é: R$", valor_conta)

# 38. Em um curso de Ciência da Computação a nota do estudante é calculada a partir de três notas atribuídas,
# respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. As notas variam, de 0
# a 10 e a nota final é a média ponderada das três notas mencionadas. A tabela abaixo fornece os pesos:
# Laboratório Peso 2
# Exame final Peso 5


# nota_laboratorio = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
# nota_avaliacao = float(input("Digite a nota da avaliação semestral (0 a 10): "))
# nota_exame_final = float(input("Digite a nota do exame final (0 a 10): "))

# peso_laboratorio = 2
# peso_exame_final = 5


# if nota_laboratorio < 0 or nota_laboratorio > 10 or nota_avaliacao < 0 or nota_avaliacao > 10 or nota_exame_final < 0 or nota_exame_final > 10:
#     print("Notas inválidas. Certifique-se de que estão no intervalo de 0 a 10.")
#     exit()
    
# nota_final = (nota_laboratorio * peso_laboratorio + nota_avaliacao + nota_exame_final * peso_exame_final) / (peso_laboratorio + peso_exame_final)

# print("A nota final do estudante é:", nota_final)
