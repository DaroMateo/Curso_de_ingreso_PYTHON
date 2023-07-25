import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
       apellido = None 
        edad= None 
        estado_civil = None 
        legajo = None

        apellido = prompt("", "APELLIDO")
        while apellido is None or apellido == "" or apellido.isdigit():
            if apellido is None:
                if question("", "DESEA CONTINUAR?"):
                    break

            apellido = prompt("", "APELLIDO")

        edad = prompt("", "EDAD")
        while edad is None or edad == "" or not edad.isdigit():
            if edad is None:
                if question("", "DESEA CONTINUAR?"):
                    break

            edad = prompt("", "EDAD")

        estado_civil = prompt("", "ESTADO CIVIL")
        while estado_civil is None or (estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a"):
            if estado_civil is None:
                if question("", "DESEA CONTINUAR?"):
                    break

            estado_civil = prompt("", "ESTADO CIVIL")

        legajo = prompt("", "LEGAJO")
        while legajo is None or legajo == "" or not legajo.isdigit() or int(legajo) < 1000 or int(legajo) > 9999:
            if legajo is None:
                if question("", "DESEA CONTINUAR?"):
                    break

            legajo = prompt("", "LEGAJO")

        self.txt_apellido.delete(0, 200)
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.delete(0, 200)
        self.txt_edad.insert(0, edad)
        self.combobox_tipo.set(estado_civil)
        self.txt_legajo.delete(0, 200)
        self.txt_legajo.insert(0, legajo)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
