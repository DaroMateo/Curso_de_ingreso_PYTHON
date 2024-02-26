import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre = None 
        edad = None 
        votos= 0 
        cantidad = 0 
        total_votos= 0 
        total_edad= 0 
        continuar = True
        minimo_votos = 0
        maximo_votos = 0
        nombre_candidato_votado = "" 
        nombre_candidato_no_votado = "" 
        edad_candidato_no_votado = 0

        while continuar:
            nombre = prompt("", "NOMBRE DE CANDIDATO")
            while nombre is None or nombre == "" or nombre.isdigit():
                if nombre is None:
                    if question("", "DESEA CONTINUAR?"):
                        quit()

                nombre = prompt("", "NOMBRE CORRECTO")

            edad = prompt("", "EDAD")
            while edad is None or edad == "" or not edad.isdigit() or int(edad) <= 25:
                if edad is None:
                    if question("", "DESEA CONTINUAR?"):
                        quit()

                edad = prompt("", "EDAD")

            votos = prompt("", "CANTIDAD")
            while votos is None or votos == "" or not votos.isdigit() or int(votos) < 0:
                if votos is None:
                    if question("", "DESEA CONTINUAR?"):
                        quit()

                votos = prompt("", "CANTIDAD DE VOTOS CORRECTOS")

            total_votos += int(votos)
            total_edad += int(edad)
            cantidad += 1

            if(nombre_candidato_votado) == "":
                nombre_candidato_votado = nombre
                nombre_candidato_no_votado = nombre
                edad_candidato_no_votado = edad
                maximo_votos = votos
                minimo_votos = votos
            else:
                if(int(maximo_votos) < int(votos)):
                    nombre_candidato_votado = nombre
                    maximo_votos = votos
                elif(int(minimo_votos) > int(votos)):
                    nombre_candidato_no_votado = nombre
                    minimo_votos = votos
                    edad_candidato_no_votado = edad

            continuar = question("", "DESEA AGREGAR CANDIDATOS")

        promedio_edad = total_edad/cantidad

        mensaje = "Resultados de la votación:\n\nCandidato con más votos: " + nombre_candidato_votado + "\n"\
                  "Candidato y edad de candidato con menos votos: " + nombre_candidato_no_votado + " " + edad_candidato_no_votado + "\n"\
                  "Promedio de edades de los candidatos: " + str(promedio_edad) + "\n"\
                  "Total de votos emitidos: " + str(total_votos)

        print("Esto es una alerta", mensaje)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
