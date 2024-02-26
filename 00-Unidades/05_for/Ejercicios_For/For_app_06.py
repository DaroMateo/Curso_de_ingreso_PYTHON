import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
<<<<<<< HEAD
=======
<<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_02/app.py
nombre: Dario Ezequiel
apellido: Mateo
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
========
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
nombre:
apellido:
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
<<<<<<< HEAD
=======
>>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/05_for/Ejercicios_For/For_app_06.py
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
<<<<<<< HEAD

        self.title("UTN Fra")
        
=======
<<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_02/app.py
========

        self.title("UTN Fra")
>>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/05_for/Ejercicios_For/For_app_06.py
        
        self.title("UTN FRA")
       
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
<<<<<<< HEAD
        pregunta = question("","¿Desea continuar?")
        for pregunta in iter(int,3):
            pregunta = question("","¿Desea continuar?")
            break
=======
        prompt("igreso de datos" , "ingreso de texto")
        alert("Datos" , "funciona")
        mensaje = "funciona"
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
        
    
if __name__ == "__main__":
    app = App()
<<<<<<< HEAD
    app.geometry("300x300")
    app.mainloop()
=======
    app.mainloop()
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
