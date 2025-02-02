import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD
<<<<<<< HEAD:ejercicios/03_instruccion_match/ejercicio_09/Match_app_09.py
nombre: Dario Ezequiel
apellido: Mateo
...
Enunciado:
=======
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
nombre:
apellido:
---
Ejercicio: Match_09
---
<<<<<<< HEAD
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/03_match/Ejercicios_Match/Match_app_09.py
=======
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

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
        estaciones = self.combobox_estaciones.get()
        destinos = self.combobox_destino.get()

        precio = 15000
        
        precio =int(precio)
        porcentaje = 1
        

        match estaciones:
            case 'Invierno':
                match destinos:
                    case 'Bariloche':
                        porcentaje = 1.20
                    case 'Mar del plata':
                        porcentaje = 0.80
                    case 'Cataratas' | 'Cordoba':
                        porcentaje = 0.90
            case 'Verano':
                match destinos:
                    case 'Bariloche':
                        porcentaje = 0.80
                    case 'Mar del plata':
                        porcentaje = 1.20
                    case 'Cataratas' | 'Cordoba':
                        porcentaje = 0.90
            case 'Otoño' | 'Primavera':
                match destinos:
                    case 'Bariloche' |'Mar del plata' |'Cataratas' :
                        porcentaje = 1.10
                    
        


        descuento_aplicado = precio * porcentaje
        
        
        descuento_aplicado = int(descuento_aplicado)
        

        alert("Costo final" , str(descuento_aplicado))
    

        



    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()