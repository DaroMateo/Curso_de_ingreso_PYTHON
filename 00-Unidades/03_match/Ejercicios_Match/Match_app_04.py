import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD:ejercicios/03_instruccion_match/ejercicio_04/Match_app_04.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
nombre:
apellido:
---
Ejercicio: Match_04
---
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/03_match/Ejercicios_Match/Match_app_04.py
Enuciado:
Al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si tiene 28 días
    Si tiene 30 días
    Si tiene 31 días
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        meses = self.combobox_mes.get()

        match meses:
            case 'Enero' | 'Marzo'| 'Mayo'| 'Julio'| 'Agosto' | 'Octubre' | 'Diciembre':
             mensaje = "Si tiene 31 días"
            case 'Febrero':
                mensaje = "Si tiene 28 días"
            case 'Abril' | 'Junio' | 'Septiembre' | 'Noviembre':
                mensaje = "Si tiene 30 días"
            
        alert("DIAS" , mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()