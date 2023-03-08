print('*' * 10)

""" name = "'Edgar'"# String
age = 24 # Number
size = 1.65 # Float
teacher = False # Boolean
student = 1 # Boolean, too """

""" print(f"Yo soy, {name}, soy estudiante en Campus")
print(f"nombre => {name}")
print('edad => ', age)
print('altura => ', size)
print('Es profesor? => ', teacher)
print('Es estudiante? => ', student) """

# Un input es una entrada, un print es un Output, una salida de datos.
name = input("\tEscribe tu nombre aqui =>  ")  # Esto tabula. 
age = int(input("Escribe tu edad aqui =>\n")) # Esto hace un salto de linea.
size = float(input("Escribe tu altura aqui =>\n")) 
teacher = bool(input("Es acaso profesor? =>\n\t1.Yes\n\t0.No\n")) 
print(f"nombre => {name}")
print('edad => ', age)

# Aqui puedo imprimir el tipo de mi variable.
print(type(name))
print(f"Dato: {age}, tipo: {type(age)}")
print(type(size))
print(type(teacher))






'''
True
1 => infinito, -1 => -infinito 
" " - "a"
[] () {}

False
0
""
None
'''

# Estructuras de Datos