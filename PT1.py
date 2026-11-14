#1. Donats dos números, indicar la suma, resta, divisió i multiplicació dels dos nombres.
print("|"+"Ejercicio 1".center(50, "-")+"|")

num1 = 10
num2 = 20
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("|Las operaciones se realizaran con: {} y {}\n"
      "|La suma dara como resultado: {}\n"
      "|La resta dara como resultado: {}\n"
      "|La multiplicacion dara como resultado: {}\n"
      "|La division dara como resultado: {}\n"
      .format(num1, num2, suma, resta, multiplicacion, division))