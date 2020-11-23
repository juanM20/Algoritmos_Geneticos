from Individuo import Individuo
import random

def mutacion_desplazamiento(individuo):
    random.shuffle(individuo.genotipo)




if __name__ == '__main__':
    
    individuo = Individuo([1,0,0,1,1])

    print(individuo.genotipo)

    mutacion_desplazamiento(individuo)
    individuo.Generar_fenotipo()

    print(individuo.genotipo)
