from Individuo import Individuo
import math
import random

def funcion2(num):
    return abs((num-5)/(2+math.sin(num)))


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


if __name__ == '__main__':
    
    poblacion = []
    Ind1 = Individuo([1,0,0,1,1])
    Ind1.Generar_fenotipo()
    Ind2 = Individuo([0,1,1,1,0])
    Ind2.Generar_fenotipo()
    Ind3 = Individuo([1,1,0,1,1])
    Ind3.Generar_fenotipo()
    Ind4 = Individuo([0,1,1,1,1])
    Ind4.Generar_fenotipo()
    

    poblacion.append(Ind1)
    poblacion.append(Ind2)
    poblacion.append(Ind3)
    poblacion.append(Ind4)

    select = Seleccion_ruleta(poblacion)

    for ind in select:
        print(ind.genotipo, ind.apto_cruza)
    