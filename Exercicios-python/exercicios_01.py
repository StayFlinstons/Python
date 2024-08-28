import json

# Abrindo o arquivo JSON para leitura
# função pode ser modificada para entregar dados de uma maneira mais isolada, irá facilitar a leitura dos dados
def leitura_do_arquivo():
    with open('zoologico.json', 'r') as file:
        dados = json.load(file)
        print(dados)
    return dados 

# filtrar todos  animais femea

def filtrar_animais_femea():
    pass

# filtrar todos os animais machos acima de 4 anos de idade
def filtrar_animais_machos_acima_de_4_anos_de_idade():
    pass

# filtrar todos os animais femeas abaixo ou igual a 4 anos de idade
def filtrar_animais_femeas_abaixo_ou_igual_a_4_anos_de_idade():
    pass

# função com maior complexidade
def tirar_media_de_idade_dos_animais():
    pass

# função com maior complexidade
# filtrar todos os animais em pacotes de informações por genero
# exemplo: {'macho': [animal1, animal2], 'femea': [animal3, animal4]}

def filtrar_animais_por_genero():
    pass

# função com maior complexidade
# filtrar todos os animais em pacotes de informações por genero e idade
""""
exemplo:
{
    'macho': {
        'acima_de_4_anos': [animal1, animal2],
        'abaixo_de_4_anos': [animal3, animal4]
    },
    'femea': {
        'acima_de_4_anos': [animal5, animal6],
        'abaixo_de_4_anos': [animal7, animal8]
    }
}
"""

def filtrar_animais_por_genero_e_idade(animais):
    pass


# função com maior complexidade
# separar todos animais usando as idades como chave de valor e agrupando eles em pacotes de idade:

"""
exemplo:
{
    '1': [animal1, animal2],
    '2': [animal3, animal4],
    '3': [animal5, animal6],
    '4': [animal7, animal8],
    '5': [animal9, animal10],
    '6': [animal11, animal12],
    '7': [animal13, animal14],
    '8': [animal15, animal16],
    '9': [animal17, animal18],
    '10': [animal19, animal20],
}
caso exista mais idades, continuar a sequencia, a função deve usar as proprias idades para agrupar os animais,
n podendo criar manual as chaves com as idades.
"""
def separar_animais_por_idade(animais):
    pass

# reescrever o genero de todos os animais para 'macho' ou 'femea', atualmente está Feminino e Masculino,
# os dados devem ser reescritos dentro do arquivo zoologico.json
def reescrever_genero_dos_animais(animais):
    pass

if __name__ == "__main__":
    pass
    # leitura_do_arquivo() // exemplo de execução da função de leitura do arquivo

    # adicione aqui as funções que vc quer rodar ao digitar python exercicios_01.py no terminal para visualizar os resultados