"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto
(bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13."""
#consultamos al usuario la cantidad de horas trabajadas este mes
horas = int(input("ingrese la cantidad de horas trabajadas:"))
#mostramos por pantalla las horas
print("la cantidad de horas que trabajo en el mes es de:",horas,"horas")

#calculamos su sueldo bruto, bonificacion y sueldo neto
if horas > 120:
    sueldo= 1500
    pago= sueldo*horas
    boni =pago*0.18
    neto=pago+boni
  
elif horas >= 80:
    sueldo= 1300
    pago= sueldo*horas
    boni =pago*0.15
    neto=pago+boni
   
else:
     sueldo = 1100
     pago= sueldo*horas
     boni =pago*0.13
     neto=pago+boni

#lo mostramos por pantalla
print("Su sueldo es de:",pago)
print("la bonificacion es de:",boni)
print("Su sueldo neto es de:",neto)
    