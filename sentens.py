print ("EJERCICIO 1")
asteroide = input ("Digitar la velocidad del asteroide: ")
if int(asteroide) > 25:
    print("¡EMERGENCIA!, ¡Un asteroide se acerca!")
else:
    print ("No hay peligro ;)")



print ("EJERCICIO 2")
asteroide = input ("Digitar la velocidad del asteroide: ")
if int(asteroide) > 20:
    print("¡CUIDADO!, un rayo de luz")
elif int(asteroide) == 20:
    print("¡CUIDADO!, un rayo de luz")
else:
    print ("No hay peligro ;)")



print ("EJERCICIO 3")
dimen_asteroide = input ("Digitar la dimensión del asteroide: ")
velocidad_asteroide = input ("Digitar la velocidad del asteroide: ")
if int(dimen_asteroide) > 25 and int(velocidad_asteroide) > 25 :
    print("¡PELIGRO!")
elif int(dimen_asteroide) < 25 : 
    print("Sin peligro")
elif int(velocidad_asteroide) >= 20 :
    print("¡OJO!, rayo de luz")
else :
    print ("Sin peligro")
    
