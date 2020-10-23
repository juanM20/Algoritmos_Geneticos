import random
import matplotlib.pyplot as plt


def funcion(num):
    return num**2

def Generar_poblacion(num_poblacion):

    cromosoma = []
    arreglo_bin = []
    poblacion = []

    for i in range(1,(num_poblacion*4)+1):
        
        if i%4 == 0:

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
        
    print(len(arreglo_bin))
    print(arreglo_bin)   

    str_bin = ""

    for i in range(len(arreglo_bin)):

        str_bin = "".join( map(str,arreglo_bin[i]) )
        poblacion.append(funcion(int(str_bin,2)))
    
    arreglo_x = [i for i in range(1,15+1)]

    print(len(poblacion))
    print(poblacion)

    plt.plot(arreglo_x, poblacion)
    plt.show()
         




if __name__ == "__main__":

    num_poblacion = 15
    Generar_poblacion(num_poblacion)
     

    


