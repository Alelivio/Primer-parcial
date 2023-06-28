'''Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales,
indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6). '''

#pedimos al usuario el ingreso de las 3 notas necesarias
n1 = float(input("ingrese la primer nota del alumno:"))
n2 = float(input("ingrese la segunda nota del alumno:"))
n3 = float(input("ingrese la tercer nota del alumno:"))
#calculamos el promedio de las notas

promedio = n1+n2+n3 /3
  

#verificamos si el usuario aprueba o debe recursar la materia
if promedio >=6: 
    print("su promedio es:",promedio,"felicidades, usted aprobo la materia")

else:
    print("tu promedio es:",promedio,"tienes que recursar la materia")
    
