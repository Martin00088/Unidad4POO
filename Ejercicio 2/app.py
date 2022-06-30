from tkinter import *
from tkinter import ttk

class Aplicacion():
    __preciosinIva=None
    __iva=None
    __precioconIVA=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('500x300')
        self.__ventana.configure(bg = 'beige')
        self.__ventana.title('Calculo de IVA')

        #Frame
        frame = ttk.Frame(self.__ventana)
        frame.grid(column = 0, row=0 , sticky =(N, W, E,S))

        self.__preciosinIva=StringVar()
        self.__iva=StringVar()
        self.__precioconIVA=StringVar()

        # Precio sin IVA
        Label(frame, text = 'Precio sin IVA:',font="Verdana",width=20).grid(row = 1, column = 0)
        self.PreciosinIVAEntry=ttk.Entry(frame, width=10, textvariable = self.__preciosinIva, justify='center')
        self.PreciosinIVAEntry.grid(row = 1, column = 1)

        #Opciones
        self.selec = IntVar() # Como StrinVar pero en entero
        ttk.Radiobutton(frame, text="IVA 21%", variable=self.selec, 
                    value=0).grid(row = 3, column = 0)
        ttk.Radiobutton(frame, text="IVA 10.5%", variable=self.selec,
                    value=1).grid(row = 4, column = 0)

        # IVA
        Label(frame, text = 'IVA: ',font = "Verdana").grid(row = 5, column = 0)
        self.IVAEntry=ttk.Entry(frame, width=10, textvariable = self.__iva, justify = 'center',state="disable")
        self.IVAEntry.grid(row = 5, column = 1)

        # Precio Con IVA
        Label(frame, text = 'Precio con IVA: ',font="Verdana").grid(row = 6, column = 0)
        self.PrecioConIVAEntry=ttk.Entry(frame, width=10, textvariable = self.__precioconIVA, justify='center',state="disable")
        self.PrecioConIVAEntry.grid(row = 6, column = 1)

        ttk.Button(frame, text = 'Calcular', command = self.calcular).grid(row = 7,column= 0, sticky = W + E)
        ttk.Button(frame, text = 'Salir', command=self.__ventana.destroy).grid(row = 7, column = 1, sticky = W + E)

        self.__ventana.mainloop()

    def calcular(self):
        precio_base=float(self.PreciosinIVAEntry.get())
        if self.selec.get() == 0:
            iva=(precio_base * 21)/100
        elif self.selec.get() == 1:
            iva=(precio_base * 10.5)/100
        self.__iva.set(iva)   
        self.__precioconIVA.set( "{}".format(precio_base + iva))

if __name__ == '__main__':
    app=Aplicacion()    

