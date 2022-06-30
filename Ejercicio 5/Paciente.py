class Paciente(object):
    __apellido=None
    __nombre=None
    __telefono=None
    __altura=None
    __peso=None

    def __init__(self, apellido, nombre, telefono, altura, peso):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__altura = float(altura)
        self.__peso = float(peso)

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    apellido=self.__apellido,
                                    nombre=self.__nombre,
                                    telefono=self.__telefono,
                                    altura=self.__altura,
                                    peso=self.__peso
                                )
                )
        return d

    def CalcularIMC(self):
        imc = self.__peso/self.__altura**2
        imc2=None
        if imc < 18.5:
            imc2 = "Peso inferior al normal"
        elif 18.5 < imc < 24.9:
            imc2 = "Normal"
        elif 25.0 < imc < 29.9:
            imc2 = "Peso superior al normal"
        elif imc > 30.0:
            imc2 = "Obesidad"
        return "Tu IMC es {} / {}".format(round(imc, 2), imc2)
