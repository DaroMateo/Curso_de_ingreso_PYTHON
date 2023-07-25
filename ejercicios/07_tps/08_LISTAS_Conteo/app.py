import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
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

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
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
        suma_positivos= 0 
        cantidad_positivos = 0 
        maximo_positivos = None
        suma_negativos = 0 
        cantidad_negativos = 0 
        minimo_negativos = None
        ceros = 0

        print(self.lista)

        for i in self.lista:
            if i > 0:
                if maximo_positivos == None:
                    maximo_positivos = i
                elif maximo_positivos < i:
                    maximo_positivos = i
                
                suma_positivos += i
                cantidad_positivos += 1
            elif i < 0:
                if minimo_negativos == None:
                    minimo_negativos = i
                elif minimo_negativos > i:
                    minimo_negativos = i
                
                suma_negativos += i
                cantidad_negativos += 1
            else:
                ceros += 1

        promedio_negativos = 0
        if cantidad_negativos != 0:
            promedio_negativos = suma_negativos//cantidad_negativos

        mensaje = ("Suma de los positivos: " + str(suma_positivos))
        mensaje = ("Suma de los negativos: " + str(suma_negativos))
        mensaje =("Cantidad de positivos: " + str(cantidad_positivos))
        mensaje = ("Cantidad de negativos: " + str(cantidad_negativos))
        mensaje = ("Minimo de negativos: " + str(minimo_negativos))
        mensaje = ("Maximo de positivos: "+ str(maximo_positivos))
        mensaje = ("Cero: " +str(ceros))
        mensaje = ("Promedio de negativos: " + str(promedio_negativos))

        alert("Esto es una alerta", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
