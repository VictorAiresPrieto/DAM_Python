import os

tabla = 50

print("|"+"Ejercicio 1".center(tabla, "-")+"|")

num1 = 10
num2 = 20
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("Las operaciones se realizaran con: {} y {}\n"
      "La suma dara como resultado: {}\n"
      "La resta dara como resultado: {}\n"
      "La multiplicacion dara como resultado: {}\n"
      "La division dara como resultado: {}"
      .format(num1, num2, suma, resta, multiplicacion, division))

print("|" + "Ejercicio 2".center(50, "-")+"|")

num = 23
#num = int(input("Ingrese un numero: "))

print(num*num)

print("|" + "Ejercicio 3".center(50, "-")+"|")

if num%2 == 0:
      print("El numero es par")
else:
      print("El numero es senar")

print("|" + "Ejercicio 4".center(50, "-") + "|")
if num < 5:
      print("Suspendido")
elif 5 <= num < 6.5:
      print("Bien")
elif 6.5 <= num < 8.5:
      print("Notable")
elif 8.5 <= num <= 10:
      print("Excelente")
else:
      print("No es valido")

print("|" + "Ejercicio 5".center(50, "-")+"|")

caracoles_d = 100
caracoles_p = 10000

if caracoles_p > 10000 and caracoles_d < 200:
      print("Grado 8")
elif caracoles_p > 10000 and caracoles_d >= 200:
      print("Grado 7")
elif caracoles_p <= 10000 and caracoles_d < 200:
      print("Grado 6")
elif caracoles_p <= 10000 and caracoles_d >= 200:
      print("Grado 5")

print("Ejercicio 6".center(50, "-")+"|")

kilos_m = 7
descuento = 0
precio = 3

if 0 <= kilos_m <= 2:
      descuento = 0
elif 2 < kilos_m <= 5:
      descuento = 10
elif 5 < kilos_m <= 10:
      descuento = 15
elif kilos_m > 10:
      descuento = 20

total = kilos_m * precio
dinero_descontado = kilos_m * descuento * precio / 100
total_descuento = kilos_m * precio - kilos_m * precio * descuento / 100
print("Total sin descuento: {}\nDinero descontado: {}\nTotal con descuento: {}"
      .format(total_descuento, descuento, dinero_descontado))

print("Ejercicio 7".center(50, "-")+"|")





