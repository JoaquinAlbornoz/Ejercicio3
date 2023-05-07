from tabla import Tablahyd
if __name__=='__main__':
    matriz=Tablahyd(5,24)
    matriz.agregareg()
    s=1
    while s==1 or s==2 or s==3:
        s=int(input('1.Mostrar menor y mayor por valor\n2.Mostrar promedio mensual por hora\n3.Valores de un dia determinado\nIngrese opcion, cualquier otro numero para finalizar:'))
        print('\n')
        match s:
            case 1:
                matriz.menor()
                matriz.mayor()
            case 2:
                matriz.promh()
            case 3:
                i=int(input('Ingrese dia:'))-1
                matriz.mostrard(i)