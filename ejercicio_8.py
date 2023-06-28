"""Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas."""

#le dámos a la variable un valor y un limite para que el usuario pueda ingresar
persona = 1
while persona <= 5:
    print("la persona numero",persona)
    persona+=1
#solicitamos al usuario los datos
    nombre = input("Ingresa el nombre:")
    apellido = input("Ingresa el apellido:")
    edad = input("Ingrese la edad:")
    
#mostramos por pantalla el nombre,apellido y edad
    print("Tu nombre completo es:",nombre,apellido)
    print("Tu edad es:", edad,"años")
    

