# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

maxNumber = int(input("Введите число: "))
firstNumber = 1 
if maxNumber % 2 != 0:
    print("Введенное число не кратно 2")
else:
    while 2 * firstNumber <= maxNumber:
      print(2 * firstNumber," ")
      firstNumber += 1