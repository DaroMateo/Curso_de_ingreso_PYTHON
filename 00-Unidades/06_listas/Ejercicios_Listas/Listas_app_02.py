import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_02
---
Enunciado:
Al presionar el botón 'Calcular' se deberá sumar todos los numeros de la lista, mostrar el resultado de la sumatoria y el promedio por Dialog Alert . 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]
        
    def btn_calcular_on_click(self):
<<<<<<< HEAD
        suma = self.lista_datos[0]
        for contador in (self.lista_datos):
            suma += contador
        alert("", suma)
=======
        pass
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
<<<<<<< HEAD
    app.mainloop()
=======
    app.mainloop()
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
