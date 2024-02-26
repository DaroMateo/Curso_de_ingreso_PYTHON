import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD:ejercicios/04_intruccion_while/ejercicio_03/While_app_03.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
nombre:
apellido:
---
Ejercicio: while_03
---
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/04_while/Ejercicios_While/While_app_03.py
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):
        contraseña = ""
        while contraseña != "utn750":
            contraseña = prompt("UTN FRA" , "ingreso")

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()