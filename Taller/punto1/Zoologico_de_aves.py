from Tipo_ave import Tipo_ave

class Zoologico_de_aves:
    def __init__(self) -> None:
        self.aves = []

    def agregar(self,ave:Tipo_ave) -> None:
        self.aves.append(ave)
    
    # ---- Hace la funcion de Iterator de JAVA ----
    def __iter__(self):
        self.indice = 0
        return self
    
    def __next__(self):
        if self.indice < len(self.aves):
            ave = self.aves[self.indice]
            self.indice += 1
            return ave
        else:
            raise StopIteration
    # -----------------------------------------------
 
    

