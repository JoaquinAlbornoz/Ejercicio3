import csv
from registro import Registro
class Tablahyd:
    def __init__(self,f=1,c=1):
        self.__tabla=[]
        self.__fila=f
        self.__columna=c
    def inicializar(self):
        for f in range(self.__fila):
            self.__tabla.append([None]*self.__columna)
    def agregareg(self):
        self.inicializar()
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Ejercicio 3\\Reg.csv','r') as a:
            reader=csv.reader(a,delimiter=';')
            for f in reader:
                reg=Registro(int(f[2]),int(f[3]),float(f[4]))
                self.__tabla[int(f[0])-1][int(f[1])]=reg
    def mayor(self):
        temp = -100
        hum = 0
        pres= 0
        for i in range(self.__fila):
            for j in range(self.__columna):
                if self.__tabla[i][j].gettemp()>temp:
                    temp = self.__tabla[i][j].gettemp()
                    may_tem=[i+1,j]
                elif self.__tabla[i][j].gethum()>hum:
                    hum = self.__tabla[i][j].gethum()
                    may_hum=[i+1,j]
                elif self.__tabla[i][j].getpre()>pres:
                    may_pres=[i+1,j]
        print('El dia con mayor temperatura fue {} a la hora {}\n El dia con mayor humedad fue {} a la hora {}\n El dia con mayor presion atmosferica fue {} a la hora {}\n'.format(may_tem[0],may_tem[1],may_hum[0],may_hum[1],may_pres[0],may_pres[1]))
    def menor(self):
        temp = 100
        hum = 101
        pres= 2000
        for i in range(self.__fila):
            for j in range(self.__columna):
                if self.__tabla[i][j].gettemp()<temp:
                    temp = self.__tabla[i][j].gettemp()
                    men_tem=[i+1,j]
                elif self.__tabla[i][j].gethum()<hum:
                    hum = self.__tabla[i][j].gethum()
                    men_hum=[i+1,j]
                elif self.__tabla[i][j].getpre()<pres:
                    men_pres=[i+1,j]
        print('El dia con menor temperatura fue {} a la hora {}\n El dia con menor humedad fue {} a la hora {}\n El dia con menor presion atmosferica fue {} a la hora {}\n'.format(men_tem[0],men_tem[1],men_hum[0],men_hum[1],men_pres[0],men_pres[1]))
    def promh(self):
        for j in range(self.__columna):
            p=0.0
            for i in range(self.__fila):
                p+=self.__tabla[i][j].gettemp()
            print('Promedio de temperatura a la hora {}: {}'.format(j,p/self.__fila))
    def mostrard(self,i):
        print('Hora\tTemperatura\tHumedad\tPresión')
        for j in range(self.__columna):
            print('{}\t{}'.format(j,self.__tabla[i][j]))