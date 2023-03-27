from tkinter import *

root = Tk()
root.title("Calculadora Básica")

num1 = None
num2 = None
operacion = None

#Prohibe agrandar o minimizar la pestaña.
root.resizable(0,0)

#Lo que va a ingresar el usuario.
entrada_texto = Entry(root, bg="LemonChiffon3")
entrada_texto.grid(row=0, column=0, columnspan=4, ipady=20, ipadx=83)

#Botones númericos de la calculadora.
boton1 = Button(root, text="1", width=9, height=3, command = lambda : envia_boton(1))
boton1.grid(row=1, column=0)
boton2 = Button(root, text="2", width=9, height=3, command = lambda : envia_boton(2))
boton2.grid(row=1, column=1)
boton3 = Button(root, text="3", width=9, height=3, command = lambda : envia_boton(3))
boton3.grid(row=1, column=2)
boton4 = Button(root, text="4", width=9, height=3, command = lambda : envia_boton(4))
boton4.grid(row=2, column=0)
boton5 = Button(root, text="5", width=9, height=3, command = lambda : envia_boton(5))
boton5.grid(row=2, column=1)
boton6 = Button(root, text="6", width=9, height=3, command = lambda : envia_boton(6))
boton6.grid(row=2, column=2)
boton7 = Button(root, text="7", width=9, height=3, command = lambda : envia_boton(7))
boton7.grid(row=3, column=0)
boton8 = Button(root, text="8", width=9, height=3, command = lambda : envia_boton(8))
boton8.grid(row=3, column=1)
boton9 = Button(root, text="9", width=9, height=3, command = lambda : envia_boton(9))
boton9.grid(row=3, column=2)
boton0 = Button(root, text="0", width=9, height=3, command = lambda : envia_boton(0))
boton0.grid(row=4, column=1)

def envia_boton(valor):
    anterior = entrada_texto.get()
    entrada_texto.delete(0,END)
    entrada_texto.insert(0,str(anterior) + str(valor))
    
def suma():
    global num1, num2, operacion
    num1 = float(entrada_texto.get())
    entrada_texto.delete(0, END)
    operacion = "suma"
    
def resta():
    global num1, num2, operacion
    num1 = float(entrada_texto.get())
    entrada_texto.delete(0, END)
    operacion = "resta"
    
def multiplicar():
    global num1, num2, operacion
    num1 = float(entrada_texto.get())
    entrada_texto.delete(0, END)
    operacion = "multiplicar"

def division():
    global num1, num2, operacion
    num1 = float(entrada_texto.get())
    entrada_texto.delete(0, END)
    operacion = "dividir"
    
def resultado():
    global num2
    num2 = float(entrada_texto.get())
    entrada_texto.delete(0, END)
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicar":
        resultado = num1 * num2
    elif operacion == "dividir":
        resultado = num1 / num2
    else:
        resultado = 0
    entrada_texto.insert(0, resultado)
    
def borrar():
    entrada_texto.delete(0, END)
    
#Botones de suma, resta, etc.
boton_division = Button(root, text="/", width=9, height=3, command=division)
boton_division.grid(row=1, column=3)
boton_multiplicar = Button(root, text="X", width=9, height=3, command=multiplicar)
boton_multiplicar.grid(row=2, column=3)
boton_suma = Button(root, text="+", width=9, height=3, command=suma)
boton_suma.grid(row=3, column=3)
boton_resta = Button(root, text="-", width=9, height=3, command=resta)
boton_resta.grid(row=4, column=3)
boton_resultado = Button(root, text="=", width=9, height=3, bg="blue", command=resultado)
boton_resultado.grid(row=4, column=2)
boton_borrar = Button(root, text="C", width=9, height=3, bg="pink", command=borrar)
boton_borrar.grid(row=4, column=0)
    
root.mainloop()

