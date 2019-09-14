#!/usr/bin/env python3
from tkinter import *
import random

PADX = 5

ventana = Tk()
ventana.title("Calculadora")


def boton_click(valor):
    # END e INSERT son valores indice en el visor Entry
    visor.insert(INSERT, valor)


def boton_borrar():
    visor.delete(0, END)


def boton_igual():
    valor = eval(visor.get())
    boton_borrar()
    boton_click(valor)


def boton_rand():
    if len(visor.get()):
        chr = visor.get()[-1]
        if chr not in ('(', '/', '*', '-', '+'):
            boton_borrar()
    boton_click(round(random.random(), 3))


visor = Entry(ventana, font=("Calibri 20"))
visor.grid(row=0, column=0, padx=50, pady=5, columnspan=4)

boton0 = Button(ventana, text="0", width=18, height=2,
                command=lambda: boton_click('0'))
boton1 = Button(ventana, text="1", width=4, height=2,
                command=lambda: boton_click('1'))
boton2 = Button(ventana, text="2", width=4, height=2,
                command=lambda: boton_click('2'))
boton3 = Button(ventana, text="3", width=4, height=2,
                command=lambda: boton_click('3'))
boton4 = Button(ventana, text="4", width=4, height=2,
                command=lambda: boton_click('4'))
boton5 = Button(ventana, text="5", width=4, height=2,
                command=lambda: boton_click('5'))
boton6 = Button(ventana, text="6", width=4, height=2,
                command=lambda: boton_click('6'))
boton7 = Button(ventana, text="7", width=4, height=2,
                command=lambda: boton_click('7'))
boton8 = Button(ventana, text="8", width=4, height=2,
                command=lambda: boton_click('8'))
boton9 = Button(ventana, text="9", width=4, height=2,
                command=lambda: boton_click('9'))

botonPunto = Button(ventana, text=".", width=4, height=2,
                    command=lambda: boton_click('.'))
botonBorrar = Button(ventana, text="AC", width=4, height=2,
                     command=boton_borrar, fg='red')
botonRand = Button(ventana, text="RND", width=4, height=2,
                   command=boton_rand, fg='blue')
botonMultiplicar = Button(ventana, text="*", width=4, height=2,
                          command=lambda: boton_click('*'))
botonDividir = Button(ventana, text="/", width=4, height=2,
                      command=lambda: boton_click('/'))
botonRestar = Button(ventana, text="-", width=4, height=2,
                     command=lambda: boton_click('-'))
botonModulo = Button(ventana, text="MOD", width=4, height=2,
                     command=lambda: boton_click('%'), fg='blue')
botonSumar = Button(ventana, text="+", width=4, height=6,
                    command=lambda: boton_click('+'))
botonIgual = Button(ventana, text="=", width=4, height=6,
                    command=boton_igual, fg='blue')
botonParentesisCerrar = Button(ventana, text=")", width=4, height=2,
                               command=lambda: boton_click(')'))
botonParentesisAbrir = Button(ventana, text="(", width=4, height=2,
                              command=lambda: boton_click('('))

# Arreglo de la interfaz gráfica
botonRand.grid(row=1, column=0, padx=PADX, pady=5)
botonParentesisAbrir.grid(row=1, column=1, padx=PADX, pady=5)
botonParentesisCerrar.grid(row=1, column=2, padx=PADX, pady=5)
botonModulo.grid(row=1, column=3, padx=PADX, pady=5)

botonBorrar.grid(row=2, column=0, padx=PADX, pady=5)
botonDividir.grid(row=2, column=1, padx=PADX, pady=5)
botonMultiplicar.grid(row=2, column=2, padx=PADX, pady=5)
botonRestar.grid(row=2, column=3, padx=PADX, pady=5)

boton7.grid(row=3, column=0, padx=PADX, pady=5)
boton8.grid(row=3, column=1, padx=PADX, pady=5)
boton9.grid(row=3, column=2, padx=PADX, pady=5)
botonSumar.grid(row=3, column=3, padx=PADX, pady=5, rowspan=2)

boton4.grid(row=4, column=0, padx=PADX, pady=5)
boton5.grid(row=4, column=1, padx=PADX, pady=5)
boton6.grid(row=4, column=2, padx=PADX, pady=5)

boton1.grid(row=5, column=0, padx=PADX, pady=5)
boton2.grid(row=5, column=1, padx=PADX, pady=5)
boton3.grid(row=5, column=2, padx=PADX, pady=5)
botonIgual.grid(row=5, column=3, padx=PADX, pady=5, rowspan=2)

boton0.grid(row=6, column=0, padx=PADX, pady=0, columnspan=2)
botonPunto.grid(row=6, column=2, padx=PADX, pady=5)

ventana.mainloop()
