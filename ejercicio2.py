# Ingresar un número entero e indicar si es positivo o negativo. En el caso que sea un cero, indicar tal situación.
# santiago centarti
# Aplicaciones informaticas

num1 = int(input("Ingrese un numero para saber si es negativo, positivo o 0"))
if num1 > 0:
    print("El numero es positvo")
elif num1 < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")