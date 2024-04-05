# Crear un programa que permita calcular los impuestos que debe pagar un auto, conociendo su modelo (año de fabricación) y tipo (P: Particular/T: Taxi/R: Remisse). Para calcular los impuestos, tener en cuenta que: Los autos particulares de menos de 10 años de antigüedad pagan $2000, entre 10 y 20 años pagan $1500 y no pagan impuestos los que tienen más de 20 años. Los taxis pagan impuestos como auto particular, más $1500 por la licencia de taxi. Los remisses pagan $1000 por cada año de antigüedad de su vehículo.
# santiago centarti
# Aplicaciones informaticas

modelo=int(input("Ingrese hace cuantos años tiene el auto: "))

tipo=input("Ingrese que tipo de vehiculo: P: Particular / T: Taxi / R: Remis: ")

if tipo=="p" or tipo=="t":
    if modelo<10:
        impuesto=2000
    elif modelo>=10 and modelo<=20:
        impuesto=1500
    else:
        impuesto=0
    if tipo=="t":
        impuesto+=1500
elif tipo=="r":
    impuesto=modelo*1000
else:
    print("El tipo que ingreso es invalido")
print(f"El impuesto a pagar por su vehiculo es de ${impuesto}")