tabla = 50

print("|"+"Ejercicio 1".center(tabla, "-") + "|")

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
cuadrado_num = num * num

print("El cuadrado del numero {}, es: {}".format(num, cuadrado_num))

print("|" + "Ejercicio 3".center(tabla, "-")+"|")

if num%2 == 0:
      senar_o_par = "par"
else:
      senar_o_par = "senar"

print("El numero {} es {}".format(num, senar_o_par))

print("|" + "Ejercicio 4".center(tabla, "-") + "|")
if num < 5:
      nota = "es un suspendido"
elif 5 <= num < 6.5:
      nota = "es un bien"
elif 6.5 <= num < 8.5:
      nota = "notable"
elif 8.5 <= num <= 10:
      nota = "es un excelente"
else:
      nota = "no es valido"
print("Un {} {}".format(num, nota))

print("|" + "Ejercicio 5".center(tabla, "-")+"|")

caracoles_d = 100
caracoles_p = 10001

if caracoles_p > 10000 and caracoles_d < 200:
      grado = "Grado 8"
elif caracoles_p > 10000 and caracoles_d >= 200:
      grado = "Grado 7"
elif caracoles_p <= 10000 and caracoles_d < 200:
      grado = "Grado 6"
elif caracoles_p <= 10000 and caracoles_d >= 200:
      grado = "Grado 5"
print("El grado del trabajador habiendo producido\n"
      "{} caracoles, de los cuales {} eran\n"
      "defectuosos es el {}"
      .format(caracoles_p, caracoles_d, grado))

print("|" + "Ejercicio 6".center(tabla, "-")+"|")

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
print("Comprando {} kilos a {} euros el kilo\n"
      "con un descuento del {}%...\n"
      "Total sin descuento: {}\n"
      "Dinero descontado: {}\n"
      "Total con descuento: {}"
      .format(kilos_m, precio, descuento, total, dinero_descontado, total_descuento))

print("|" + "Ejercicio 7".center(tabla, "-")+"|")

print("Perezón histórico")





