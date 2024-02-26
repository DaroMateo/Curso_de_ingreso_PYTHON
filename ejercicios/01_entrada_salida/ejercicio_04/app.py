import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Dario Ezequiel
apellido: Mateo
---
Ejercicio: entrada_salida_04
---
Enunciado:
<<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_04/app.py
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
========
Al presionar el botón  'Mostrar', se deberá obtener el contenido de la caja de texto para luego 
mostrarlo utilizando el Dialog Alert
>>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/01_entrada_salida/Ejercicios_entrada_salida/ES_app_03.py
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nombre = prompt("datos", "nombre")
        self.txt_nombre.delete(0,100)
        self.txt_nombre.insert(0,nombre)



if __name__ == "__main__":
    app = App()
    app.mainloop()