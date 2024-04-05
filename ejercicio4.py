# Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2-representa Nocturno) y la cantidad de horas trabajadas. La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 400.60 pesos la hora, si lo hace en el turno diurno cobra 350.50 pesos la hora. 
# santiago centarti
# Aplicaciones informaticas

codigoTurno = int(input("ingrese el codigo de turno 1- representa Diurno y 2-representa Nocturno: "))
cantidadHoras = int(input("ingrese la cantidad de horas trabajadas: "))

if codigoTurno == 1:
    sueldo = 350.50 * cantidadHoras
elif codigoTurno == 2:
   sueldo = 400.60 * cantidadHoras
else:
    print("ingrese un numero valido")

print("su sueldo correspondidio es de: ", sueldo)