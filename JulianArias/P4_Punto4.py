import tkinter as tk #Importa librería Python
from tkinter import ttk

####METODOS#####

def calcularArea():
    
    seleccion = combo.get()

    print(seleccion)

    if seleccion == "Rectangulo":
        print("calcularareaRectangulo")
        etiquetaResult.config(text=f"{float(baseCasilla.get())*float(alturaCasilla.get())}")

    elif seleccion == "Triangulo":
        print("calcularareaTriangulo")
        etiquetaResult.config(text=f"{float(baseCasilla.get())*float(alturaCasilla.get())*0.5}")

######EJECUCION##################

ventana = tk.Tk() #Crea objeto ventana

ventana.title("Mi Ventana")
ventana.geometry("400x300+500+200")


combo = ttk.Combobox(state="readonly",values=["Rectangulo", "Triangulo"])
combo.place(x=130, y=150)


etiquetaBase = tk.Label(ventana, text="Base: ")
etiquetaBase.pack()
baseCasilla = tk.Entry(ventana, width=10)
baseCasilla.pack()
etiquetaAltura = tk.Label(ventana, text="Altura: ")
etiquetaAltura.pack()
alturaCasilla = tk.Entry(ventana, width=10)
alturaCasilla.pack()

boton = tk.Button(ventana, text="Calcular Area", command=calcularArea)
boton.pack()

etiquetaTextR = tk.Label(ventana, text="Resultado: ")
etiquetaTextR.pack()

etiquetaResult = tk.Label(ventana, text="")
etiquetaResult.pack()

ventana.mainloop()    #Genera ventana
