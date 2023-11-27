produto_bar = ('Cerveja', 'Velho barrero', '51', 'Timotina', 'Cachaça da mata', 'Linguiça', 'Fritas', 'Ovo', 'Torresmo', 'Salaminho')
precos_bar = (7.99, 2.00, 2.00, 2.00, 2.00, 1.50, 14.99, 1.50, 1.50, 2.00)

mesas = {}

while True:
    try:
        numero_mesa = int(input('\nDigite o número da mesa (ou 0 para sair): '))
    except ValueError:
        print('Digite um número válido.')
        continue
    
    if numero_mesa == 0:
        break
    
    if numero_mesa not in mesas:
        # Cria uma nova mesa se não existir
        mesas[numero_mesa] = {'pedidos': [], 'precos': []}

    while True:
        print('\nComanda:')
        for item, preco in zip(mesas[numero_mesa]['pedidos'], mesas[numero_mesa]['precos']):
            print(f"{item} - R${preco:.2f}")

        print(f"\nPreço total: R${sum(mesas[numero_mesa]['precos']):.2f}")

        print('\nMenu:')
        for i, produto in enumerate(produto_bar, start=1):
            print(f'{i}. {produto:<20}R$ {precos_bar[i - 1]:.2f}')

        print('\nEscolha uma operação:\n'
              '1. Adicionar item na mesa\n'
              '2. Remover item da mesa\n'
              '3. Encerrar mesa\n'
              '0. Sair\n')

        try:
            operacao = int(input('Opção: '))
        except ValueError:
            print('Digite uma opção válida.')
            continue
        
        if operacao == 0:
            break

        elif operacao == 1:
            try:
                escolha_produto = int(input('Escolha um item para adicionar (ou 0 para cancelar): '))
                if escolha_produto >= 1 and escolha_produto <= 10:
                    inserir_produto = produto_bar[escolha_produto - 1]
                    inserir_preco = precos_bar[escolha_produto - 1]

                    # Adiciona o item e preço à lista de pedidos e preços da mesa
                    mesas[numero_mesa]['pedidos'].append(inserir_produto)
                    mesas[numero_mesa]['precos'].append(inserir_preco)
                else:
                    print('Opção inválida. Tente novamente.')
            except ValueError:
                print('Digite um número válido.')

        elif operacao == 2:
            try:
                escolha_remover = int(input('Escolha um item para remover (ou 0 para cancelar): '))
                if escolha_remover >= 1 and escolha_remover <= len(mesas[numero_mesa]['pedidos']):
                    # Remove o item tanto da lista de pedidos quanto da lista de preços da mesa
                    del mesas[numero_mesa]['pedidos'][escolha_remover - 1]
                    del mesas[numero_mesa]['precos'][escolha_remover - 1]
                else:
                    print('Opção inválida. Tente novamente.')
            except ValueError:
                print('Digite um número válido.')

        elif operacao == 3:
            print('\nComanda Finalizada:')
            for item, preco in zip(mesas[numero_mesa]['pedidos'], mesas[numero_mesa]['precos']):
                print(f'{item} - R${preco:.2f}')

            print(f'\nTotal a ser pago: R${sum(mesas[numero_mesa]['precos']):.2f}')
            # Remove a mesa do sistema
            del mesas[numero_mesa]
            break

        else:
            print('Opção inválida. Tente novamente.')