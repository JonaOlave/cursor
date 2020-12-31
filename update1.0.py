import pyautogui
import time

x = 200
y = 200
cord_x, cord_y = pyautogui.position()

def cursor():
    pyautogui.moveTo(x, y)
    pyautogui.rightClick()

while True:
    #captura posicion del Mouse
    cord_x, cord_y = pyautogui.position()
    time.sleep(5) # Tiempo esperado para capturar y comparar la posision del mouse
    cord_x2, cord_y2 = pyautogui.position()
    
    #Compara la captura de posicion del Mouse
    if cord_x2 == cord_x and cord_y2 == cord_y:
        time.sleep(4)
        print('paso 4 seg ...')
        print(cord_x, cord_y)
        cursor()
        x = x + 1
        y = y + 1

