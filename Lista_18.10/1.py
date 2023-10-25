# CRIE UM PROGRAMA ONDE O USUÁRIO PODE INSERIR 
# QUANTOS NÚMEROS QUISER EM UMA LISTA, ATÉ QUE ELE 
# NÃO QUEIRA MAIS EXECUTAR O PROGRAMA
# ° A CADA INSERÇÃO, VERIFICAR SE O ITEM EXISTE NA LISTA
# ° CASO NÃO EXISTA, ADICIONE NA LISTA E EXIBA UMA MENSAGEM
# ° CASO EXISTA, EXIBA UMA MENSAGEM QUE O NÚMERO JÁ EXISTE NA LISTA
# ° IMPRIMA A LISTA A CADA INTERAÇÃO

lista = []
while True:
    
    numero = int(input('Digite qualquer numero ou 0 para sair: '))
    if numero == 0:
        print('Programa finalizado!')
        break
    elif numero in lista:
        numero = int(input('Esse número já existe, digite novamente ou * para sair: '))
    elif numero != 0:
        lista.append(numero)
        print('Lista:')
        print(*lista, sep=' - ', end=';\n')