import pyautogui, time, keyboard, threading

#Coordenadas donde se realizan los clicks
x, y = 641, 663  #Coords responder historia
x2, y2 = 663, 612  #Coords emoji fuego
x3, y3 = 129, 45  #Coords de F5
x4, y4 = 703, 495  #Coords ver historia

#Variable para detener el bucle
stop_script = False

#Funcion para verificar si se presiona la tecla 'z'
def check_stop():
    global stop_script
    keyboard.wait('z')  #Espera a que el usuario presione la tecla 'z'
    stop_script = True #Cambia stop_script a True para detener el script

# Crear y iniciar la verificación de la tecla de detencion (z)
stop_thread = threading.Thread(target=check_stop)
stop_thread.start()

print("Inicia el script con la letra 'x', detenlo con 'z'\n")

keyboard.wait('x')  # Espera a que el usuario presione la tecla 'x' para que se siga ejecutando

while not stop_script: #Se ejecuta hasta que stop_script sea True
    for i in range(1, 10): #Repite el proceso 10 veces
        if stop_script: #Verifica si se quizo detener el script
            break
        pyautogui.click(x, y)  #Clickea en el botón para responder la historia
        pyautogui.click(x2, y2)  #Clickea en el emoji de fuego (🔥)

    if stop_script:#Verifica nuevamente despues del for
        break

    time.sleep(1)  #Espera 1 segundo
    pyautogui.click(x3, y3)  #Recarga la página ya que si no ocurren bugs
    time.sleep(2.5)  #Espera 2.5 segundos mientras se recarga la página
    pyautogui.click(x4, y4)  #Clickea en el botón de ver historia
    time.sleep(0.5)  #Espera 0.5s mientras carga correctamente la historia

print("El script ha sido detenido.")
