from Individuo import Individuo
import math
import random

def funcion2(num):
    return abs((num-5)/(2+math.sin(num)))


def seleccion_1(poblacion):

    seleccion = []
    rango_prob = []
    sum = 0

    for ind in poblacion:
        ind.aptitud = funcion2(ind.fenotipo)
        sum = sum + ind.aptitud

    for ind in poblacion:
        ind.prob = ind.aptitud / sum

    rango_prob.append([0,poblacion[0].prob])
    rango_prob.append([poblacion[0].prob, poblacion[0].prob + poblacion[1].prob])

    
    for i in range(len(poblacion)):
        va = random.uniform(0,1)

        if va > rango_prob[i][0] and va < rango_prob[i][1]:
            poblacion[i].apto_cruza = True
            seleccion.append(poblacion[i])
        else:
            poblacion[i].apto_cruza = False
            seleccion.append(poblacion[i])


    return seleccion



if __name__ == '__main__':
    
    poblacion = []
    Ind1 = Individuo([1,0,0,1,1])
    Ind1.Generar_fenotipo()
    Ind2 = Individuo([0,1,1,1,0])
    Ind2.Generar_fenotipo()
    

    poblacion.append(Ind1)
    poblacion.append(Ind2)

    select = seleccion_1(poblacion)

    for i in select:
        print(i.genotipo, i.apto_cruza)

   



    