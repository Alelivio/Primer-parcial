"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre
por pantalla el resultado, considerando lo siguiente:
a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100."""

#consultamos al usuario la cantidad de horas trabajadas este mes
horas = int(input("ingrese la cantidad de horas trabajadas:"))

#mostramos la cantidad de horas trabajadas en el mes
print("la cantidad de horas que trabajo en el mes es de:",horas,"horas")


#calculamos su sueldo segun las horas trabajadas
if horas > 120:
    sueldo= 1500
    pago= sueldo*horas
    
elif horas >= 80:
    sueldo= 1300
    pago= sueldo*horas
   
else:
     sueldo = 1100
     pago= sueldo*horas
     
#lo mostramos por pantalla
print("Su sueldo es de:",pago)
      


