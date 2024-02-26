import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos= 0 
        acumulador_positivos= 0 
        cantidad_negativos= 0 
        cantidad_positivos=0 
        ceros = 0
        
        numero = prompt("NUMEROS", "Ingrese un número")
        while True:
            if numero is None or numero == "":
                respuesta = question("Cancelacion", "¿Desea cancelar?")
                if respuesta:
                    break
            else:
                agregado = int(numero)
                if agregado < 0:
                    acumulador_negativos += agregado
                    cantidad_negativos += 1
                elif agregado > 0:
                    acumulador_positivos += agregado
                    cantidad_positivos += 1
                else:
                    ceros += 1
            
            numero = prompt("NUMEROS", "Ingrese un número")

        alert("Suma de positivos", str(acumulador_positivos))
        alert("Cantidad de positivos", str(cantidad_positivos))
        alert("Suma de negativos", str(acumulador_negativos))
        alert("Cantidad de negativos", str(cantidad_negativos))
        alert("Cantidad de ceros", str(ceros))

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
