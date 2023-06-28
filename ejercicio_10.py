"""Escribe un programa que calcule el promedio general de una clase"""

#consultamos al usuario la cantidad de alumnos
alumnos = int(input("ingrese la cantidad de alumnos:"))

#variables para almacenar sumas
n1 = 0
suma=0
#consultamos la nota del estudiante
while n1< alumnos:
    nota = float(input("ingrese la nota del alumno:"))
    n1+=1
    suma+=nota
#calculamos su promedio dividiendo la suma de las notas por los alumnos
promedio= suma/alumnos

#mostramos por pantalla es resultado
print("el promedio de la clase es de:",promedio)

          