import os

# Diretório base do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Configuração do banco de dados
DATABASE = os.path.join(BASE_DIR, 'database.db')

# Chave secreta para a sessão
SECRET_KEY = 'chave-secreta-super-segura'

# Ativando o modo de depuração (apenas para desenvolvimento)
DEBUG = True
