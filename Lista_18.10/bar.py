produto_bar = ('Cerveja', 'Velho barrero', '51', 'Timotina', 'Cachaça da mata', 'Linguiça', 'Fritas', 'Ovo', 'Torresmo', 'Salaminho')
precos_bar = (7.99, 2.00, 2.00, 2.00, 2.00, 1.50, 14.99, 1.50, 1.50, 2.00)

lista_pedidos = []
lista_precos = []

while True:
    print("\nComanda:")
    for for2, preco in zip(lista_pedidos, lista_precos):
        print(f"{for2} - R${preco:.2f}")

    print(f"Preço total: R${sum(lista_precos):.2f}")
    
    print('\nMenu:')
    for for1, produto in enumerate(produto_bar, start = 1):
        print(f'{for1}. {produto:<20}R$ {precos_bar[for1 - 1]:.2f}')

    print('0. Fechar pedido')
    comanda = int(input('Escolha um item (ou 0 para fechar): '))

    if comanda >=1 and comanda <=10:
        inserir_produtos = produto_bar[comanda - 1]
        inserir_precos = precos_bar[comanda - 1]

        lista_pedidos.append(inserir_produtos)
        lista_precos.append(inserir_precos)

    elif comanda == 0:
        print(f'Comanda finalizada, total pedido: {(lista_pedidos)} Preco total: R${sum(lista_precos):2}')
        break
    else:
        comanda = (int(input(f'O produto não está na, lista digite novamente\n{produto_bar}\n{precos_bar}\nDigite seu pedido ou 0 pra fechar: \n')))