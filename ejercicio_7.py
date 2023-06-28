"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de
horas, escribe un programa que calcule el descuento anual a realizarse, considerando:
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
d. El programa debe mostrar elsalario anual bruto, el monto anual de bonificaciones, el monto anual
a descontarse y las horas trabajadas en todo el año. """


#concultamos al usuario la cantidad de horas
horas= int(input("Ingrese la cantidad de horas trabajadas por mes: "))
meses = 12

#verificamos su sueldo y su bonificacion correspondiente segun la cantidad de horas trabajadas
if horas > 120:
    sueldo = 1500
    bon = 0.18
elif horas >= 80 and horas <= 120:
    sueldo = 1300
    bon = 0.15
else:
    sueldo = 1100
    bon = 0.13

#calculamos su sueldo mensual y anual
sueldomensual = horas* sueldo
sueldoanual = sueldomensual * meses
bon_anual = sueldoanual * bon

#verificamos el descuento que se realiza a su sueldo anual
if sueldoanual > 2000000:
    descuento = 0.05
elif sueldoanual >= 1000000 and sueldoanual <= 2000000:
    descuento = 0.03
else:
    descuento = 0.01

#descuento anual
descuento_anual = sueldoanual * descuento
#sueldo neto
sueldonetoanual = sueldoanual - descuento_anual

#mostramos por pantalla
print("Las trabajadas en todo el año son:", horas* meses,"horas")
print("el salario anual bruto es de:", sueldoanual)
print("EL monto anual de bonificaciones es:", bon_anual)
print("Su monto anual a descontarse es:",descuento_anual)
print("Salario anual neto: $", sueldonetoanual)

