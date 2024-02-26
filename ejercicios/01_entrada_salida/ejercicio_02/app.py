import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
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
nombre:
apellido:
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
>>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/05_for/Ejercicios_For/For_app_06.py
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
<<<<<<<< HEAD:ejercicios/01_entrada_salida/ejercicio_02/app.py
========

        self.title("UTN Fra")
>>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/05_for/Ejercicios_For/For_app_06.py
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        prompt("igreso de datos" , "ingreso de texto")
        alert("Datos" , "funciona")
        mensaje = "funciona"
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()