import json
from pathlib import Path
from Paciente import Paciente


class ObjectEncoder(object):

    def decodificarDiccionario(self, lista):
        d = self.leerJSONArchivo("pacientes.json")
        for elem in d:
            if '__class__' not in elem:
                print("No se encuentra en la clase")
            else:
                nombreclase = elem['__class__']
                class_ = eval(nombreclase)
                if nombreclase == "Paciente":
                    atributos = elem["__atributos__"]
                    P = class_(**atributos)
                    lista.append(P)
                else:
                    print("No se puede agregar")

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
        return diccionario

    def convertirADiccionario(self, elem):
        return json.loads(elem.toJSON())
