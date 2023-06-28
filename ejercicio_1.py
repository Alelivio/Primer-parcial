'''Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el
año de nacimiento.'''

#consultamos año de nacimiento
nacimiento = int(input("Ingrese su año de nacimiento: "))

#consultamos año actual
año = int(input("ingrese el año actual: "))

#calculamos la edad restando el año de nacimiento al año actual
edad = año - nacimiento

#mostramos por pantalla
print ("tu edad actual es: ",edad)


