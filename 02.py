# 2. Escribir un programa que calcule el área de un rectángulo:
# lado1 = 3 lado2 = 4 área del rectángulo= lado1 * lado2



""" lado1 = 3
lado2 = 4 """


lado1 = int(input("Escribe el lado 1\n"))
lado2 = int(input("Escribe el lado 2\n"))





def area(p1, p2):
    resultado = p1 * p2
    print(f"Area del rectangulo\n {resultado}")

area(lado1, lado2)