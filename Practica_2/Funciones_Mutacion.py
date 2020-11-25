from Individuo import Individuo
import random
import numpy as np

def mutacion_desplazamiento(individuo):
    random.shuffle(individuo.genotipo)



def CMintercambio(p1):
    x = random.randint(0, (len(p1.genotipo)-1))
    y = random.randint(0, (len(p1.genotipo)-1))
    mp1 = [] 
    while x == y:
        x = random.randint(0, (len(p1.genotipo)-1))
        y = random.randint(0, (len(p1.genotipo)-1))
    else:
        a = p1.genotipo[x]
        b = p1.genotipo[y]
        p1.genotipo[y] = a
        p1.genotipo[x] = b
         
         
def mutacionInsercion(ind1):
    while True:
        inicio = random.randint(0, len(ind1.genotipo) - 1)
        fin = random.randint(0, len(ind1.genotipo) - 1)
        if (inicio!=fin):
            break
    diferencia = max(inicio, fin) - min(inicio, fin)
    if(inicio < fin):
        if(diferencia == 1):
            aux = ind1.genotipo[inicio]
            ind1.genotipo[inicio] = ind1.genotipo[fin]
            ind1.genotipo[fin] = aux
        else:
            aux = ind1.genotipo[inicio]
            for i in range(inicio, fin+1):
                ind1.genotipo[i] = ind1.genotipo[i+1]
            ind1.genotipo[fin] = aux
    else:
        if(diferencia == 1):
            aux = ind1.genotipo[inicio]
            ind1.genotipo[inicio] = ind1.genotipo[fin]
            ind1.genotipo[fin] = aux
        else:
            aux = ind1.genotipo[inicio]
            for i in range(inicio, fin, -1):
                ind1.genotipo[i] = ind1.genotipo[i-1]
            ind1.genotipo[fin] = aux
