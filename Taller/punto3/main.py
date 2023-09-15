'''
    3. Escribir un programa que permita visualizar el triángulo de Pascal. 
    En el triangulo de Pascal, cada número es la suma de los dos números situados encima de el. 
    Este problema se debe resolver utilizando un array de una sola dimensión. 
'''

def main():
    
    def suma_consecutiva(n:int):
        # suma los primeros n-numeros
        return int((n * ( n + 1))/2)
    
    
    def cal_num_triangulo_pascal(nivel:int , numeros:list) -> int:
        if len(numeros) < 3:
            return 1
        
        if len(numeros) % suma_consecutiva(nivel - 1) == 0 or len(numeros) % suma_consecutiva(nivel) == suma_consecutiva(nivel) - 1:
            return 1
        
        return numeros[ len(numeros) - nivel] + numeros[len(numeros) - (nivel - 1) ]
    
    # Imprime los numeros en piramide
    def imprimir_numeros(nivel,numeros):
        index = 0
        for i in range(nivel + 1):
            salida = ''
            for f in range( nivel - i):
                salida += ' '

            for j in range(i):
                salida +=str(numeros[index]) + " "
                index += 1
            print(salida)

    # ARRAY DE UNA SOLA DIMENSION
    numeros = [] 

    def triagulo_pascal(n:int):
        
        for i in range(n + 1):
            for j in range(i):
                numeros.append( cal_num_triangulo_pascal(i,numeros) )
        
        imprimir_numeros(n,numeros)
                
    
    triagulo_pascal(10)   


if __name__ == "__main__":
    main()