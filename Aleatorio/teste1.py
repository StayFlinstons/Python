def main():
    while True:
        # Coloque todo o código principal do seu programa aqui
        # ...

        reiniciar = input("Deseja reiniciar o programa? (s/n): ")
        if reiniciar.lower() != 's':
            break  # Sai do loop se a resposta não for 's'

if __name__ == "__main__":
    main()
