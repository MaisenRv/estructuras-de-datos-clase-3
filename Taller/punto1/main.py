'''
    1. Crear una clase denominada TipoAve con 4 atributos. 
    Uno será de tipo String  (nombreTipoDeAve) y los otros tres serán de tipo int (numeroAves, numeroMachos, numeroHembras). 

    Crea una clase ZoologicoDeAves que implemente la interface Iterable. 
    Crea varios objetos de tipo TipoAve y añádelos a un objeto ZoologicoDeAves. 
    Utilizando un iterador, muestra los datos de los objetos presentes en el objeto ZoologicoDeAves.   

    Aunque habría muchas formas de llegar a este resultado,es obligatorio el uso de iterator  
    Por ejemplo  TipoAve = new TipoAve("Aguila", 35, 10, 25); sería un objeto de la clase TipoAve y 
    public TipoAve[] gruposDeAves sería el atributo de la clase ZoologicoDeAves con base al cual se realiza la iteración. 
'''


from Tipo_ave import Tipo_ave
from Zoologico_de_aves import Zoologico_de_aves

def main():
    zoo = Zoologico_de_aves()
    zoo.agregar(Tipo_ave("Flamenco",300,140,160))
    zoo.agregar(Tipo_ave("Ganso",200,120,80))
    zoo.agregar(Tipo_ave("Tucan",100,45,55))
    zoo.agregar(Tipo_ave("Condor",20,8,12))

    print('Aves en el zoologico')
    for i, ave in enumerate(zoo):
        print(f'{i + 1} Nombre del ave: {ave.nombre}')
        print(f'   - Numero de aves: {ave.numero_aves}')
        print(f'   - Numero de machos: {ave.numeros_machos}')
        print(f'   - Numero de hembras: {ave.numeros_hembras}')
    


if __name__ == "__main__":
    main()