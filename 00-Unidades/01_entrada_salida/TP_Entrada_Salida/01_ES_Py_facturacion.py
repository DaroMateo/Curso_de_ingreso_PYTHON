import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: ES_Facturaciones
---
Enunciado:
<<<<<<< HEAD:ejercicios/07_tps/01_E-S_ferrete_facturacion/app.py


A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

* Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
    2- Peso promedio (en onzas) 
    3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    6- Informar la cantidad de articulos que superan el peso promedio
    7- Informar la cantidad de articulos que NO superan el peso promedio
    8- Indicar los pesos repetidos (gramos)
    9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
=======
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/01_entrada_salida/TP_Entrada_Salida/01_ES_Py_facturacion.py
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

<<<<<<< HEAD:ejercicios/07_tps/01_E-S_ferrete_facturacion/app.py
        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")
=======
        self.title("UTN FRA")
>>>>>>> 277afc52c540c0c72fe55761e1c978c933b67b86:00-Unidades/01_entrada_salida/TP_Entrada_Salida/01_ES_Py_facturacion.py

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):
        peso = self.txt_peso_articulo.get()
        lista= self.combobox_tipo_de_peso.get()

        if not peso.isalpha() or float(peso) == 0:
            alert("", "error al validar")
        else:
            match lista:
                case "Onzas":
                    peso = float(peso) * 28.3495
                case "Gramos":
                    peso = float(peso) * 0.035274
        self.lista_pesos.append(peso)
        peso = str(peso)
        alert("","se cargo  correctamente")
    def btn_mostrar_on_click(self):
            contador = 0
            print("Listas de pesos:\n")

            for peso in self.lista_pesos:
                pesos_onzas= float(peso) *0.035274
                mensaje = "Gramos: " + str(peso) + "Onzas: )" +str(pesos_onzas)
                print(mensaje)
                contador += 1

            #for i in range(0, len(self.lista_pesos),1):
            #    pesos_onzas= self.lista_pesos[i] *0.035274
            #    mensaje = "Gramos: " + str(self.lista_pesos[i]) + "Onzas: )" +str(pesos_onzas)
            #    print(mensaje)
    def btn_informar_on_click(self):
       #eje 0 : Valor (en onzas) y posicion del articulo mas pesado
       #pesado=None
       #for i in range(0, len(self.lista_pesos),1):
       #    if i == 0 or self.lista[i] > pesado:
       #       pesado=self.lista_pesos[i]
       #       posicion = i
       #
       #if pesado is not None:
       #    print("articulo mas pesado\nvalor de onzas{0}oz de la lista".format(pesado,poscision))
       #else:
       #    print(la lista esta vacia)
       
       #  eje 8 : Indicar los pesos repetidos (gramos)
       #(10,5,3,9,10,5)
        #10 primer indice
       #for peso in self.lista_pesos:
        #   contador = 0
        #   #10 primer indice
        #   for j in self.lista_pesos:
        #       if i==j:
        #           if contador > 0: #1
        #               print(i)
        #           contador += 1
        #lista_mostrar=[]
        #for peso in self.lista_pesos:
        #   if self.lista_pesos.count(peso)>1 and lista_mostrar.count(peso)==0:
        #       lista_mostrar.append(peso)
        #print(lista_mostrar)
         peso = len(self.lista_pesos)
         acumulador=0
         contador=0
         if peso > 0:
             acumulador += peso
             contador+=1
             promedio_onzas= peso/contador
             promedio_granos= peso/contador

         tipo= self.combobox_tipo_de_peso.set()
         promedio_mayor=0
         promedio_menor=0
         for tipo in self.lista_pesos:
            peso_mayor= 0
            if tipo > peso_mayor:
                promedio_mayor.append(tipo)
            else:
                promedio_menor.append(tipo)
         print("PROMEDIO" + promedio_granos)
         print("Promedio" + promedio_onzas)
         print("Kilomentrasje que supera el promedio: " + str(promedio_mayor))
         print("Kilomentrasje que NO supera el promedio" + str(promedio_menor))

         #peso=self.lista_pesos
         #onzas = self.combobox_tipo_de_peso.get()
         #pesado = self.combobox_tipode_peso.get()
         #for i in self.combobox_tipo_de_peso("Granos"):
         # eje 1
         #   if i > 0:
         #       if pesado == None:
         #         pesado = i 
         #       elif pesado < i:
         #        pesado = i
         #       
         #       pesado=float(pesado)
         #       pesado += i
         #eje 2   
         #   elif self.combobox_tipo_de_peso("Onzas"):
         #        onzas += peso
         #        onzas += 1
         #   promedio = peso/onzas


                
        #    print(promedio)
        #    print(pesado)   
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
