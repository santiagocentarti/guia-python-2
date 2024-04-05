# Desarrollar un programa que permita al usuario jugar contra la computadora el clásico “Piedra, papel o Tijera” y determine cuál de ellos es el ganador. Las reglas son:* La piedra aplasta (o rompe) la Tijera. (Gana la piedra). * La Tijera corta el papel. (Gana la Tijera). El papel envuelve la piedra. (Gana el papel) * Si los dos jugadores eligen el mismo elemento, empatan.
# santiago centarti
# Aplicaciones informaticas
import random

opciones=["piedra","papel","tijera"]

jugador=input("Elige piedra, papel o tijera: ")

maquina = random.choice(opciones)

print("Opcion de la maquina: ",maquina)

if maquina==jugador:
      print("Empate")
elif jugador=="piedra":
     if maquina=="tijera":
         print("Perdiste")
     else:
        print("perdiste")
elif jugador=="papel":
    if maquina=="piedra":
        print("ganaste")
    else:
         print("ganaste")
elif jugador=="tijera":
    if maquina=="papel":
          print("ganaste")
    else:
         print("ganaste")

