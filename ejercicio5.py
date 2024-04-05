# Ingresar por teclado las edades de 3 participantes de un concurso. Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado
# santiago centarti
# Aplicaciones informaticas

edad1 = int(input("Ingrese la edad del participante 1: "))
edad2 = int(input("Ingrese la edad del participante 2: "))
edad3 = int(input("Ingrese la edad del participante 3: "))

edadmin = int(input("Ingrese la edad mínima requerida para el concurso: "))

if edad1 >= edadmin and edad2 >= edadmin and edad3 >= edadmin:
    print("Todos los participantes cumplen con la edad mínima requerida.")
else:
    print("Al menos uno de los participantes no cumple con la edad mínima requerida.")