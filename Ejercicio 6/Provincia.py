import requests


class Provincia(object):
    __nombre = None
    __capital = None
    __canthabitantes = None
    __cantdep_partido = None
    __temperatura = None
    __stermina = None
    __humedad = None
    __datos = None

    def __init__(self, nombre, capital, CantidadHabitantes, CantidadDepPartidos):
        self.__nombre = str(nombre)
        self.__capital = str(capital)
        self.__canthabitantes = CantidadHabitantes
        self.__cantdep_partido = CantidadDepPartidos
        datos = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+self.__nombre+','+self.__capital+'&units=metric&APPID=c11ac3db89f712f69b4de0396d61f22a')
        self.__datos = datos.json()
        print(self.__datos)

    def getNombre(self):
        return self.__nombre

    def getCapital(self):
        return self.__capital

    def getCantHab(self):
        return self.__canthabitantes

    def getCantDepPart(self):
        return self.__cantdep_partido

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    nombre=self.__nombre,
                                    capital=self.__capital,
                                    CantidadHabitantes=self.__canthabitantes,
                                    CantidadDepPartidos=self.__cantdep_partido,
                                )
                )
        return d

    def getTemperatura(self):
        temp = self.__datos["main"]["temp"]
        return temp

    def getSTermica(self):
        stermica = self.__datos["main"]["feels_like"]
        return stermica

    def getHumedad(self):
        humedad = self.__datos['main']['humidity']
        return humedad
