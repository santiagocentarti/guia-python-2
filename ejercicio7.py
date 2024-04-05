# Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes a diferentes momentos de un día y determinar cuál es el promedio de las temperaturas y si existe alguna temperatura que sea mayor al promedio.
# santiago centarti
# Aplicaciones informaticas

temp1 = float(input("Ingrese la temperatura de la mañana del día: "))
temp2 = float(input("Ingrese la temperatura de la tarde del día: "))
temp3 = float(input("Ingrese la temperatura de la noche del día: "))

promtemp = (temp1 + temp2 + temp3) / 3

if temp1 > promtemp:
    print(f"La temperatura {temp1} es mayor que el promedio.")
if temp2 > promtemp:
    print(f"La temperatura {temp2} es mayor que el promedio.")
if temp3 > promtemp:
    print(f"La temperatura {temp3} es mayor que el promedio.")

print(f"El promedio de las temperaturas es: {promtemp}")