# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Какой номер интересен?: "))
if day > 7 or day < 1:
    print("Выбери из семи дней!")
elif day == 6 or day == 7:
    print("ДА!!! это выходной!!!!")
else:
    print("НЕТ!!!! опять пахать!")