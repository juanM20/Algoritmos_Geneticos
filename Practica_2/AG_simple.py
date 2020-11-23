import random
import math
import matplotlib.pyplot as plt


def funcion1(num):
    return num**2

def funcion2(num):
    return abs((num-5)/(2+math.sin(num)))

def funcion3(num):
    return ((math.exp(num) - math.exp(-num))/num)


def Generar_poblacion(num_poblacion,num_alelos,opc):

    cromosoma = []
    arreglo_bin = []
    poblacion = []

    for i in range(1,(num_poblacion*num_alelos)+1):
        
        if i%num_alelos == 0:

            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)
            
            arreglo_bin.append(cromosoma)
            cromosoma = []
        else:
            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)
        
    # print(len(arreglo_bin))
    print(arreglo_bin)   

    str_bin = ""

    for i in range(len(arreglo_bin)):

        str_bin = "".join( map(str,arreglo_bin[i]) )

        if opc == 1:
            poblacion.append(round(funcion1(int(str_bin,2)),2))
        elif opc == 2:
            poblacion.append(round(funcion2(int(str_bin,2)),2))
        elif opc == 3:
            poblacion.append(round(funcion3(int(str_bin,2)),2))  
        
    # arreglo_x = [i for i in range(1,num_poblacion+1)]

    # print(len(poblacion))
    # print(poblacion)


    # plt.stem(arreglo_x, poblacion)
    # plt.show()
  

    

if __name__ == "__main__":


    variable = 10
    variable2 = 2

    opc = int(input('''

            Selecciona la función (escribe número).

            1. f(x) = x^2
            2. f(X) = |(x-5)/2+sin(x)|
            3. f(x) = (e^x - e^-x)/x 
    '''))

    num_poblacion = 4
    num_generacion =  int(input("Ponga el numero de Generaciones \n"))
    num_alelos =  int(input("Ponga el tamaño de los alelos \n"))
    for i in range(num_generacion):
        
        Generar_poblacion(num_poblacion,num_alelos,opc)
     

    


