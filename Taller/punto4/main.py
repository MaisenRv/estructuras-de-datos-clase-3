'''
    4.1 Opere la siguiente ecuación NL= (Latitud *0333)/(Latitud+0.1)
    4.2 Opere. NLng= (Longitud *0555)/(Longitud+0.3)
    4.3 De los puntos 4.1 y 4.2 ordene los datos de NL y ND 
        Datos Latitud y longitud: 
        (40.7128, -74.0060), 
        (34.0522, -118.2437), 
        (41.8781, -87.6298), 
        (37.7749, -122.4194), 
        (48.8566, 2.3522), 
        (51.5074, -0.1278), 
        (35.6895, 139.6917), 
        (55.7558, 37.6176), 
        (25.276987, 55.2962), 
        (-33.8688, 151.2093) 
'''

from BubbleSort.Bubble_sort import Bubble_sort

def calcular_NL(latitud):
    return (latitud * 0.333)/(latitud + 0.1)

def calcular_ND(longitud):
    return (longitud * 0.555)/(longitud + 0.3)


def main():
    #Latitud y Longitud
    datos = [
        [40.7128, -74.0060],
        [34.0522, -118.2437],
        [41.8781, -87.6298],
        [37.7749, -122.4194],
        [48.8566, 2.3522],
        [51.5074, -0.1278],
        [35.6895, 139.6917],
        [55.7558, 37.6176],
        [25.276987, 55.2962],
        [-33.8688, 151.2093],
    ]

    datos_NL = []
    datos_ND = []
    for dato in datos:
        datos_NL.append(calcular_NL(dato[0]))
        datos_ND.append(calcular_ND(dato[1]))

    bubble_sort = Bubble_sort()
    print('------------ datos NL ordenados ------------')
    bubble_sort.ordenar(datos_NL)
    print('------------ datos ND ordenados ------------')
    bubble_sort.ordenar(datos_ND)
    

if __name__ == '__main__':
    main()