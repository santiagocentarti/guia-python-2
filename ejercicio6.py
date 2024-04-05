# Una persona compra un billete de Quiniela y apuesta 3 números a la cabeza. En el caso que acierte alguno de ellos ganará 70 veces el monto de lo apostado. Crear un programa que genere un número al azar del 0 al 99 y que permita apostar los tres valores. En el caso que se acierte indicar el monto a cobrar.
# santiago centarti
# Aplicaciones informaticas

import random

quini1= random.randint(1,99)
quini2= random.randint(1,99)
quini3= random.randint(1,99)
apuesta = int(input("ingrese cuanto quiere apostar: "))

num1 = int(input("ingrese un numero para apostar entre 1 y 99: "))
num2 = int(input("ingrese otro numero para apostar entre 1 y 99: "))
num3 = int(input("ingrese el tercer numero para apostar entre 1 y 99: "))

if num1 == quini1 or num2 == quini2 or num3 == quini3:
    if num2 == quini1 or num2 == quini2 or num2 == quini3:
        if num3 == quini1 or num3 == quini2 or num3 == quini3:
            print("usted ha ganado: ", apuesta*70)
else:
    print("usted perdio")
