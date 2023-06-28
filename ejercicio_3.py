'''Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El
programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).'''


#consultamos al usuario el valor del dolar actualmente y cuanto quiere cambiar a pesos argentinos
dolar = int(input("Ingrese el valor del dolar actualmente:"))
cambio = int(input("ingrese cuantos dolares quiere cambiar:"))

#mostramos por pantalla y realizamos su calculo
print("el valor del dolar es actualmente de ",dolar,"pesos")
print("su cambio de dolares a pesos es de:",cambio*dolar)
