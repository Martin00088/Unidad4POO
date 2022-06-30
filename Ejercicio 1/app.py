from tkinter import *
from tkinter import ttk

class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __mensaje = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('500x300')
        self.__ventana.configure(bg = 'beige')
        self.__ventana.title('Calculadora de IMC')
        frame = ttk.Frame(self.__ventana)
        frame.grid(column = 0, row=0 , sticky =(N, W, E,S))

        self.__peso=StringVar()
        self.__altura=StringVar()
        
        #Style
        ttk.Style().configure("TButton", padding=6, relief="flat",
        background = "green")
        ttk.Style().configure("TLabel", padding=6, relief="flat",
        background = "green")

        # Altura
        Label(frame, text = 'Altura:',font="Verdana",width=20).grid(row = 1, column = 0)
        Label(frame, text = 'cm',font="Verdana").grid(row = 1, column = 3)
        self.AlturaEntry=ttk.Entry(frame, width=10, textvariable = self.__altura, justify='center')
        self.AlturaEntry.grid(row = 1, column = 1)

        # Peso
        Label(frame, text = 'Peso: ',font="Verdana").grid(row = 2, column = 0)
        Label(frame, text = 'kg',font="Verdana").grid(row = 2, column = 3)
        self.PesoEntry=ttk.Entry(frame, width=10, textvariable = self.__peso, justify='center')
        self.PesoEntry.grid(row = 2, column = 1)

        ttk.Button(frame, text = 'Calcular', command = self.calcular).grid(row = 3,column= 0, sticky = W + E)
        ttk.Button(frame, text = 'Limpiar', command = self.limpiar).grid(row = 3, column = 1, sticky = W + E)
        
        self.__mensaje = Label(text = '', fg = 'red',font=('Verdana',10,'bold'))
        self.__mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
        self.__ventana.mainloop()

    def calcular(self):
        peso = float(self.PesoEntry.get())
        altura = float(self.AlturaEntry.get())
        altura=altura/100
        imc= peso / altura**2 

        if imc < 18.5:
            imc2 = "Peso inferior al normal"
        elif imc > 18.5 and imc < 24.9:
            imc2 ="Normal"
        elif imc > 25.0 and imc < 29.9:
            imc2="Peso superior al normal"
        elif imc > 30.0 :
            imc2="Obesidad"
        self.__mensaje['text'] = "Tu indice de Masa Corporal (IMC) es: {}\n{}".format(imc,imc2)

    def limpiar(self):
        self.__mensaje['text'] = ''

if __name__ == '__main__':
    app=Aplicacion()

