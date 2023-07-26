'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre = "" 
        edad = 0  
        genero = "" 
        tecnologia = ""  
        senior = ""

        nbs = 0 
        nombre_jr_menor = "" 
        edad_jr_menor = 0
        cantidad_nbs = 0 
        edades_nbs = 0 
        cantidad_fs = 0 
        edades_fs = 0 
        cantidad_ms = 0 
        edades_ms = 0 
        postulantes = 0
        cantidad_python = 0 
        cantidad_js = 0 
        cantidad_asp = 0

        promedio_nbs = 0
        porcentaje_nbs = 0
        promedio_fs = 0
        porcentaje_fs = 0
        promedio_ms = 0
        porcentaje_ms = 0

        for i in range(0, 10, 1):
            nombre = prompt("", "NOMBRE")
            edad = prompt("", "EDAD")
            genero = prompt("", "GENERO")
            tecnologia = prompt("", "TECNOLOGIA")
            senior = prompt("", "PUESTO")

            postulantes += 1

            if genero == "NB":
                cantidad_nbs += 1
                edades_nbs += edad
            elif genero == "Femenino":
                cantidad_fs += 1
                edades_fs += edad
            elif genero == "Masculino":
                cantidad_ms += 1
                edades_ms += edad

            if tecnologia == "PYTHON":
                cantidad_python += 1
            elif tecnologia == "JS":
                cantidad_js += 1
            elif tecnologia == "ASP.NET":
                cantidad_asp += 1

            
            if genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and edad > 24 and edad < 41 and senior == "Ssr":
                nbs += 1

            if senior == "Jr":
                if nombre_jr_menor == "":
                    nombre_jr_menor = nombre
                    edad_jr_menor = edad
                elif edad_jr_menor > edad:
                    nombre_jr_menor = nombre
                    edad_jr_menor = edad

        
        if cantidad_nbs or cantidad_fs or cantidad_ms != 0:
            promedio_nbs = edades_nbs/cantidad_nbs
            porcentaje_nbs = cantidad_nbs/postulantes*100
            promedio_fs = edades_fs/cantidad_fs
            porcentaje_fs = cantidad_fs/postulantes*100
            promedio_ms = edades_ms/cantidad_ms
            porcentaje_ms = cantidad_ms/postulantes*100

        tecnologia_mas_postulada = "PYTHON"
        if cantidad_js > cantidad_python:
            if cantidad_js > cantidad_asp:
                tecnologia_mas_postulada = "ASP.NET"
            else:
                tecnologia_mas_postulada = "JS"

        print("Cantidad de postulantes de genero NB que programan en ASP.NET o JS " + str(nbs))
        print("Nombre del postulante Jr con menor edad: " + nombre_jr_menor)
        print("Promedio de edades por género NBS: " + str(promedio_nbs))
        print("Promedio de edades por género FS: " + str(promedio_fs))
        print("Promedio de edades por género MS: "  + str(promedio_ms))
        print("Tecnología con más postulantes: " + tecnologia_mas_postulada)
        print("Porcentaje de postulantes de cada género NBS: " + str(porcentaje_nbs))
        print("Porcentaje de postulantes de cada género FS: " + str(porcentaje_fs))
        print("Porcentaje de postulantes de cada género MS: " + str(porcentaje_ms))



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
