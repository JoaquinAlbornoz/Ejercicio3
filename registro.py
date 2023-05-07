class Registro:
    def __init__(self,temperatura=0.0,humedad=0.0,presión=0.0):
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presión=presión
    def __str__(self):
        return '\t{}\t{}\t{}'.format(self.__temperatura,self.__humedad,self.__presión)
    def gettemp(self):
        return self.__temperatura
    def gethum(self):
        return self.__humedad
    def getpre(self):
        return self.__presión
    