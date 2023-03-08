""" 9. Escribir un algoritmo que permita obtener las raíces reales de la ecuación de
segundo grado: A * x2 +
b * x + c, siendo X un valor constante de 2. """


# Copy from Chatgpt 

import math

# Definir los coeficientes de la ecuación
a = 1
b = 2
c = 1

# Calcular el discriminante
discriminante = b**2 - 4*a*c

# Verificar si hay raíces reales
if discriminante < 0:
    print("La ecuación no tiene raíces reales.")
else:
    # Calcular las raíces
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    # Imprimir las raíces
    print("Las raíces de la ecuación son:")
    print("x1 = ", x1)
    print("x2 = ", x2)

