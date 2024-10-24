import pyautogui as pg
import time as tm
import webbrowser as web

web.open("https://web.whatsapp.com/send/?phone=+52NUMERO")

tm.sleep(30)

archivo = open("mensaje.txt", "r")
with open("mensaje.txt") as archivo:
    for linea in archivo:
        #print(type(linea))
        pg.typewrite(linea.replace('1', '\t'))
        print(linea.replace('1', '\t'))
        #pg.typewrite(linea)
        #print(linea)
        tm.sleep(3)
        pg.press("Enter")