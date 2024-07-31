import pyautogui
import time

print("Mueve el cursor a la posición deseada en los próximos 5 segundos...")

#Espera 5 segundos para que puedas mover el cursor a la posicion deseada
time.sleep(5)

#Guarda la posicion del cursor
x, y = pyautogui.position()

print(f"La posición actual del cursor es: ({x}, {y})")

#(641, 663)coords boton responder historia
#(663, 612)coords emoji fuego
#(129, 45)coords reiniciar pagina
#(797, 134) coords pausar historia
#(703, 495) coords ver historia