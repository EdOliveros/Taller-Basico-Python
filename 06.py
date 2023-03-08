""" 6. Escribir un programa que calcule la velocidad de un proyectil que recorre 2 Km en
5 minutos. Expresar
el resultado en metros/segundo. Velocidad = espacio/tiempo. """

""" distancia_km = 2
tiempo_minutos = 5 """

distancia_km = int(input("Escribe la distancia en Km\n"))
tiempo_minutos = int(input("Escribe el tiempo en minutos\n"))


def velocidad(tiempo, distancia):
    distancia = distancia * 1000
    tiempo = tiempo * 60

    print(f"La velocidad es de:\n {distancia / tiempo} m/s") 

velocidad(tiempo_minutos, distancia_km)