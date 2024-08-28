import json

# Abrindo o arquivo JSON para leitura
# função pode ser modificada para entregar dados de uma maneira mais isolada, irá facilitar a leitura dos dados
def leitura_do_arquivo():
    with open('zoologico.json', 'r', encoding='utf-8') as file:
        dados = json.load(file)
    return dados

# filtrar todos  animais femea
def filtrar_animais_femea():
    dados = leitura_do_arquivo()
    animais = dados["animais"]
    animais_femeas = []
    for animal in animais:
        if animal["genero"] == "Feminino":
            animais_femeas.append(animal)
    print(json.dumps(animais_femeas, indent=4))

# filtrar todos os animais machos acima de 4 anos de idade
def filtrar_animais_machos_acima_de_4_anos_de_idade():
    dados = leitura_do_arquivo()
    animais = (dados["animais"])
    animais_acima4anos = []
    for animal in animais:
        if animal["genero"] == "Masculino" and animal["idade"] > 4:
            animais_acima4anos.append(animal)
    print(json.dumps(animais_acima4anos, indent=4))
          
# filtrar todos os animais femeas abaixo ou igual a 4 anos de idade
def filtrar_animais_femeas_abaixo_ou_igual_a_4_anos_de_idade():
    dados = leitura_do_arquivo()
    animais = (dados["animais"])
    animais_FeAbaixo4anos = []
    for animal in animais:
        if animal["genero"] == "Feminino" and animal["idade"] <= 4:
            animais_FeAbaixo4anos.append(animal)
    print(json.dumps(animais_FeAbaixo4anos, indent=4))

# função com maior complexidade
def tirar_media_de_idade_dos_animais():
    dados = leitura_do_arquivo()
    animais = (dados["animais"])
    soma_idade = 0
    for animal in animais:
        soma_idade = (soma_idade + animal["idade"])
    media_idade = soma_idade / len(animais)
    print(media_idade)

# função com maior complexidade
# filtrar todos os animais em pacotes de informações por genero
# exemplo: {'macho': [animal1, animal2], 'femea': [animal3, animal4]}

def filtrar_animais_por_genero():
    dados = leitura_do_arquivo()
    animais = (dados["animais"])
    animais_femeas = []
    animais_machos = []
    for animal in animais:
        if animal["genero"] == "Feminino":
            animais_femeas.append(animal)
        else:
            animais_machos.append(animal)
    dic_animais = {"Macho": animais_machos, "Femea": animais_femeas}
    print(json.dumps(dic_animais, indent=4))

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

def filtrar_animais_por_genero_e_idade():
    dados = leitura_do_arquivo()
    animais = (dados["animais"])
    animais_femeas = {
        "acima_de_4_anos": [],
        "abaixo_de_4_anos": []
     }
    animais_machos = {
        "acima_de_4_anos": [],
        "abaixo_de_4_anos": []
     }
    for animal in animais:
        if animal["genero"] == "Feminino":
            if animal["idade"] > 4:
                animais_femeas["acima_de_4_anos"].append(animal)
            elif animal["idade"] < 4:
                animais_femeas["abaixo_de_4_anos"].append(animal)
        if animal["genero"] == "Masculino":
            if animal["idade"] > 4:
                animais_machos["acima_de_4_anos"].append(animal)
            elif animal["idade"] < 4:
                animais_machos["abaixo_de_4_anos"].append(animal)
    dic_animais = {"Macho": animais_machos, "Femea": animais_femeas}
    print(json.dumps(dic_animais, indent=4))

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
def separar_animais_por_idade():
    dados = leitura_do_arquivo()
    animais = (dados["animais"])
    dic_idades = {}
    for animal in animais:
        if not dic_idades.get(animal["idade"]):
            dic_idades[animal["idade"]] = []
        dic_idades[animal["idade"]].append(animal)

    print(json.dumps(dic_idades, indent=4))

# reescrever o genero de todos os animais para 'macho' ou 'femea', atualmente está Feminino e Masculino,
# os dados devem ser reescritos dentro do arquivo zoologico.json
def reescrever_genero_dos_animais():
    pass

if __name__ == "__main__":
    
    separar_animais_por_idade()

    # adicione aqui as funções que vc quer rodar ao digitar python exercicios_01.py no terminal para visualizar os resultados
