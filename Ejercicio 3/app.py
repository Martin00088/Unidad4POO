from tkinter import *   
from tkinter import ttk
from click import command
import requests
from decimal import Decimal

datos=requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
datos=datos.json()


class Aplicacion():
    __dolares=None
    __pesos=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('500x300')
        self.__ventana.configure(bg = 'beige')
        self.__ventana.title('Conversor de moneda')

        #Frame
        frame = ttk.Frame(self.__ventana)
        frame.grid(column = 0, row=0 , sticky=N + W+ E+ S)
        self.__dolares = StringVar()
        self.__dolares.trace("w", self.calcular)

        # Dolares
        Label(frame, text = 'dolares',font="Verdana",width=10).grid(row = 1, column = 3)
        self.DolaresEntry=ttk.Entry(frame, width=10, textvariable = self.__dolares, justify='center')
        self.DolaresEntry.grid(row = 1, column = 2)
        
        # Pesos
        Label(frame, text = 'Es equivalente a ',font="Verdana").grid(row = 2, column = 1)
        Label(frame, text = 'pesos ',font="Verdana").grid(row = 2, column = 3)
        
        self.__mensaje = Label(frame,text = '', fg = 'red',font=('Verdana',10,'bold'))
        self.__mensaje.grid(row = 2, column = 2)
        
        ttk.Button(frame, text = 'Salir', command=self.__ventana.destroy).grid(row = 3, column = 3, sticky = W + E)
        
        self.__ventana.mainloop()

    def calcular(self, *args):
        i=0
        band=False
        preciodolarblue=None
        while i < len(datos) and band == False:
            if datos[i]["casa"]["nombre"] == "Oficial":
                preciodolarblue = datos[i]["casa"]["venta"]
                band=True
            i += 1
        preciodolarblue = preciodolarblue.replace(",", ".")
        dolares = float(self.DolaresEntry.get())
        self.__mensaje['text']='{}'.format(float(float(preciodolarblue)*dolares))


if __name__ == '__main__':
    app=Aplicacion()    
