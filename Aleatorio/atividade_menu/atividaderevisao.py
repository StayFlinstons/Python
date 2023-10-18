def opcao1():
    nome = input('Qual seu nome? ')
    ano = input('Voce nasceu em que ano? ')
    print('Seu nome é {} e você tem {} anos'.format(nome, 2023 - int(ano)))

def opcao2():
    valor = input('Digite algo:')
    print('0 tipo primitivo desse valor e {}'.format(type(valor)))
    print('So tem espaço: {}'.format(valor.isspace()))
    print('É um número: {}'.format(valor.isnumeric()))
    print('É alfabético: {}'.format(valor.isalpha()))
    print('É alfanumerico: {}'.format(valor.isalnum()))
    print('Está em maiúsculo: {}'.format(valor.isupper()))
    print('Está em minúsculo: {}'.format(valor.islower()))
    print('Está capitalizado: {}'.format(valor.istitle()))
    
def opcao3():
    sinal = input('Qual a cor do sinal?')
    if sinal == 'verde': print('Aberto')
    elif sinal == 'amarelo': print('Atenção')
    else:
        print('Fechado')

def sair():
    print("Saindo do programa...")
    exit()

while True:
    print("===== MENU =====")
    print("1 - Nome")
    print("2 - Tipo primitivo")
    print("3 - Semáfaro")
    print("0 - Sair")
    print("================")

    opcao = input("Selecione uma opção: ")

    if opcao == '1':
        opcao1()
    elif opcao == '2':
        opcao2()
    elif opcao == '3':
        opcao3()
    elif opcao == '0':
        sair()
    else:
        print("Opção inválida. Digite uma opção válida.")
