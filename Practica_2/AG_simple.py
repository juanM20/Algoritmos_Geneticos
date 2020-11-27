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

    CRUZA = 0.8
    MUTACION = 1-CRUZA
    
    opc = int(input('''

            Selecciona la función (escribe número).

            1. f(x) = x^2
            2. f(X) = |(x-5)/2+sin(x)|
            3. f(x) = (e^x - e^-x) 
    '''))

    num_poblacion = int(input("Número de población \n"))
    num_generacion =  int(input("Numero de Generaciones \n"))
    num_alelos =  int(input("Tamaño de los alelos \n"))
    
    poblacion = []
    poblacion = Generar_poblacion(num_poblacion,num_alelos,opc)
    
    for ind in poblacion:
        print(ind.genotipo, ind.fenotipo, ind.aptitud)
        
    
    for i in range(num_generacion):
        
        print(f'''
              
              -------------------
                GENERACION {i+1}
              -------------------
              
              ''')
          
        seleccion = []
        Hijos = []
        
        seleccion = Seleccion_ruleta(poblacion)
        
        print("Individuos seleccionados: ")
        for ind in seleccion:
            print(ind.genotipo, ind.fenotipo, ind.aptitud)
            
        seleccion_cruza = seleccion[:int(len(seleccion) * CRUZA)].copy()
        seleccion_mutacion = seleccion[int(len(seleccion) * CRUZA):].copy()
        
        
        opc_cruza = int(input('''

                            Selecciona el tipo de cruza:

                            1. Cruza por un punto.
                            2. Cruza por dos puntos.

                        '''))

        if opc_cruza == 1:

            Hijos = Cruza_Punto(seleccion_cruza)

            opc_mutacion = int(input('''

                            Selecciona el tipo de mutacion:

                            1. Mutación aleatoria.
                            2. Mutación por intercambio de bit.
                            3. Mutación por Inserción.

                            '''))

            if opc_mutacion == 1:

                for ind in seleccion_mutacion:
                    mutacion_desplazamiento(ind)

            elif opc_mutacion == 2:

                for ind in seleccion_mutacion:
                    CMintercambio(ind)

            elif opc_mutacion == 3:

                for ind in seleccion_mutacion:
                    mutacionInsercion(ind)

        elif opc_cruza == 2:

            Hijos = Cruza_Punto(seleccion_cruza)

            opc_mutacion = int(input('''
                            
                            Selecciona el tipo de mutacion:
                            
                            1. Mutación aleatoria.
                            2. Mutación por intercambio de bit.
                            3. Mutación por Inserción.    
                                     
                            '''))

            if opc_mutacion == 1:

                for ind in seleccion_mutacion:
                    mutacion_desplazamiento(ind)

            elif opc_mutacion == 2:

                for ind in seleccion_mutacion:
                    CMintercambio(ind)

            elif opc_mutacion == 3:

                for ind in seleccion_mutacion:
                    mutacionInsercion(ind)
        
        
        print(f"Hijos de la generacion {i+1}")
        for ind in Hijos:
            ind.Generar_Aptitud(opc)
            print(ind.genotipo, ind.fenotipo, ind.aptitud)

        print(f"Mutantes de la generacion {i+1}")
        for ind in seleccion_mutacion:
            print(ind.genotipo, ind.fenotipo, ind.aptitud)

        Hijos.extend(seleccion_mutacion)
        poblacion = Hijos.copy()
        
        graficar(poblacion)
        
        random.shuffle(poblacion)

     

    


