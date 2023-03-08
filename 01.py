# 1. Escribir un programa que sume, reste, multiplique y divida dos números

num1 = int(input("Escribe el primer numero\n"))
num2 = int(input("Escribe el segundo numero\n"))


def oper(p1, p2):

    print(f"Suma => {p1 + p2}")
    print(f"Resta => {p1 - p2}")
    print(f"Multiplicacion => {p1 * p2}")
    print(f"Division => {p1 / p2}")


print("Resultados\n   ")
oper(num1, num2)