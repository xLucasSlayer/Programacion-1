# Nombre del archivo: Palindromo.py
# Descripción: Programa detector de palindromos
# Autor: Luis Fernando Gálvez Huez
# Fecha: 22/10/2026

cadena =  str(input("Ingresa una frase -> "))
cadena = cadena.lower()

cadena = cadena.replace("á","a")
cadena = cadena.replace("é","e")
cadena = cadena.replace("í","i")
cadena = cadena.replace("ó","o")
cadena = cadena.replace("ú","u")
cadena = cadena.replace("ü","u")
cadena = cadena.replace(",","")
cadena = cadena.replace(" ","")
cadena = cadena.replace("-","")
cadena = cadena.replace("'","")
cadena = cadena.replace("¿","")
cadena = cadena.replace("?","")
cadena = cadena.replace("!","")
cadena = cadena.replace("¡","")
cadena = cadena.replace(";","")
cadena = cadena.replace(":","")
cadena = cadena.replace(".","")

invertida = ""
for i in range(len(cadena) -1,-1,-1):
    invertida = invertida + cadena[i]
    
if cadena == invertida:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
