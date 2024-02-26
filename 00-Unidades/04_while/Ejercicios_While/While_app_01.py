import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
<<<<<<< HEAD
<<<<<<< HEAD:ejercicios/04_intruccion_while/ejercicio_01/While_app_01.py
nombre: Dario Ezequiel
apellido: Mateo
...
=======
nombre:
apellido:
---
Ejercicio: while_01
---
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/04_while/Ejercicios_While/While_app_01.py
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
=======
nombre:
apellido:
---
<<<<<<<< HEAD:00-Unidades/04_while/Ejercicios_While/While_app_02bis.py
Ejercicio: while_02bis
========
Ejercicio: while_01
>>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/04_while/Ejercicios_While/While_app_01.py
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
<<<<<<< HEAD
        numero = 1
        while numero<= 10:
            alert( "NUMERO" , numero)
            numero += 1
=======
        pass
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()