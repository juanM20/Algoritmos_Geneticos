from Individuo import Individuo
from Funciones_math import *
import random

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


def Seleccion_ruleta(poblacion):
    
    seleccion = []
    Valores_esperados = []
    
    for ind in poblacion:
        ind.aptitud = funcion2(ind.fenotipo)    

    aptitudes = [ind.aptitud for ind in poblacion]
    sumatoria = sum(aptitudes)
    f = sumatoria / len(poblacion)
    
    for ind in poblacion:
        ind.prob = ind.aptitud / f
        Valores_esperados.append(ind.aptitud / f) 
    
    T = sum(Valores_esperados)

    while len(seleccion) < len(poblacion):
        r = random.uniform(0, T)
        suma = 0 
        for ind in poblacion:
            suma = suma + ind.prob
            if suma >= r:
                ind.apto_cruza = True
                seleccion.append(ind)
                break

    return seleccion
