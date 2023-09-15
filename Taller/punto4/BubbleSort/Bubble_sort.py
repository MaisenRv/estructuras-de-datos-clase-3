
class Bubble_sort:

    @staticmethod #Metodo estatico
    def ordenar(numeros):
        tamano = len(numeros)

        for i in range(len(numeros)):
            for j in range(tamano):

                if (j + 1 < len(numeros) and numeros[j] > numeros[j + 1]):
                    aux = numeros[j]
                    numeros[j] = numeros[j + 1]
                    numeros[j + 1] = aux
                    
            tamano = tamano - 1
        
        for numero in numeros:
            print(numero)