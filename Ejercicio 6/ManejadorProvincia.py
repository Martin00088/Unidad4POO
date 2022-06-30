from Provincia import Provincia
from claseObjectEncoder import ObjectEncoder
from vistaProvincia import NewProvincia


class ManejadorProvincia:
    __provincias = None
    __seleccion = None
    __vista = None
    __jsonF = ObjectEncoder()

    def __init__(self, vista):
        self.__jsonF = ObjectEncoder()
        self.__provincias = []
        self.__vista = vista
        self.__seleccion = -1

    def CargaLista(self):
        jsonF = ObjectEncoder()
        jsonF.decodificarDiccionario(self.__provincias)

    def toJSON(self):
        lista=[]
        for paciente in self.__provincias:
            d = paciente.toJSON()
            lista.append(d)
        return lista

    def getListaProvincia(self):
        return self.__provincias

    def obtenerIndiceProvincia(self, provincia):
        bandera = False
        i = 0
        while i < len(self.__provincias) and not bandera:
            if self.__provincias[i] == provincia:
                bandera = True
            else:
                i += 1
        return i

    def start(self):
        for p in self.__provincias:
            self.__vista.agregarprovincia(p)
        self.__vista.mainloop()

    def guardarCambios(self):
        self.__jsonF.guardarJSONArchivo(self.toJSON(), "datos.json")

    def agregarProvincia(self):
        provincia = NewProvincia(self.__vista).show()
        if provincia:
            self.__provincias.append(provincia)
            self.__vista.agregarprovincia(provincia)
            self.guardarCambios()

    def seleccionarProvincia(self, index):
        self.__seleccion = index
        self.__vista.verProvinciaEnForm(self.__provincias[self.__seleccion])
