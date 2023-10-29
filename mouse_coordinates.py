from pynput import keyboard
import pyautogui

def capturar_coordenadas():
    def on_key_release(key):
        if key == keyboard.Key.esc:
            # Encerra o programa quando a tecla Esc é pressionada
            print("\nCaptura de coordenadas encerrada.")
            return False

    # Configura o listener do teclado
    with keyboard.Listener(on_release=on_key_release) as listener:
        while True:
            x, y = pyautogui.position()
            print(f"Posição atual do mouse: X={x}, Y={y}", end="\r")

capturar_coordenadas()
