# def escrito():
#     print('Mensagem')

# def escrito2(mensagem):
#     print(mensagem)

# escrito()

# nome=input('Digite seu nome: ')
# escrito2('Olá %s' % (nome))

# def soma(a,b):
#     resultado=a+b
#     print(resultado)

# def multiplicar(a,b):
#     resultado=a*b
#     print(resultado)

# def subtrair(a,b):
#     resultado=a+b
#     print(resultado)

# def dividir(a,b):
#     if b=!0:
#       resultado=a/b
#       print(resultado) 
#     else:
#       print('Divisão por 0 não é possível!!!')

# e=int(input('1-Soma\n2-Multiplicação\n3-Subtração\n4-Divisão\nEscolha uma opção: '))
# n1=int(input('Digite um número inteiro: '))
# n2=int(input('Digite um número inteiro: '))

# if e==1:
#     soma(n1,n2)
# elif e==2:
#     multiplicar(n1,n2)
# elif e==3:
#     subtrair(n1,n2)
# elif e==4:
#     dividir(n1,n2)
# else:
#     print('Opção Inválida')

# def soma(a,b):
#     resultado=a+b
#     return resultado

# def multiplicar(a,b):
#     resultado=a*b
#     return resultado

# def subtrair(a,b):
#     resultado=a-b
#     return resultado

# def dividir(a,b):
#     if b=!0:
#       resultado=a/b
#       return resultado
#     else:
#       print('Divisão por 0 não é possível!!!')

# def pedirnum():
#     n=int(input('Digite um número inteiro: '))
#     return n

# import funcao

# a=True

# while a:
#     e=int(input('1-Soma\n2-Multiplicação\n3-Subtração\n4-Divisão\n9-Encerrar\nEscolha uma opção: '))

#     if e==1:
#         n1=funcao.pedirnum()
#         n2=funcao.pedirnum()
#         resultado=funcao.soma(n1,n2)
#         print(resultado)
#     elif e==2:
#         n1=funcao.pedirnum()
#         n2=funcao.pedirnum()
#         resultado=funcao.multiplicar(n1,n2)
#         print(resultado)
#     elif e==3:
#         n1=funcao.pedirnum()
#         n2=funcao.pedirnum()
#         resultado=funcao.subtrair(n1,n2)
#         print(resultado)
#     elif e==4:
#         n1=funcao.pedirnum()
#         n2=funcao.pedirnum()
#         resultado=funcao.dividir(n1,n2)
#         print(resultado)
#     elif e==9:
#         print('Programa Encerrado')
#         a=False
#     else:
#         print('Opção Inválida')   

# def soma(a,b):
#     global resultado
#     resultado=a+b

# def multiplicar(a,b):
#     global resultado
#     resultado=a*b

# def subtrair(a,b):
#     global resultado
#     resultado=a-b

# def dividir(a,b):
#         global resultado
#         resultado=a/b

# def pedirnum():
#     n=int(input('Digite um número inteiro: '))
#     return n

# resultado=0
# a=True
        
# while a:
#     e=int(input('1-Soma\n2-Multiplicação\n3-Subtração\n4-Divisão\n9-Encerrar\nEscolha uma opção: '))
#     if e>=1 and e<=4:
#         n1=pedirnum()
#         n2=pedirnum()
#         if n2!=0:
#             if e==1:
#                 soma(n1,n2)
#             elif e==2:
#                 multiplicar(n1,n2)
#             elif e==3:
#                 subtrair(n1,n2)
#             elif e==4:
#                 dividir(n1,n2)
#             print(resultado)
#         else:
#             print('Não é possível dividir por 0!!!')
#     elif e==9:
#             print('Programa Encerrado')
#             a=False
#     else:
#             print('Opção Inválida') 
      

# def teste(*parametros):
#     resultado=0
#     for valor in parametros:
#         resultado+=valor
#     print('Resultado %f' % (resultado))

# teste(2,3,1,5,6)

# def teste(a,b,c=0):
#     resultado=a+b+c
#     print('A soma é: %f' % (resultado))

# teste(1,2)
# teste(3,4,5)

# def parOuimpar(a):
#     if a%2==0:
#         print('Par')
#     else:
#         print('ímpar')

# def exibir_mensagem(mensagem):
#     print(mensagem)

# def fatorial(num):
#     if num==0 or num==1:
#         print("Foguete")
#         return 1
#     else:
#         return num * fatorial(num-1)

# num=int(input('Digite um número: '))
# resultado=fatorial(num)
# print(resultado)

# def contagem(segundos):
#     if segundos == 0:
#         print("DECOLAR!")
#     else:
#         print(segundos)
#         contagem(segundos - 1)

# segundos=int(input('Digite a quantidade de segundos: '))
# contagem(segundos)

# def soma_pares(n):
#     if n <= 1:
#         return 0
#     elif n % 2 == 0:
#         return n + soma_pares(n - 2)
#     else:
#         return soma_pares(n - 1)

# n=int(input('Digite um número: '))
# resultado = soma_pares(n)
# print(f"A soma dos números pares até {n} é {resultado}")
   
# for i in range(1,3+1,1):
#     print(i)

# def soma_pares(n):
#     total = 0
#     for num in range(2, n + 1, 2):
#         total += num
#     return total


# valor_de_n = 6
# resultado = soma_pares(valor_de_n)
# print(f"A soma dos números pares de 2 até {valor_de_n} é {resultado}")

# def contardiviseis(divisor, inicio, fim):
    # Caso base: quando chegamos ao fim do intervalo
    # if inicio > fim:
    #     return 0
    
    # Verificar se o número atual é divisível pelo divisor
    # if inicio % divisor == 0:
    #     return 1 + contardiviseis(divisor, inicio + 1, fim)
    # else:
    #     return contardiviseis(divisor, inicio + 1, fim)

# Exemplo de uso
# divisor = int(input("Digite o número divisor: "))
# inicio_intervalo = int(input("Digite o início do intervalo: "))
# fim_intervalo = int(input("Digite o fim do intervalo: "))

# resultado = contardiviseis(divisor, inicio_intervalo, fim_intervalo)
# print(f"Existem {resultado} números divisíveis por {divisor} no intervalo de {inicio_intervalo} a {fim_intervalo}.")

# def contar(divisor, fim):
#     if fim<1:
#         return 0
#     elif fim % divisor==0:
#         print(fim)
#         return 1 + contar(divisor, fim-1)
#     else:
#         return 0 + contar(divisor, fim-1)
    
# a=contar(5,50)
# print(a)

# def euro(a):
#     return a*5.38
# def dolar(a):
#     return a*4.89

# moeda=int(input('1-Euro\n2-Dólar\nEscolha uma opção: '))
# reais=float(input('Digite a quantidade de reais: '))

# if moeda==1:
#     vl_conversao=euro(reais)
#     print('Valor em Euro: %f' % (vl_conversao))
# elif moeda==2:
#     vl_conversao=dolar(reais)
#     print('Valor em Dólar: %f' % (vl_conversao))
# else:
#     print('Opção inválida')

# def parimpar(num):
#     if num%2==0:
#         return 'Par'
#     else:
#         return 'Ímpar'

# num=int(input('Digite um número: '))

# print(parimpar(num))