def teste(a):
    print(f'Decolando em: {a}')
    if a == 0:
        return print('Decolando!')
    else:
        teste(a-1)
        
a = int(input('Digite um numero para contagem: '))
teste(a)