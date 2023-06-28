"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de
personas ingresada por el usuario."""

#consultamos al usuario la cantidad de personas que quiere ingresar los datos
cantidad = int(input("ingrese un numero de personas:"))

#variable para almacenar cantidad
personas = 1

#el bucle se va a ejecutar mientras la variable persona sea mayor a la cantidad de personas0
while personas <= cantidad:
    print("Persona numero",personas)
    personas+=1


#consultamos al usuarios los datos
    nombre = input("Ingresa el nombre:")
    apellido = input("Ingresa el apellido:")
    edad = input("Ingrese la edad:")

#mostramos por pantalla los datos.
    print("Tu nombre completo es:",nombre,apellido)
    print("Tu edad es:", edad,"años")
