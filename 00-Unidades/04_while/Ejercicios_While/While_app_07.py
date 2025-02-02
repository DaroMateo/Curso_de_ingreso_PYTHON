import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
<<<<<<< HEAD
<<<<<<< HEAD:ejercicios/04_intruccion_while/ejercicio_07/While_app_07.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
nombre:
apellido:
---
Ejercicio: while_07
---
<<<<<<< HEAD
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/04_while/Ejercicios_While/While_app_07.py
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
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
        acumulador = 0
        contador = 0
        cancelar = False

        numero = prompt("SUMA", "NUMERO no vacio")
        while not cancelar:
            if numero is None or numero == "":
                cancelar = question("Confirmación", "¿Desea cancelar?")
                if cancelar:
                    continue
            else:
                acumulador += int(numero)
                contador += 1

            numero = prompt("SUMA", "NUMERO no vacio")

        promedio = acumulador/contador
        self.txt_suma_acumulada.delete(0, 100)
        self.txt_suma_acumulada.insert(0, str(acumulador))
        self.txt_promedio.delete(0, 100)
        self.txt_promedio.insert(0, str(promedio))
    

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
