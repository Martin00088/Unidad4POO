from Paciente import Paciente
from claseObjectEncoder import ObjectEncoder
from vistaPaciente import NewPaciente


class ManejadorPaciente:
    __pacientes = None
    __seleccion = None
    __vista = None
    __jsonF = ObjectEncoder()

    def __init__(self, vista):
        self.__jsonF = ObjectEncoder()
        self.__pacientes = []
        self.__vista = vista
        self.__seleccion = -1

    def CargaLista(self):
        jsonF = ObjectEncoder()
        jsonF.decodificarDiccionario(self.__pacientes)

    def toJSON(self):
        lista=[]
        for paciente in self.__pacientes:
            d = paciente.toJSON()
            lista.append(d)
        return lista
    """
    def CargaJson(self):
        paciente1 = Paciente('Rueda', 'Melisa', '(264)4777222',180,70)
        paciente2 = Paciente('Lopez', 'Carlos', '(261)4888111',180,70)
        paciente3 = Paciente('Perez', 'Maira','(264)5111222',180,70)
        paciente4 = Paciente('Altamirano', 'Sandra','(263)6478912',180,70)
        paciente5 = Paciente('Artime', 'Luis', '(264)4558699',180,70)
        paciente1 = paciente1.toJSON()
        paciente2 = paciente2.toJSON()
        paciente3 = paciente3.toJSON()
        paciente4 = paciente4.toJSON()
        paciente5 = paciente5.toJSON()
        lista = [paciente1, paciente2, paciente3, paciente4, paciente5]
        self.__jsonF.guardarJSONArchivo(lista, "pacientes.json")
    """
    def getListaPaciente(self):
        return self.__pacientes

    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i = 0
        while i < len(self.__pacientes) and not bandera:
            if self.__pacientes[i] == paciente:
                bandera = True
            else:
                i += 1
        return i

    def start(self):
        for c in self.__pacientes:
            self.__vista.agregarpaciente(c)
        self.__vista.mainloop()

    def guardarCambios(self):
        self.__jsonF.guardarJSONArchivo(self.toJSON(), "pacientes.json")

    def agregarPaciente(self):
        paciente = NewPaciente(self.__vista).show()
        if paciente:
            print(len(self.__pacientes))
            self.__pacientes.append(paciente)
            print(len(self.__pacientes))
            self.__vista.agregarpaciente(paciente)
            self.guardarCambios()

    def seleccionarPaciente(self, index):
        self.__seleccion = index
        self.__vista.verPacienteEnForm(self.__pacientes[self.__seleccion])

    def updatePaciente(self, paciente):
        self.__pacientes[self.__seleccion] = paciente
        return self.__pacientes[self.__seleccion]

    def modificarPaciente(self):
        detallesPaciente = self.__vista.obtenerDetalles()
        paciente = self.updatePaciente(detallesPaciente)
        self.__pacientes[self.__seleccion] = paciente
        self.__vista.modificarpaciente(paciente, self.__seleccion)
        self.guardarCambios()

    def deletePaciente(self):
        self.__pacientes.pop(self.__seleccion)
        self.__vista.borrarPaciente(self.__seleccion)
        self.guardarCambios()

    def calcularIMC(self):
        IMC = self.__pacientes[self.__seleccion].CalcularIMC()
        self.__vista.CalcularIMC(IMC)
