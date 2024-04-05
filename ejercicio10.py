peso = float(input("ingrese su peso en Kg: "))
altura = float(input("ingrese altura en metros: "))

imc=peso/(altura**2)

if imc > 30:
    print("se encuentra en un grado de obesidad")
elif imc > 24.5 and imc < 29.9:
    print("se encuentra en sobrepeso")
elif imc > 18.5 and imc < 24.9:
    print("se encuentra en un peso saludable")
elif imc < 18.5:
    print("se encuentra en un peso insuficiente")

print("su peso ideal seria: ",21.7*(altura**2))