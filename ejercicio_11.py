"""Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
a. Si es número es par o impar.
b. Cuanto es la suma total de todos los números mostrados.
c. Cuanto es la suma total de todos los números pares mostrados.
d. Cuanto es la suma total de todos los números impares mostrados."""

#variables para almacenar las sumas
num= 1
suma= 0
pares= 0
impar= 0

#ealizamos una variable que hace que se realize un bucle 
while num <= 10:
    print("Número:", num)
    
    if num % 2 == 0:
        print("Es par")
        pares += num
    else:
        print("Es impar")
        impar += num

     #se realiza la suma total 
        suma+=num
    print("-")
    num+=1


#se muestra por pantalla los resultados 
print("la suma total es:",suma)
print("la suma de los numeros pares es:",pares)
print("la suma de los numeros impares es:",impar)


