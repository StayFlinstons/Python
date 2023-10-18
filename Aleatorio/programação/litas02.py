# ESCREVA UM PROGRAMA ONDE O USUÁRIO 
# DIGITARÁ A TEMPERATURA MEDIDA EM 
# FAHRENHEIT E O PROGRAMA MOSTRARÁ O 
# VALOR EM CELSIUS

# temp = float(input('Digite uma temperatura em CELSIUS: '))
# print(f'Você digitou a temperatura: {temp}, convertido para Fahrenheit: {(temp*1.8)+32}')

# ESCREVA UM PROGRAMA QUE CALCULA O 
# QUADRADO, O CUBO E A RAIZ QUADRADA DE 
# UM NÚMERO DIGITADO PELO USUÁRIO

# num = float(input('Digite um número: '))
# print(f'Quadrado: {num**2}\nCubo: {num**3}\nRaiz: {num**(1/2)}')

# ESCREVA UM PROGRAMA QUE CALCULA A ÁREA 
# E O VOLUME DE UM CUBO QUE TENHA UMA 
# ARESTA QUE SERÁ FORNECIDA PELO USUÁRIO.

# ld1 = float(input('Digite um valor: '))
# ld2 = float(input('Digite um valor: '))
# aresta = float(input('Digite um valor: '))
# print(f'Área: {ld1*ld2}, Volume: {aresta**3}')

# ESCREVA UM PROGRAMA QUE LÊ UMA 
# VELOCIDADE EM KM/H DO TECLADO E 
# RETORNA NA TELA O VALOR DA VELOCIDADE 
# EM MPH (MILHAS POR HORA).

# km = float(input('Digite uma velocidade em KM/H: '))
# print(f'Velocidade em MPH: {km/1.609}')

# O USUÁRIO DIGITARÁ A COTAÇÃO DO DÓLAR 
# EM REAIS E UM VALOR QUALQUER EM DÓLARES, 
# E O PROGRAMA IRÁ CONVERTER PARA REAIS.

# cotacao = float(input('Digite a cotação do dolar: '))
# reais = float(input('Digite um valor em reais: '))
# print(f'Convertendo reais em dolar: {reais*cotacao}')

# ESCREVA UM PROGRAMA QUE LEIA TRÊS 
# VALORES INTEIROS E DIFERENTES E MOSTRE-OS 
# EM ORDEM DECRESCENTE.

# valor1 = float(input("Digite o primeiro valor: "))
# valor2 = float(input("Digite o segundo valor: "))
# valor3 = float(input("Digite o terceiro valor: "))

# valores = [valor1, valor2, valor3]
# valores_de = sorted(valores, reverse=True)

# print("Valores em ordem decrescente:", valores_de)

# TENDO COMO DADOS DE ENTRADA A ALTURA E O 
# SEXO DE UMA PESSOA, CONSTRUA UM PROGRAMA 
# QUE CALCULE SEU PESO IDEAL, UTILIZANDO AS 
# SEGUINTES FÓRMULAS:
# • PARA HOMENS: (72.7 * H) - 58;
# • PARA MULHERES: (62.1 * H) – 44.7

# a = float(input('Digite a altura: '))
# sexo = input('Digite se é homem ou mulher > H/M: ')
# sm = sexo.upper()

# if sm == 'H':
#     print(f'Peso ideal: {(72.7*a)-58}')
    
# else:
#     print(f'Peso ideal: {(62.1*a)-44.7}')

# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE 
# UMA PESSOA, CALCULE E MOSTRE SUA IDADE E, TAMBÉM, 
# VERIFIQUE E MOSTRE SE ELA JÁ TEM IDADE PARA VOTAR (16 
# ANOS OU MAIS) E PARA CONSEGUIR A CARTEIRA DE 
# HABILITAÇÃO (18 ANOS OU MAIS).

# ano = int(input("Digite o ano de nascimento: "))
# atual = 2023  
# idade = atual - ano
# votar = idade >= 16
# dirigir = idade >= 18

# print("Idade:", idade, "anos")

# if votar:
#     print("Pode votar (16 anos ou mais)")
# else:
#     print("Não pode votar ainda (menos de 16 anos)")

# if dirigir:
#     print("Pode obter a carteira de habilitação (18 anos ou mais)")
# else:
#     print("Não pode obter a carteira de habilitação ainda (menos de 18 anos)")

# ESCREVA UM PROGRAMA QUE LEIA O CÓDIGO DE UM DETERMINADO 
# PRODUTO E MOSTRE A SUA CLASSIFICAÇÃO. UTILIZE A SEGUINTE TABELA 
# COMO REFERÊNCIAS:

# codigo = int(input('Digite o código do produto: '))

# if codigo == 1:
#     print('Alimento não-perecível')
# elif codigo == 2 or 3 or 4:
#     print('Alimento perecível')
# elif codigo == 5 or 6:
#     print('Vestuário')
# elif codigo == 7:
#     print('Higiene pessoal')
# elif codigo >= 8 and codigo <= 15:
#     print('Limpeza e utensílios domésticos')
# else:
#     print('Código inválido')

# O IMC – ÍNDICE DE MASSA CORPORAL É UM CRITÉRIO DA ORGANIZAÇÃO 
# MUNDIAL DA SAÚDE PARA DAR UMA INDICAÇÃO SOBRE A CONDIÇÃO DE 
# PESO DE UMA PESSOA ADULTA. A FÓRMULA É IMC = PESO / (ALTURA)². 
# ELABORE UM PROGRAMA QUE LEIA O PESO E A ALTURA DE UM ADULTO E 
# MOSTRE A SUA CONDIÇÃO.

# peso = float(input("Digite o peso (kg): "))
# altura = float(input("Digite a altura (metros): "))
# imc = peso / (altura ** 2)

# if imc < 18.5:
#     condicao = "Abaixo do peso"
# elif imc > 18.5 or imc <=25:
#     condicao = "Peso normal"
# elif imc >25 or imc <=30:
#     condicao = "Acima do peso"
# elif imc > 30:
#     condicao = "Obeso"
    
# print("IMC:", imc)
# print("Condição de peso:", condicao)

# • ANACLETO TEM 1,50 METRO E CRESCE 2 
# CENTÍMETROS POR ANO, ENQUANTO 
# FELISBERTO TEM 1,10 METRO E CRESCE 3 
# CENTÍMETROS POR ANO. CONSTRUA UM 
# PROGRAMA QUE CALCULE E IMPRIMA 
# QUANTOS ANOS SERÃO NECESSÁRIOS PARA 
# QUE FELISBERTO SEJA MAIOR QUE ANACLETO.

# altura_anacleto = 150
# crescimento_anacleto = 2

# altura_felisberto = 110
# crescimento_felisberto = 3

# anos = 0

# while altura_felisberto <= altura_anacleto:
#     altura_anacleto += crescimento_anacleto
#     altura_felisberto += crescimento_felisberto
#     anos += 1

# print(f"Serão necessários {anos} anos para que Felisberto seja maior que Anacleto.")

