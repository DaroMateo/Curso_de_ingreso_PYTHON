import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
<<<<<<< HEAD
<<<<<<< HEAD:ejercicios/04_intruccion_while/ejercicio_06/While_app_06.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
nombre:
apellido:
---
Ejercicio: while_06
---
<<<<<<< HEAD
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/04_while/Ejercicios_While/While_app_06.py
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        acumulador = 0
        numero = int(prompt("SUMA" , "Numero"))


        while contador < 5:
            
            numero = int(prompt("SUMA" , "Numero"))
            acumulador += numero
            contador += 1
            
        promedio = acumulador / contador

        numero= str(numero)
        promedio = str(promedio)

        self.txt_suma_acumulada.delete(0 , 100)
        self.txt_suma_acumulada.insert(0, str(numero))
        self.txt_promedio.delete (0 , 100)
        self.txt_promedio.insert(0 , str(promedio))


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
