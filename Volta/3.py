frase = input("Digite uma frase: ").lower()
vogais = ["a", "e", "i", "o", "u"]
indice = 0

for letras in frase:
    if letras in vogais:
        indice += 1
print(f"Na frase digitada tem {indice}")