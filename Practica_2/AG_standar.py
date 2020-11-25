from Individuo import *
from Funciones_seleccion import *
from Funciones_Cruza import *
from Funciones_Mutacion import *

import matplotlib.pyplot as plt

def Generar_poblacion(num_poblacion,num_alelos,opc):

    cromosoma = []
    poblacion = []

    for i in range(1,(num_poblacion*num_alelos)+1):
        
        if i%num_alelos == 0:

            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)
            
            ind = Individuo(cromosoma)
            ind.Generar_fenotipo()
            ind.Generar_Aptitud()
            poblacion.append(ind)
            cromosoma = []
        else:
            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)
        
    


    # print(len(arreglo_bin))
    # print(arreglo_bin)   

    # arreglo_x = [i for i in range(1,num_poblacion+1)]

    # print(len(poblacion))
    # print(poblacion)


    # plt.stem(arreglo_x, poblacion)
    # plt.show()
      

if __name__ == "__main__":
    
    opc = int(input('''

            Selecciona la función (escribe número).

            1. f(x) = x^2
            2. f(X) = |(x-5)/2+sin(x)|
            3. f(x) = (e^x - e^-x)/x 
    '''))

    num_poblacion = 4
    num_generacion =  int(input("Ponga el numero de Generaciones \n"))
    num_alelos =  int(input("Ponga el tamaño de los alelos \n"))
    
    poblacion = []

    for i in range(num_generacion):
        
        poblacion = Generar_poblacion(num_poblacion,num_alelos,opc)





     

    


