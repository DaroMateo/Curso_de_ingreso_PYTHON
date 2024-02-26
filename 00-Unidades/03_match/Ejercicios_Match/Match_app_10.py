import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD:ejercicios/03_instruccion_match/ejercicio_10/Match_app_10.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
nombre:
apellido:
---
Ejercicio: Match_10
---
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/03_match/Ejercicios_Match/Match_app_10.py
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar un alert con el mensaje “Se viaja”, 
caso contrario mostrar “No se viaja”. 
    Si es invierno: solo se viaja a Bariloche
    Si es verano: se viaja a Mar del plata y Cataratas
    Si es otoño: se viaja a todos los lugares
    Si es primavera: se viaja a todos los lugares menos Bariloche
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        estacion = self.combobox_estaciones.get()
        destino = self.combobox_destino.get()

        match estacion:
            case 'Invierno':
                match destino:
                    case 'Bariloche':
                        mensaje = "SE VIAJA"
                    case _: 
                        mensaje = "NO SE VIAJA"
            case 'Verano':
                match destino:
                    case 'Mar del plata' | 'Cataratas':
                        mensaje = "SE VIAJA"
                    case _: 
                        mensaje = "NO SE VIAJA"
            case 'Otoño':
                match destino:
                    case 'Bariloche'| 'Mar del plata'| 'Cataratas'| 'Cordoba':
                        mensaje = "SE VIAJA"
                    case _: 
                        mensaje = "NO SE VIAJA"
            case 'Primavera':
                match destino:
                    case 'Mar del plata'| 'Cataratas'| 'Cordoba':
                        mensaje = "SE VIAJA"
                    case _: 
                        mensaje = "NO SE VIAJA"
        
        alert("AGENCIA DE VIAJE" , mensaje)


            

            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()