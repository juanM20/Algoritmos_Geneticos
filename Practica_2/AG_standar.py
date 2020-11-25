from Individuo import *
from Funciones_seleccion import *
from Funciones_Cruza import *
from Funciones_Mutacion import *
from Funciones_math.py

def Generar_poblacion(num_poblacion,num_alelos,opc):

    cromosoma = []
    poblacion = []

    for i in range(1,(num_poblacion*num_alelos)+1):
        
        if i%num_alelos == 0:

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
    
    CRUZA = 0.80
    MUTACION = 0.20
    
    opc = int(input('''

            Selecciona la función (escribe número).

            1. f(x) = x^2
            2. f(X) = |(x-5)/2+sin(x)|
            3. f(x) = (e^x - e^-x)/x 
    '''))

    num_poblacion = 2
    num_generacion =  int(input("Ponga el numero de Generaciones \n"))
    num_alelos =  int(input("Ponga el tamaño de los alelos \n"))
    
    poblacion = []
    poblacion = Generar_poblacion(num_poblacion,num_alelos,opc)

    for i in range(num_generacion):
        
        seleccion_cruza = []
        seleccion_mutacion = []
        
        Hijos = []
        
        aleatorio_cruza = random.uniform(0,1)
        aleatorio_mutacion = random.uniform(0,1)
        
        if aleatorio_cruza <= CRUZA:
            
            seleccion_cruza = seleccion_1(poblacion)
            
            if seleccion_cruza[0].apto_cruza == False or seleccion_cruza[1].apto_cruza == False:
                print("No hay cruza en generacion: ", num_generacion)
            else:
                Hijos = Cruza_Punto(seleccion_cruza)
                
                if aleatorio_mutacion <= MUTACION:
                    
                    r = random.randint(0, 1)
                    opc = input('''
                                    1. Mutacion aleatoria
                                    2. Mutacion intercambio de bit
                                    Elige una opción: 
                                ''')
                    
                    if opc = 1:
                        mutacion_desplazamiento(Hijos[r])
                    else:
                        CMIntercambio(Hijos[r])
        
        else:
            Hijos = Cruza_Punto(poblacion)
                
                if aleatorio_mutacion <= MUTACION:
                    
                    r = random.randint(0, 1)
                    opc = input('''
                                    1. Mutacion aleatoria
                                    2. Mutacion intercambio de bit
                                    Elige una opción: 
                                ''')
                    
                    if opc = 1:
                        mutacion_desplazamiento(Hijos[r])
                    else:
                        CMIntercambio(Hijos[r])
        
        
        poblacion = Hijos.copy()
        graficar(poblacion)
            
            
                
                   
                    
        
            
            
        
        
        
        
        
        
        





     

    


