"""
Nombre del archivo: AreaPython.py
Descripción: Programa para cálcular el área de figuras geométricas
Autor: Luis Fernando Gálvez Huez
Fecha: 15/10/2026
"""
import sys
import math

while True:

    print("Calculador de Área")

    print("0) Salir")
    print("1) Triángulo")
    print("2) Círculo")
    print("3) Rectángulo")

    a = int(input("¿Qué área desea cálcular? -> "))
    
    if a == 0:
       
         print("Proceso finalizado")
         break

    elif a == 1:
         
        base_triangulo = float(input("Ingrese la base del triángulo = "))
        altura_triangulo = float(input("Ingrese la altura del triángulo = "))
        area = float(base_triangulo * altura_triangulo) / 2
        print("El área del triángulo es:")
        print(area)
        True

    elif a == 2:
        
        radio_circulo = float(input("Ingrese el radio del círculo = "))
        area = float(math.pi) * (radio_circulo) ** 2
        print("El área del círculo es:")
        print(area)
        
    elif a == 3:
        base_rectangulo = float(input("Ingrese la base del rectángulo = "))
        altura_rectangulo = float(input("Ingrese la altura del rectángulo = "))
        area = float(base_rectangulo * altura_rectangulo)
        print("El área del rectángulo es:")
        print(area)

    else:   
        print("Error, selecciona un número del 0 al 3",file=sys.stderr)
