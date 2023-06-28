"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no
hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas."""

#variables para almacenar las sumas y el total.
personas = 0
suma = 0
#bucle que reliza el ingreso de las edades
while True: 
    edad = input("Ingrese la edad o 'n' para finalizar: ")
#verificacion de si quiere seguir ingresando o no.
    if edad == "n":
      break
    
#convierte la edad en entero y los suma
    suma += int(edad)
#incrementa el contador sumando 1    
    personas += 1

#verifica el ingreso de las personas
if personas > 0:
#calcula el promedio de las edades
    prom = suma / personas

#muestra por pantalla los resultados
    print("Promedio de edades:", prom)
    print("Total de personas ingresadas:", personas)

#muestra que no se ingresaron edades
else:
    print("No se ingresaron edades.")