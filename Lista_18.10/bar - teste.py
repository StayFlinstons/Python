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
        # Criar mesa
        mesas[numero_mesa] = {'pedidos': [], 'precos': []}
        print(f'Mesa {numero_mesa} criada.')

    while True:
        print(f'\nComanda da Mesa {numero_mesa}:')
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
              '4. Mudar de mesa\n'
              '0. Sair\n')

        try:
            operacao = int(input('Opção: '))
        except ValueError:
            print('Digite uma opção válida.')
            continue
        
        if operacao == 0:
            # Fechar programa
            break

        elif operacao == 1:
            # Adicionar item na mesa
            try:
                escolha_produto = int(input('Escolha um item para adicionar (ou 0 para cancelar): '))
                if escolha_produto >= 1 and escolha_produto <= 10:
                    inserir_produto = produto_bar[escolha_produto - 1]
                    inserir_preco = precos_bar[escolha_produto - 1]

                    mesas[numero_mesa]['pedidos'].append(inserir_produto)
                    mesas[numero_mesa]['precos'].append(inserir_preco)
                    
                    print(f'\nItem {inserir_produto} adicionado à Mesa {numero_mesa}.')
                else:
                    print('Opção inválida. Tente novamente.')
            except ValueError:
                print('Digite um número válido.')

        elif operacao == 2:
            # Remover item da lista
            try:
                escolha_remover = int(input('Escolha um item para remover (ou 0 para cancelar): '))
                if escolha_remover >= 1 and escolha_remover <= len(mesas[numero_mesa]['pedidos']):
                    
                    removido = mesas[numero_mesa]['pedidos'].pop(escolha_remover - 1)
                    preco_removido = mesas[numero_mesa]['precos'].pop(escolha_remover - 1)
                    print(f'\nItem {removido} removido da Mesa {numero_mesa}.')
                else:
                    print('Opção inválida. Tente novamente.')
            except ValueError:
                print('Digite um número válido.')

        elif operacao == 3:
            # Encerrar a mesa / fechar comanda
            print(f'\nComanda da Mesa {numero_mesa} Finalizada:')
            for item, preco in zip(mesas[numero_mesa]['pedidos'], mesas[numero_mesa]['precos']):
                print(f'{item} - R${preco:.2f}')

            print(f'\nTotal a ser pago: R${sum(mesas[numero_mesa]['precos']):.2f}')
            del mesas[numero_mesa]
            break

        elif operacao == 4:
            # Mudar a mesa / adicionar uma nova mesa
            try:
                nova_mesa = int(input('Digite o número da nova mesa: '))
                if nova_mesa != numero_mesa:
                    numero_mesa = nova_mesa
                    if numero_mesa not in mesas:
                        mesas[numero_mesa] = {'pedidos': [], 'precos': []}
                        print(f'\nVocê mudou para a Mesa {numero_mesa}.')
                    else:
                        print(f'Mesa {numero_mesa} já existe. Escolha uma mesa válida.')
                else:
                    print('Mesa existente.')
            except ValueError:
                print('Digite um número válido.')

        else:
            print('Opção inválida. Tente novamente.')