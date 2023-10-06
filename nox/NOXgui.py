import speech_recognition as sr  # Importa la biblioteca SpeechRecognition para el reconocimiento de voz.
import subprocess as sub  # Importa la biblioteca subprocess para ejecutar comandos del sistema operativo.
import pyttsx3  # Importa la biblioteca pyttsx3 para la síntesis de voz.
import os  # Importa la biblioteca os para interactuar con el sistema operativo.
from tkinter import *  # Importa la biblioteca tkinter para crear la interfaz gráfica de usuario.
from PIL import ImageTk, Image  # Importa la biblioteca PIL para trabajar con imágenes.

# python .\NOXgui.py

#telegram C:\Users\ryzen 5\AppData\Roaming\Telegram Desktop\Telegram.exe
#música C:\Users\ryzen 5\AppData\Roaming\Spotify\Spotify.exe

#---------------------------------------------------Ventana Base--------------------------------------------------
main_window = Tk() #Ventana raíz
main_window.title("NOX Assistant")

main_window.geometry("800x450")#Ancho x alto
main_window.resizable(0,0)#Se elimina el resize
main_window.configure(bg="#0F2027")#fondo

comandos = """
        Comandos disponibles:
        - Reproduce ... (canción)
        - Busca ... (algo)
        - Abre ... (pag o app)
        - Alarma ... (Hora en 24hrs)
        - Archivo ... (nombre)
        - Escribe ... (info a anotar)
        - Termina para que deje de
          escuchar
"""


label_title = Label(main_window, text="NOX", bg="#000000", fg="#833ab4", font=("Arial", 20,'bold'))
label_title.pack(pady=10)#vuelve a la label un bloque y lo pone en el centro con padding de 10 px

canvas_comandos = Canvas(bg="#2c3e50", height=170, width=195)
canvas_comandos.place(x=0,y=0)
canvas_comandos.create_text(90,80, text = comandos, fill="white", font='Arial 10')


nox_photo = ImageTk.PhotoImage(Image.open(r"C:\Users\ryzen 5\Desktop\UNI\7mo semestre\SisInfo\R.jpg"))
window_photo = Label(main_window, image=nox_photo)
window_photo.pack(pady=5)
#-------------------------------------Configuraciones iniciales-----------------------------------------
def mexico_voice():
    change_voice(2)
def usa_voice():
    change_voice(0)

def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    if id == 2:
        talk("Hola; Soy Nox")
    else:
        talk("Hello; Im Nox")

def charge_data(name_dict, name_file):
    # La función charge_data toma un diccionario (name_dict) y un nombre de archivo (name_file) como entrada.
    try:
        # Intenta abrir el archivo especificado en modo lectura.
        with open(name_file) as f:
            # Itera a través de cada línea en el archivo.
            for line in f:
                # Elimina los espacios en blanco al principio y al final de la línea, y luego divide la línea en partes usando ',' como separador.
                parts = line.strip().split(",")
                # Comprueba si la línea contiene exactamente dos partes (clave y valor).
                if len(parts) == 2:
                    # Asigna las partes a las variables 'key' y 'val'.
                    key, val = parts
                    # Agrega la clave y el valor al diccionario name_dict.
                    name_dict[key] = val
    # Captura la excepción que ocurre cuando el archivo no se encuentra.
    except FileNotFoundError:
        # Si el archivo no se encuentra, no hace nada y continúa con la ejecución del programa.
        pass



name = "Nox"
engine = pyttsx3.init()
# for i in voices:
#     print(i)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 145)


#-------------------------------------------Archivos Permanencia---------------------------------------------
sites = {}
charge_data(sites,"paginas.txt")
programs = {}
charge_data(programs,"aplicaciones.txt")

#------------------------------------------Habla y Escucha-------------------------------------------
def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen(phrase=None):
    # Inicia el reconocedor de voz
    listener = sr.Recognizer()
    # Abre el micrófono como fuente de audio
    with sr.Microphone() as source:
        # Ajusta el nivel de ruido ambiental para mejorar la calidad del reconocimiento
        listener.adjust_for_ambient_noise(source)
        # Lee la frase de entrada y la reproduce usando la función de síntesis de voz "talk"
        talk(phrase)
        # Captura el audio del micrófono y lo almacena en la variable 'pc'
        pc = listener.listen(source)
    try:
        # Utiliza el reconocedor de voz de Google para convertir el audio en texto
        rec = listener.recognize_google(pc, language="es")
        # Convierte el texto a minúsculas para facilitar el manejo
        rec = rec.lower()
    except sr.UnknownValueError:
        # Maneja el error cuando el reconocedor no puede entender la entrada de voz
        print("No entendí, intenta de nuevo")
        print(rec)  # Esta línea no debería imprimirse, debería ser eliminada o modificada
    except sr.RequestError as e:
        # Maneja el error cuando no se puede conectar al servicio de reconocimiento de voz de Google
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    # Devuelve el texto reconocido en minúsculas
    return rec


# ---------------------------Funciones----------------------------------



def abre(rec):
    # La función abre toma una cadena de texto `rec` como entrada, que contiene la instrucción para abrir un sitio web o una aplicación.
    # Elimina la palabra 'abre' del texto de entrada y elimina los espacios en blanco al principio y al final de la cadena resultante.
    task = rec.replace("abre", "").strip()
    # Comprueba si la tarea está en el diccionario de sitios web (sites).
    if task in sites:
        # Itera a través de las claves en el diccionario de sitios web.
        for task in sites:
            # Comprueba si la clave está presente en la cadena de entrada original (`rec`).
            if task in rec:
                # Utiliza el módulo subprocess para abrir el sitio web en el navegador (en este caso, Microsoft Edge).
                # Utiliza 'shell=True' para que la línea de comando sea ejecutada en un intérprete de comandos del sistema operativo.
                sub.call(f'start msedge.exe {sites[task]}', shell=True)
                # Imprime un mensaje en la consola indicando que el sitio web está siendo abierto.
                print(f"Abriendo {task}")
                # Utiliza la función talk para sintetizar un mensaje hablado informando que el sitio web está siendo abierto.
                talk(f'Abriendo {task}')

    # Si la tarea no está en el diccionario de sitios web, comprueba si está en el diccionario de aplicaciones (programs).
    elif task in programs:
        # Itera a través de las claves en el diccionario de aplicaciones.
        for task in programs:
            # Comprueba si la clave está presente en la cadena de entrada original (`rec`).
            if task in rec:
                # Utiliza la función os.startfile para abrir la aplicación asociada con la clave en el diccionario de aplicaciones.
                os.startfile(programs[task])
                # Utiliza la función talk para sintetizar un mensaje hablado indicando que la aplicación está siendo abierta.
                talk(f"Abriendo {task}")
    
    # Si la tarea no está en ninguno de los diccionarios (sites o programs), informa al usuario que debe agregar programas usando los botones correspondientes.
    else:
        talk("Aún no has agregado elementos, usa los botones correspondientes")


# -------------------------------------------------Palabras Clave---------------------------------------------------
key_words = {
    'abre': abre
}

#------------------------------------------Main------------------------------------
def run_nox():
    talk("Te escucho...")
    while True:
        try:
            rec = listen("")
        except UnboundLocalError:
            talk("No te entendí, intenta de nuevo")
            continue
        if rec.split()[0] in key_words:
            # obtiene la palabra clave y llama a la función correspondiente con la instrucción como argumento.
            key = rec.split()[0]        
            key_words[key](rec)
            print(rec)
        elif 'fuera' in rec or 'salir' in rec or 'termina' in rec:
            break
    main_window.update() #Refresca el programa para eficiencia


#-----------------------------------------------------INTERFAZ---------------------------------------------------------


def open_w_apps():
    global app_entry, patha_entry
    window_app = Toplevel()
    window_app.title("Agregar Aplicaciones")
    window_app.configure(bg="#0F2027")
    window_app.geometry("300x200")
    window_app.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_app)} center')

    title_label = Label(window_app, text="Agrega una aplicación",fg="white",bg="#0F2027", font=('Arial', 15,'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_app, text="Nombre de la aplicación",fg="white",bg="#0F2027", font=('Arial', 10,'bold'))
    name_label.pack(pady=2)

    app_entry = Entry(window_app)
    app_entry.pack(pady=1)

    path_label = Label(window_app, text="Dirección de la aplicación",fg="white",bg="#0F2027", font=('Arial', 10,'bold'))
    path_label.pack(pady=2)
    patha_entry = Entry(window_app,width=35)
    patha_entry.pack(pady=1)

    save_button = Button(window_app, text="Guardar", bg="#203A43", fg="White",width=8,height=1,command=add_apps)
    save_button.pack(pady=4)
def open_w_pages():
    global page_entry, pathp_entry
    window_page = Toplevel()
    window_page.title("Agregar Páginas")
    window_page.configure(bg="#0F2027")
    window_page.geometry("300x200")
    window_page.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_page)} center')

    title_label = Label(window_page, text="Agrega una página",fg="white",bg="#0F2027", font=('Arial', 15,'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_page, text="Nombre de la pag",fg="white",bg="#0F2027", font=('Arial', 10,'bold'))
    name_label.pack(pady=2)

    page_entry = Entry(window_page)
    page_entry.pack(pady=1)

    path_label = Label(window_page, text="URL de la página",fg="white",bg="#0F2027", font=('Arial', 10,'bold'))
    path_label.pack(pady=2)
    pathp_entry = Entry(window_page,width=35)
    pathp_entry.pack(pady=1)

    save_button = Button(window_page, text="Guardar", bg="#203A43", fg="White",width=8,height=1, command=add_pages)
    save_button.pack(pady=4)


#--------------------------------------------FUNCIONES GUI-----------------------------------------------------------


def add_apps():
    name_app = app_entry.get().strip()
    path_app = patha_entry.get().strip()
    programs[name_app] = path_app
    save_data(name_app,path_app,"aplicaciones.txt")
    app_entry.delete(0,"end")
    patha_entry.delete(0,"end")
def add_pages():
    # La función add_pages se utiliza para agregar una nueva página web al diccionario 'sites'.
    # Obtiene el nombre de la página ingresado por el usuario y elimina los espacios en blanco al principio y al final.
    name_page = page_entry.get().strip()
    # Obtiene la URL de la página ingresada por el usuario y elimina los espacios en blanco al principio y al final.
    path_page = pathp_entry.get().strip()
    # Agrega la nueva página web al diccionario 'sites', donde el nombre de la página es la clave y la URL es el valor.
    sites[name_page] = path_page
    # Llama a la función save_data para guardar los datos del diccionario 'sites' en un archivo llamado "paginas.txt".
    save_data(name_page, path_page, "paginas.txt")
    # Borra el contenido de los campos de entrada (Entry widgets) para futuras entradas.
    page_entry.delete(0, "end")
    pathp_entry.delete(0, "end")


def save_data(key, value, file_name):
    # La función save_data se utiliza para guardar una clave y un valor en un archivo de texto.
    try:
        # Intenta abrir el archivo en modo de anexar ('a').
        with open(file_name, 'a') as f:
            # Escribe la clave y el valor separados por una coma en una nueva línea del archivo.
            f.write(key + "," + value + "\n")
    # Captura la excepción que ocurre cuando el archivo no se encuentra.
    except FileNotFoundError:
        # Si el archivo no se encuentra, crea un nuevo archivo y escribe la clave y el valor en una nueva línea.
        file = open(file_name, 'a')
        file.write(key + "," + value + "\n")

def talk_pages():
    if bool(sites) == True:
        talk("Has agregado las siguientes páginas web:")
        for site in sites:
            talk(site)
    else:
        talk("Aún no has agregado páginas web")
def talk_apps(): 
    if bool(programs) == True:
        talk("Has agregado las siguientes aplicaciones:")
        for program in programs:
            talk(program)
    else:
        talk("Aún no has agregado aplicaciones")



#------------------------------------------------BOTONES-------------------------------------------------------
button_voice_mx = Button(main_window, text="Voz México", fg="white", bg="#38ef7d", 
                         font=("Arial",10,"bold"), command=mexico_voice)
button_voice_mx.place(x=625,y=90, width=100, height=30)

button_voice_us = Button(main_window, text="Voz USA", fg="white", bg="#11998e", 
                         font=("Arial",10,"bold"), command=usa_voice)
button_voice_us.place(x=625,y=50, width=100, height=30)

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#8E0E00", 
                         font=("Arial",15,"bold"),width=20,height= 2,command=run_nox)
button_listen.pack(side=BOTTOM, pady=10)



button_add_apps = Button(main_window, text="Add apps", fg="white", bg="#23074d", 
                         font=("Arial",10,"bold"), command=open_w_apps)
button_add_apps.place(x=625,y=230, width=100, height=30)
button_add_pages = Button(main_window, text="Add pages", fg="white", bg="#23074d", 
                         font=("Arial",10,"bold"), command=open_w_pages)
button_add_pages.place(x=625,y=270, width=100, height=30)



button_actual_pages = Button(main_window, text="Páginas actuales", fg="white", bg="#7303c0", 
                         font=("Arial",10,"bold"), command=talk_pages)
button_actual_pages.place(x=205,y=280 , width=125, height=30)

button_actual_apps = Button(main_window, text="Apps actuales", fg="white", bg="#7303c0", 
                         font=("Arial",10,"bold"), command=talk_apps)
button_actual_apps.place(x=335,y=280 , width=125, height=30)

main_window.mainloop()