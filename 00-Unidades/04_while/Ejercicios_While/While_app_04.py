import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD
<<<<<<< HEAD:ejercicios/04_intruccion_while/ejercicio_04/While_app_04.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
nombre:
apellido:
---
Ejercicio: while_04
---
<<<<<<< HEAD
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/04_while/Ejercicios_While/While_app_04.py
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        numero = -1

        while numero < 0 or numero > 9:
            numero =int(numero)
            numero = prompt("VALIDAR NUMERO" , "NUMERO")
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()