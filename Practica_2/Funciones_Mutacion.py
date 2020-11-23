from Individuo import Individuo
import random

def mutacion_desplazamiento(individuo):
    random.shuffle(individuo.genotipo)



def CMintercambio(p1):
    x = random.randint(0, (len(p1)-1))
    y = random.randint(0, (len(p1)-1))
    mp1 = [] 
    while x == y:
        x = random.randint(0, (len(p1)-1))
        y = random.randint(0, (len(p1)-1))
    else:
        a = p1[x]
        b = p1[y]
        p1[y] = a
        p1[x] = b
    return p1
         
            