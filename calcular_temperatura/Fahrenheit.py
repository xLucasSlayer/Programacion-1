# Nombre del archivo: Fahrenheit.py
# Descripción: Programa convertidor de temperaturas (Celsius/Fahrenheit)
# Autor: Luis Fernando Gálvez Huez
# Fecha: 07/10/2026

import sys

print("Convertidor de temperatura")

print("1) Celsius° -> Fahrenheit°")
print("2) Fahrenheit° -> Celsius°")
print ("¿Que desea convertir?")

a = int(input())

if a == 1:

    temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius(°C)= "))
    temperatura_fahrenheit = float((temperatura_celsius * 1.8) + 32)

    print("Temperatura convertida de Celsius(°C) a Fahrenheit(°F)")
    print(f"{temperatura_celsius}°C => {temperatura_fahrenheit}°F")

elif a == 2:
    
    temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit(°F)= "))
    temperatura_celsius = float((temperatura_fahrenheit - 32) / 1.8)

    print("Temperatura convertida de Fahrenheit(°F) a Celsius(°C)")
    print(f"{temperatura_fahrenheit}°F => {temperatura_celsius}°C")
    
else:
       print("Error, selecciona un número del 1 al 2",file=sys.stderr)