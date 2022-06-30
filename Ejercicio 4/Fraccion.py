from fractions import gcd

class Fraccion:
    __numerador=None
    __denominador=None

    def __init__(self,numerador,denominador):
        self.__numerador=float(numerador)
        self.__denominador=float(denominador)

    def __add__(self,other):
        if isinstance(other,Fraccion):
            denominador = self.__denominador * other.__denominador
            return Fraccion(self.__numerador * other.__denominador + self.__denominador * other.__numerador,denominador)
        else:
            return Fraccion((self.__numerador / self.__denominador) + ((self.__denominador * float(other))/self.__denominador),self.__denominador)

    def __sub__(self,other):
        if isinstance(other,Fraccion):
            denominador = self.__denominador * other.__denominador
            return Fraccion(self.__numerador * other.__denominador - self.__denominador * other.__numerador,denominador)
        else:
            return Fraccion((self.__numerador / self.__denominador) - ((self.__denominador * float(other))/self.__denominador),self.__denominador) 

    def __mul__(self,other):
        if isinstance(other,Fraccion):
            denominador = self.__denominador * other.__denominador
            numerador = self.__numerador * other.__numerador
            return Fraccion(numerador,denominador)
        else:
            denominador = self.__denominador
            numerador = self.__numerador * float(other)
            return Fraccion(numerador,denominador) 

    def __div__(self,other):
        if isinstance(other,Fraccion):
            denominador = self.__denominador * other.__numerador
            numerador = self.__numerador * other.__denominador
            return Fraccion(numerador,denominador)
        else:
            denominador = self.__denominador * float(other)
            numerador = self.__numerador
            return Fraccion(numerador,denominador) 

    def __str__(self):
        return "{}/{}".format(self.__numerador,self.__denominador)

    def simplifica(self):
        simp = Fraccion(self.__numerador, self.__denominador)
        mcd = gcd(self.__numerador, self.__denominador)
        simp.__numerador = self.__numerador / mcd
        simp.__denominador = self.__numerador / mcd
        return(simp)