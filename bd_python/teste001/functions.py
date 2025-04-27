import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import Users
engine = create_engine("sqlite:///teste001/users.db")
Session = sessionmaker(engine)

def menu():
      while True:
            print("""
Escolha uma opção:
1. Inserir usuário
0. Sair
            """)
            options = input('Digite sua escolha: ')
            try:
                  if options == '1':
                        insert_users()
                  elif options == '0':
                        break
                  else:
                        print('Opção inválida! Tente novamente.')
            except ValueError:
                  print('Por favor, insira um número válido!')

def insert_users():
    session = Session()
    name_user = input('Nome: ').upper()
    position_user = input('Cargo: ').upper()
    account_active_user = input('Status: (1 - TRUE ou 2 - FALSE): ').strip().upper()

    if account_active_user == '1':
        account_active_user = True
    elif account_active_user == '2':
        account_active_user = False
    else:
        print('Valor inválido para status, insira "TRUE" ou "FALSE".')
        session.close()
        return

    try:
        if all([name_user, position_user, account_active_user is not None]):
            users = Users(name=name_user, position=position_user, account_active=account_active_user)
            session.add(users)
            session.commit()
            print(f'O usuário {name_user} foi cadastrado com sucesso!')
        else:
            print('É obrigatório preencher todos os campos!')
    except Exception as e:
        print(f'Erro ao inserir usuário: {e}')
        session.rollback()
    finally:
        session.close()

def delete_user():
     session = Session()
     id_user = int(input('Digite o ID: '))
