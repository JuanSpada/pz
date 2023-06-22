from pynput.keyboard import Controller
import pyautogui
import time
from utils.open_game import abrir_juego

abrir_juego()

def do_job():
    # Crea el objeto de control de teclado
    keyboard = Controller()
    # Obtener las dimensiones de la pantalla
    ancho_pantalla, alto_pantalla = pyautogui.size()
    # Calcular el centro
    centro_x = ancho_pantalla // 2
    centro_y = alto_pantalla // 2
    pyautogui.moveTo(centro_x, centro_y)
    pyautogui.mouseDown(button='right')

    # GO NORTH
    keyboard.press('w')
    keyboard.press('d')
    time.sleep(11)
    keyboard.release('w')
    keyboard.release('d')

    # GO SOUTH
    keyboard.press('a')
    keyboard.press('s')
    time.sleep(11)
    keyboard.release('a')
    keyboard.release('s')

    # STOP
    pyautogui.mouseUp(button='right')

def re_do_job(times):
    for _ in range(times):
        do_job()

# Llamada a la función
re_do_job(100)
