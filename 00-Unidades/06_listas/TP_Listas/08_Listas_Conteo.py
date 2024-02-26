import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: Listas_conteo
---
Enunciado:
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

Bonus:
    i. El listado de numeros pares
    j. Que se ingreso mas? positivos, negativos o ceros

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista_numeros = []

    def btn_comenzar_ingreso_on_click(self):
<<<<<<< HEAD
        numero = prompt("", "NUMERO")
        continuar = True

        while continuar:
            if(numero == None):
                continuar = not question("", "DEJAR DE INGRESAR?")
                if not continuar:
                    break
            elif(numero == ""):
                numero = prompt("", "NUMERO VALIDO")
                continue
            else:
                self.lista.append(int(numero))

            numero = prompt("", "NUMERO")

    def btn_mostrar_estadisticas_on_click(self):
        suma_positivo= 0 
        cantidad_positivo = 0 
        maximo_positivo = None
        suma_negativo = 0 
        cantidad_negativo = 0 
        minimo_negativo = None
        ceros = 0

        print(self.lista)

        for i in self.lista:
            if i > 0:
                if maximo_positivo == None:
                    maximo_positivo = i
                elif maximo_positivo < i:
                    maximo_positivo = i
                
                suma_positivo += i
                cantidad_positivo += 1
            elif i < 0:
                if minimo_negativo == None:
                    minimo_negativo = i
                elif minimo_negativo > i:
                    minimo_negativo = i
                
                suma_negativo += i
                cantidad_negativo += 1
            else:
                ceros += 1

        promedio_negativo = 0
        if cantidad_negativo != 0:
            promedio_negativo = suma_negativo//cantidad_negativo

        mensaje = ("Suma de los positivos: " + str(suma_positivo))
        mensaje = ("Suma de los negativos: " + str(suma_negativo))
        mensaje =("Cantidad de positivos: " + str(cantidad_positivo))
        mensaje = ("Cantidad de negativos: " + str(cantidad_negativo))
        mensaje = ("Minimo de negativos: " + str(minimo_negativo))
        mensaje = ("Maximo de positivos: "+ str(maximo_positivo))
        mensaje = ("Cero: " +str(ceros))
        mensaje = ("Promedio de negativos: " + str(promedio_negativo))


        alert("Estadisticas", mensaje)
=======
        pass

    def btn_mostrar_estadisticas_on_click(self):
        pass
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
