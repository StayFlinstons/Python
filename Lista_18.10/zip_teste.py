frutas = ['maçã', 'banana', 'laranja', 'uva']
quantidades = [10, 5, 8, 15]

#combinar as listas
for fruta, quantidade in zip(frutas, quantidades):
    print(f"{fruta}: {quantidade} unidades")
