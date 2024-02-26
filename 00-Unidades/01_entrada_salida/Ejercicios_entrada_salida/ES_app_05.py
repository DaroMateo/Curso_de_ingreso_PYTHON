import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_05
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener tanto el nombre como la edad contenida en 
las cajas de texto correspondientes y luego mostrar los datos concatenados utilizando el Dialog Alert. 
Ej: "Usted se llama José y su edad es 66 años"
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
<<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_05/app.py
        nombre=self.txt_nombre.get()
        edad= self.txt_edad.get()
        mensaje_en_alert= "Hola " + nombre + " usted tiene " + edad + " años"
        alert("Bienvenido" , mensaje_en_alert)
========
        pass

        
>>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/01_entrada_salida/Ejercicios_entrada_salida/ES_app_05.py
    
     
if __name__ == "__main__":
    app = App()
    app.mainloop()