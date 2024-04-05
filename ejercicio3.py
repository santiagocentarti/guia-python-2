# Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2, en caso contrario elevar el resultado al cubo.
# santiago centarti
# Aplicaciones informaticas

num1= int(input("Ingrese numero 1:"))
num2= int(input("Ingrese numero 2:"))
num3= int(input("Ingrese numero 3:"))

suma = num1 + num2 + num3

if suma > 10:
     resultado = suma / 2
else:
     resultado = suma **3

print("El resulatado es: ",resultado)