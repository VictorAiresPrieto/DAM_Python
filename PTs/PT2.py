import random

tabla = 50

print("|"+"Ejercicio 1".center(tabla, "-") + "|")

divisible3 = 0
divisible2 = 0
max_num = 100
min_num = 0
for i in range (min_num + 1, max_num + 1):
    if i%3 == 0:
        divisible3 = divisible3 + 1
    if i%2 == 0:
        divisible2 = divisible2 + 1

print("En el rango entre {} y {}\n"
      "hay {} numeros divisibles entre 3 y\n"
      "{} numeros divisibles entre 2".format(min_num, max_num, divisible3, divisible2))

print("|" + "Ejercicio 2".center(tabla, "-") + "|")

nums = [2,5,7,1,4,2,3,8,93,2,14,0,2,-1]
total = 0

for j in range (0, len(nums)):
    total = total + nums[j]

cantidad = len(nums)
media = total / len(nums)

print("Dados los numeros\n{},\n"
      "al sumarlos dan {}\n"
      "que dividiendolo entre {}\n"
      "obtenemos la media aritmetica que es {:.2f}"
      .format(nums, total, cantidad, media))

print("|" + "Ejercicio 3".center(tabla, "-") + "|")

mayor = 0
total = 0
nums_usados = []
for k in range (0, len(nums)):

    if nums[k] == 0:
        break
    nums_usados.append(nums[k])
    if k == 0:
        mayor = nums[k]
    else:
        if mayor < nums[k]:
            mayor = nums[k]

    total = total + nums[k]
media = total / len(nums_usados)
print("Dados los numeros\n{},\n"
      "el mayor de ellos es {}\n"
      "y la media es {:.2f}".format(nums_usados, mayor, media))

print("|" + "Ejercicio 4".center(tabla, "-") + "|")

pos_eureka = random.randint(0,10)
eureka_donde = []
for l in range (10):
    if pos_eureka == l:
        eureka_donde.append("eureka")
    else:
        eureka_donde.append("")

resultado = ""
for m in range (3):
    if eureka_donde[m] == "eureka":
        resultado = "Has acertado con {} intentos".format(m+1)
        break
    else:
        resultado = "Has perdido"

print(resultado)

print("|" + "Ejercicio 5".center(tabla, "-") + "|")

dia = random.randint(1, 35)
mes = random.randint(1, 15)
anno = random.randint(1900, 2100)

meses_y_dias = {
    1: (31, "Enero"),
    2: (28, "Febrero"),
    3: (31, "Marzo"),
    4: (30, "Abril"),
    5: (31, "Mayo"),
    6: (30, "Junio"),
    7: (31, "Julio"),
    8: (31, "Agosto"),
    9: (30, "Septiembre"),
    10: (31, "Octubre"),
    11: (30, "Noviembre"),
    12: (31, "Diciembre"),
}
mes_valido = True
bisiesto = 0
if not mes in meses_y_dias.keys():
    print("El mes {} no existe".format(mes))
    mes_valido = False
if mes==2 and dia==29:
    if anno%4 != 0:
        print("El dia {} de febrero no exite\nya que el año {} no es bisiesto".format(dia, anno))
    else:
        bisiesto = 1
if mes_valido:
    if 0 < dia-bisiesto <= meses_y_dias[mes][0]:
        print("{} de {} de {}".format(dia, meses_y_dias[mes][1], anno))
    elif bisiesto == 1:
        print("El dia {} no exite".format(dia))
print(dia,mes,anno)

