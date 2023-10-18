# 1. Faça um algoritmo que receba dois números e exiba o resultado da sua soma

# a = input('Digite um número: ')
# b = input('Digite um número: ')
# print('Primeiro número: {} \nSegundo número: {}'.format(a, b))


# 2. Faça um algoritmo que receba dois números e ao final mostre a soma, subtração, multiplicação e a divisão dos
# números lidos

# a = float(input('Digite um número: '))
# b = float(input('Digite um número: '))
# print('Soma: {} \nSubtração: {}\nMutiplicação: {} \nDivisão: {}'.format((a+b), (a-b), (a*b), (a/b)))

# 3. Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total
# percorrida pelo automóvel e o total de combustível gasto.

# dis_total = float(input('Digite a distância total percorrida: '))
# consumo = int(input('Digite o consumo total: '))
# print('Consumo médio: {}'.format(dis_total/consumo))

# 4. Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no
# mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o
# seu nome, o salário fixo e salário no final do mês.


# nome = input('Digite seu nome: ')
# salario_fixo = float(input('Digite o salário fixo: '))
# total_vendas = float(input('Digite o total de vendas: '))
# print('Seu nome: {} \nSalário fixo: R${} \nSalário total: R${}'.format(nome, salario_fixo, ((salario_fixo*0.15)+salario_fixo+total_vendas)))

# 5. Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final
# informar o nome do aluno e a sua média (aritmética)

# nome = input('Digite seu nome: ')
# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# nota3 = float(input('Digite a terceira nota: '))
# print('Seu nome: {}, sua média: {:.2f}'.format(nome, (nota1+nota2+nota3)/3))

# 6. Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o
# valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.


# a = input('Digite um número: ')
# b = input('Digite um número: ')
# c = a
# a = b
# b = c
# print('Valor de a: {}, valor de b: {}'.format(a, b))

# 7. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é:
# F=(9*C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius


# c = float(input('Digite uma temperatura em Celsius: '))
# print('A conversão de Celsius para Fahrenheit é: {}'.format(((9*c+160)/5)))

# 8. Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar
# (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o
# usuário.


# dolar = float(input('Digite o valor do dolar hoje: '))
# quant_dolar = float(input('Digite seu saldo de dolar: '))
# print('Você tem ${} Dolar, em reais R${:.2f}'.format(quant_dolar, (dolar*quant_dolar)))

# 9. Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês.
#  Considere fixo o juro da poupança em 0,70% a. m


# valor_depositado = float(input('Valor depositado: '))
# print('Rendimento após um mês: {}'.format((valor_depositado*0.7+valor_depositado)))

# 10. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que
# receba um valor de uma compra e mostre o valor das prestações

# valor = float(input('Digite o valor da compra: '))
# print('Valor da pestação sem juros: {}'.format(valor/5))

# 11. Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de
# custo receberá um acréscimo de acordo com um percentual informado pelo usuário

# preco = float(input('Digite o preço do produto: '))
# acrescimo = float(input('Digite o valor do acréscimo: '))
# print('Valor do produto com acréscimo: {}'.format(((acrescimo/100)*preco+preco)))

# 12. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos
# impostos (aplicados, primeiro os impostos sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o
# resultado). Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um algoritmo que
# leia o custo de fábrica de um carro e informe o custo ao consumidor do mesmo.

# custo = float(input('Digite o custo de fábrica do carro: '))
# imposto = (custo * 0.45)+custo
# imposto2 = imposto * 0.28
# print('O custo total {}'.format(custo+imposto2))