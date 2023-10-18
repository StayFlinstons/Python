# Crie um programa que pergunte qual operação matemática o usuário deseja fazer (+, -, /, *) 
# e crie funções que faça o cálculo com a entrada de dois números e retorne o valor para o 
# usuário. 
# • O programa só deve encerrar quando o usuário desejar sair. 
# • A impressão do valor não pode ser feita na função e sim no programa principal. 

def soma(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a-b

def mult(a, b):
    return a*b

escolha = int(input('Selecione uma operação:\n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n0 - Sair\n'))

while True:
    if escolha >=1 and escolha <=4:
        numero1 = float(input('Escolha um número: '))
        numero2 = float(input('Escolha um número: '))

        if escolha == 1:
            print(f'Resultado: {soma(numero1, numero2)}')
        elif escolha == 2:
            print(f'Resultado: {sub(numero1, numero2)}')
        elif escolha == 3:
            print(f'Resultado: {div(numero1, numero2)}')
        elif escolha == 4:
            print(f'Resultado: {mult(numero1, numero2)}')
    elif escolha == 0:
        print('Programa encerrado.')
        break
    else:
        escolha = int(input('Escolha inválida, tente novamente: '))
        
# Crie funções para conversão de moeda, onde o usuário vai informar a moeda que deseja a 
# conversão e o valor em reais. 
# Euro 5,38
# Dólar 4,89

# def euro(a):
#     return a * 5.38

# def dolar(a):
#     return a * 4.89

# saldo = float(input('Digite seu saldo: '))
# escolha = int(input('Escolha: 1 - Dolar = R$5.38 ou 2 - Euro\n'))

# if escolha == 1:
#     print(dolar(saldo))
# else:
#     print(euro(saldo))
    
# 3. Crie uma função que verifica se um número é par ou ímpar.

# def ParImpar(a):
#     if a % 2 == 0:
#         print(F'O número {a} é par')
#     else:
#         print(F'O número {a} é impar')
        
# numero = int(input('Digite um número: '))
# ParImpar(numero)
