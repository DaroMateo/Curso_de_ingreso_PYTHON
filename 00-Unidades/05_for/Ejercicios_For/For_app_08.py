import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
<<<<<<< HEAD
        numero = int(prompt("", "NUMERO"))
        es_primo = True

        for i in range(2, numero // 2 + 1, 1):
            if(numero%i == 0):
                es_primo = False

        mensaje = "El número ingresado "
        if es_primo:
            mensaje += "es primo"
        if not es_primo:
            mensaje += "no es primo"
            
        alert("Esto es una alert", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
=======
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
