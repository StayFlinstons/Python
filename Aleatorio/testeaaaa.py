import pyautogui
import time
import keyboard 

def main():
    teste = input('Digite o texto: ')
    num_repeticoes = int(input('Digite o número de repetições: '))
    tecla = input('Digite uma tecla para rodar o programa: ')
    print("Pressione uma tecla para começar a execução.")
    keyboard.wait(tecla) 

    for _ in range(num_repeticoes):
        pyautogui.typewrite(teste)
        pyautogui.press('enter')
        time.sleep(0)
        
    main()

if __name__ == "__main__":
    main()    