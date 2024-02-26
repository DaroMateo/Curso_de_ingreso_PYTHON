import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
<<<<<<< HEAD:ejercicios/05_instruccion_for/ejercicio_06/For_app_06.py
        for i in range(1,12,2):
            alert("PARES", i)
=======
        pass
            
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/05_for/Ejercicios_For/For_app_05.py
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
