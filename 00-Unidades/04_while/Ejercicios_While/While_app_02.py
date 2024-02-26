import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD:ejercicios/04_intruccion_while/ejercicio_02/While_app_02.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
nombre:
apellido:
---
Ejercicio: while_02
---
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/04_while/Ejercicios_While/While_app_02.py
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números DESCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        numero = 10
        while numero >=1 :
            alert("NUMERO" , numero)
            numero -= 1

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()