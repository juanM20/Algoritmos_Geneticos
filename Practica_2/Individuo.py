class Individuo:

    def __init__(self, genotipo = [], fenotipo=0,aptitud = 0 ,apto_cruza = False, prob = 0.0):
        self.genotipo = genotipo
        self.fenotipo = fenotipo
        self.aptitud = aptitud
        self.apto_cruza = apto_cruza
        self.prob = prob


    def Generar_fenotipo(self):

        str_bin = "".join(map(str, self.genotipo))
        self.fenotipo = int(str_bin,2)




        
