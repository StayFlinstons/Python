import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import Users
engine = create_engine("sqlite:///teste001/users.db")
Session = sessionmaker(engine)

def menu():
      while True:
            print("""
====================
Escolha uma opção:
1. Inserir usuário
2. Deletar usuário
3. Listar usuários
0. Sair
====================
 """)
            options = input('Digite sua escolha: ')
            try:
                  if options == '1':
                        insert_users()
                  elif options == '2':
                        delete_user()
                  elif options == '3':
                       list_all_users()
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

    try:
        if all([name_user, position_user]):
            users = Users(name=name_user, position=position_user)
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

    user = session.query(Users).filter(Users.id == id_user).first()
    if user:
         name = user.name
    else:
         name = None

    try:
        if id_user:
            users = session.query(Users).filter(Users.id==id_user).first()
            session.delete(users)
            session.commit()
            print(f'Usuário {name} deletado com sucesso!')
        else:
             print('É obrigatorio inserir um ID válido.')
    except Exception as e:
            print(f'Erro ao tentar deletar o usuário {name}')
            session.rollback()
    finally:
            session.close()

def list_all_users():
     session = Session()

     print('''
1. Listar todos os usuários
2. Listar um usuário por ID
                         ''')
     options = int(input('Digite sua escolha: '))

     if options == 1:
          try:
               dados = session.query(Users).all()
               for i in dados:
                    print(f'\nID: {i.id}\nUsuário: {i.name}\nCargo: {i.position}\nAtivo: {i.account_active}\n')
          except Exception as e:
                    print('Ocorreu um erro.')

     elif options ==2:
          id_user = int(input('Digite o ID: '))
          try:
               dados = session.query(Users).filter(Users.id == id_user)
               for i in dados:
                    print(f'\nID: {i.id}\nUsuário: {i.name}\nCargo: {i.position}\nAtivo: {i.account_active}\n')
          except Exception as e:
               print('Ocorreu um erro.')
     else:
          print('Opção inválida, digite novamente.')