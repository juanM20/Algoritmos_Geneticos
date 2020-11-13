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
    
    arreglo_x = [i for i in range(1,num_poblacion+1)]

    # print(len(poblacion))
    #print(poblacion)


    suma = 0

    for i in range(len(poblacion)):
        suma = suma + poblacion[i]

    media = suma/len(poblacion)
    media = round(media,2)

    print("Población: ",poblacion,"")
    print("suma: ",round(suma,2))
    print("media: ", media)

    probabilidad = []

    for i in range(len(poblacion)):
        probabilidad.append(round(poblacion[i]/suma,2))
    
    print("Probabilidad de seleccion: ", probabilidad)

    prob_acumulada = []

    for i in range(len(probabilidad)):
        if i == 0:
            prob_acumulada.append(probabilidad[i])
        else:
            prob_acumulada.append(round(probabilidad[i-1] + probabilidad[i],2))

    print("Probabilidad acumulada: ", prob_acumulada)

    T = 0

    for i in range(len(prob_acumulada)):
        T = T + prob_acumulada[i]

    T = round(T,2)

    print("T: ",T)


    padres_ruleta = []

    # for i in range(len(poblacion)):
    #     r = random.uniform(0,T)
    #     print("r: ",r)
        
    #     for i in range(len(prob_acumulada)):
    #         if prob_acumulada[i] > r:
    #             padres_ruleta.append(prob_acumulada[i])
    #             break 

    while len(padres_ruleta) != len(probabilidad):
        r = random.uniform(0,T)
        indice = random.randint(0,len(probabilidad)-1)

        if probabilidad[indice] > r:
            padres_ruleta.append(probabilidad[indice])
    
        
    print("Padres seleccionados por método ruleta \n",padres_ruleta)


    padres_estocasticos = []
    r_2 = 0.1
    i=0

    while i < len(probabilidad):
        if probabilidad[i] > r_2:
            padres_estocasticos.append(probabilidad[i])
        i = i + 1 


    print("Padres seleccionados por método estocástico \n",padres_estocasticos)

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
    for i in range(num_generacion):
        
        Generar_poblacion(num_poblacion,num_alelos,opc)
     

    


