import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Dario Ezequiel
apellido: mateo
---
Ejercicio: entrada_salida_03
---
Enunciado:
<<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_03/app.py
Al presionar el botón  'Mostrar', se deberá obtener contenido en la caja de texto y luego mostrarlo utilizando el Dialog Alert
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
       participante = self.txt_nombre.get()
       alert("alumno", participante)


        
                
    
if __name__ == "__main__":
    app = App()
    app.mainloop()