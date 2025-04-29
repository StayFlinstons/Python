import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

import functions

# configurando a engine do BD
engine = create_engine("sqlite:///teste001/users.db")

# configurando a sessão
Session = sessionmaker(engine)

# criando tabela
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    date = Column(DateTime, default=func.now())
    account_active = Column(Boolean, default=True)

if __name__ == '__main__':
    os.system('cls')
    Base.metadata.create_all(engine)
    functions.run_app()