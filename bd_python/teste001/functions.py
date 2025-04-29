import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main import Users
engine = create_engine("sqlite:///teste001/users.db")
Session = sessionmaker(engine)

def run_app():
      while True:
            print("""
                  
====================
Escolha uma opção:
1. Inserir usuário
2. Deletar usuário
3. Listar usuários
4. Atualiar usuário
0. Sair
====================
                  
 """)
            options = input('Digite sua escolha: ')
            try:
                  if options == '1':
                        insert_user()
                  elif options == '2':
                        delete_user()
                  elif options == '3':
                       list_all_users()
                  elif options == '4':
                       update_user()
                  elif options == '0':
                        break
                  else:
                        print('Opção inválida! Tente novamente.')
            except ValueError:
                  print('Por favor, insira um número válido!')

def insert_user():
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
                    session.rollback()

     elif options ==2:
          id_user = int(input('Digite o ID: '))
          try:
               dados = session.query(Users).filter(Users.id == id_user)
               for i in dados:
                    print(f'\nID: {i.id}\nUsuário: {i.name}\nCargo: {i.position}\nAtivo: {i.account_active}\n')
          except Exception as e:
               print(f'Ocorreu um erro. {e}')
               session.rollback()
     else:
          print('Opção inválida, tente novamente.')

def update_user():
     session = Session()
     id_user = int(input('Digite o ID do usuário: '))

     dados = session.query(Users).filter(Users.id == id_user).first()

     options = input('''
Selecione o campo que deseja alterar:
                     
1. Nome
2. Cargo
3. Status
                     
''')
     
     if options == '1':
          try:
               name_user = input('Digite o novo nome de usuário: ')
               dados.name = name_user
               session.commit()
               print(f'Nome ({name_user}) alterado com sucesso!')
          except Exception as e:
               print(f'Ocorreu um erro. {e}')
               session.rollback()
     elif options == '2':
          try:
               position_user = input('Digite o novo cargo: ')
               dados.position = position_user
               session.commit()
               print(f'Cargo ({position_user}) alterado com sucesso!')
          except Exception as e:
               print(f'Ocorreu um erro. {e}')
               session.rollback()
     elif options == '3':
          try:
               status_user = input('''
                                   
1 - ATIVO
2 - INATIVO

''')
               if status_user not in ['1', '2']:
                    print('Opção inválida. Escolha 1 ou 2.')
               else:
                    if status_user == '1':
                         if dados.account_active:
                              print(f'O usuário {dados.name} já está ativo.')
                         else:
                              dados.account_active = True
                              session.commit()
                              print(f'O status do usuário {dados.name} foi atualiado para ATIVO')
                    elif status_user == '2':
                         if not dados.account_active:
                              print(f'O usuário {dados.name} já está inativo')
                         else:
                              dados.account_active = False
                              session.commit()
                              print(f'O status do usuáro {dados.name} foi atualiado para INATIVO')
          except Exception as e:
               print(f'Ocorreu um erro. {e}')
               session.rollback()
     else:
          print('Opção inválida, tente novamente.')