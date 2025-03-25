import random

randomNum = random.randint(1, 100)
tentativas = 0

while True:
    numeroUsuario = int(input("Digite um número: "))
    tentativas += 1 
    if numeroUsuario == randomNum:
        print(f"Você acertou em {tentativas} tentativas.")
        break
    elif numeroUsuario < randomNum:
        print("Digite um numero maior")

    elif numeroUsuario > randomNum:
        print("Digite um numero menor")