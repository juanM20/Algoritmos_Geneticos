from Individuo import Individuo
from Funciones_seleccion import *
from Funciones_Cruza import *
from Funciones_Mutacion import *
from Funciones_math import *


def Generar_poblacion(num_poblacion, num_alelos, opc):

    cromosoma = []
    poblacion = []

    for i in range(1, (num_poblacion*num_alelos)+1):

        if i % num_alelos == 0:

            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)

            ind = Individuo(cromosoma)
            ind.Generar_fenotipo()
            ind.Generar_Aptitud(opc)
            poblacion.append(ind)
            cromosoma = []
        else:
            if random.random() > 0.5:
                cromosoma.append(1)
            else:
                cromosoma.append(0)

    return poblacion


if __name__ == "__main__":

    opc1 = int(input('''

            Selecciona la función (escribe número).

            1. f(x) = x^2
            2. f(X) = |(x-5)/2+sin(x)|
            3. f(x) = (e^x - e^-x)
    '''))

    num_poblacion = 2
    num_generacion = int(input("Ponga el numero de Generaciones \n"))
    num_alelos = int(input("Ponga el tamaño de los alelos \n"))

    poblacion = []
    poblacion = Generar_poblacion(num_poblacion, num_alelos, opc1)
    
    for ind in poblacion:
        print(ind.genotipo)
        print(ind.fenotipo)

    for i in range(num_generacion):

        print(f'''
              
              -------------------
                GENERACION {i}
              -------------------
              
              ''')
          
        seleccion_cruza = []
        Hijos = []
        
        seleccion_cruza = seleccion_1(poblacion)

        if seleccion_cruza[0].apto_cruza == True or seleccion_cruza[1].apto_cruza == True:

            Hijos = Cruza_Punto(poblacion)

            print("Hijos de generacion: ",i)
            for ind in Hijos:
                print(ind.genotipo)
                print(ind.fenotipo)

            r = random.randint(0, 1)

            opc = int(input('''
                            1. Mutacion aleatoria
                            2. Mutacion intercambio de bit
                            Elige una opción:
                    '''))
            if opc == 1:
                mutacion_desplazamiento(seleccion_cruza[r])
            else:
                CMintercambio(seleccion_cruza[r])

            poblacion = seleccion_cruza.copy()
        
        else: 
            r = random.randint(0, 1)

            opc = int(input('''
                            1. Mutacion aleatoria
                            2. Mutacion intercambio de bit
                            Elige una opción:
                    '''))
            if opc == 1:
                mutacion_desplazamiento(seleccion_cruza[r])
            else:
                CMintercambio(seleccion_cruza[r])

            poblacion = seleccion_cruza.copy()

            
        print("Nueva poblacion: ")
        for ind in poblacion:
            ind.Generar_Aptitud(opc1)
            print(ind.genotipo)
            print(ind.fenotipo)

        graficar(poblacion)
