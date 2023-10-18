import tkinter as tk
import time
import threading
from pynput.mouse import Controller, Button
from pynput import keyboard

class AutoClicker:
    def __init__(self, interval, button, clicks):
        self.interval = interval / 1000  # Converter para segundos
        self.button = button
        self.clicks = clicks
        self.running = False
        self.mouse = Controller()

    def click(self):
        for _ in range(self.clicks):
            if not self.running:
                break
            self.mouse.click(self.button)
            time.sleep(self.interval)

    def start_clicking(self):
        self.running = True
        self.click_thread = threading.Thread(target=self.click)
        self.click_thread.start()

    def stop_clicking(self):
        self.running = False
        if hasattr(self, 'click_thread'):
            self.click_thread.join()

def iniciar_auto_clicker():
    intervalo = int(entry_intervalo.get())
    button = Button.left if var_botao.get() == 0 else Button.right
    clicks = int(entry_clicks.get())

    global auto_clicker
    auto_clicker = AutoClicker(intervalo, button, clicks)
    auto_clicker.start_clicking()

def parar_auto_clicker():
    auto_clicker.stop_clicking()

def tecla_emergencial():
    if auto_clicker:
        parar_auto_clicker()

def on_press(key):
    if key == keyboard.Key.f1:
        if auto_clicker and var_botao.get() == 0:
            iniciar_auto_clicker()
        elif auto_clicker and var_botao.get() == 1:
            parar_auto_clicker()
    elif key == keyboard.Key.f9:
        tecla_emergencial()

listener = keyboard.Listener(on_press=on_press)
listener.start()

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("350x400")  

label_botao = tk.Label(root, text="Escolha o botão:")
label_botao.pack()
var_botao = tk.IntVar()
var_botao.set(0)
radio_esquerdo = tk.Radiobutton(root, text="Esquerdo", variable=var_botao, value=0)
radio_esquerdo.pack()
radio_direito = tk.Radiobutton(root, text="Direito", variable=var_botao, value=1)
radio_direito.pack()

label_intervalo = tk.Label(root, text="Intervalo (ms):")
label_intervalo.pack()
entry_intervalo = tk.Entry(root)
entry_intervalo.pack()

label_clicks = tk.Label(root, text="Número de cliques:")
label_clicks.pack()
entry_clicks = tk.Entry(root)
entry_clicks.pack()

botao_parar = tk.Button(root, text="Parar", command=parar_auto_clicker)
botao_parar.pack()

root.mainloop()