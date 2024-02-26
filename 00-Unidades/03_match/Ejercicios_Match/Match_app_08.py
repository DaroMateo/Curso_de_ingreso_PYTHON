import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD:ejercicios/03_instruccion_match/ejercicio_08/Match_app_08.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
nombre:
apellido:
---
Ejercicio: Match_08
---
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/03_match/Ejercicios_Match/Match_app_08.py
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
‘Informar’ indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destinos = self.combobox_destino.get()

        match destinos:
            case 'Bariloche' | 'Ushuaia':
                mensaje = "FRIO"
            case 'Cataratas':
                mensaje = "CALOR"
            case 'Mar del plata':
                mensaje = "FRIO/CALOR"
        
        alert("CLIMA" , mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()