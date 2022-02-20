
from datetime import date
date.today()

print("Bienvenido al programa")
name = input("Introduzca su nombre ")
print("Saludos: " + name)
print("La fecha de hoy es: " + str(date.today()))

print("Conversión de Parsec a Lightyears")
parsec = input ("Introduzca el valor de Parsec: ")
lightyears = 3.26156 
multi = float (parsec) * float(lightyears)
print (str(parsec) + " parsec son: " + str(multi) + " lightyears.")