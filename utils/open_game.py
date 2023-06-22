import pygetwindow
import subprocess

# Abre el juego si no está abierto
def abrir_juego():
    juego = pygetwindow.getWindowsWithTitle("Project Zomboid")
    if not juego:
        subprocess.Popen("D:\SteamLibrary\steamapps\common\ProjectZomboid\ProjectZomboid64.exe")
        # Agrega un tiempo de espera para que la ventana del juego se abra completamente
        time.sleep(2)

# Enfoca la ventana del juego por su título
def enfocar_ventana_juego():
    juego = pygetwindow.getWindowsWithTitle("Project Zomboid")
    if juego:
        juego[0].activate()

# Llamada a las funciones
abrir_juego()
enfocar_ventana_juego()
