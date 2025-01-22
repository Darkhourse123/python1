#'==============Домашняя работа№2============'
# Task1

num1=10.5
print(num1) #10,5
print(int(num1)) #10
print(str(num1)) #10,5

# 2-ой способ

# # Число в формате float: 10.5
# # Число в формате int: 10
# # Число в формате строки: '10.5'

# num1 = 10.5
# print('Число в формате float:', num1) #число в формате float: 10.5
# print('Число в формате int:', int(num1)) #число в формате int: 10
# print('Число в формате str:', str(num1)) # число в формате str: 10.5

#task2

# num1=float(input('Введите ваше число: '))

# print('остаток от деления на 5: ',num1%5) # остаток от деления на 5: 3.6999999999999993
# print('число в кубе: ',num1**3) #число в кубе: 658.5029999999993
# print('Округленное число:', round(num1)) # округленное число: 9

# task3

num2=float(input("Введите ваше число")) # num2=7.4567
print('округление до 1 знака: ', (round(num2,1))) # округление до 1 знака: 7.5
print('округление до 2 цифры: ',(round(num2,2))) # округление до 2 цифры: 7.46

#task4

from decimal import Decimal
num=Decimal(input('Введите вещественное число: ')) # num=0.8
print(num+num+num+num+num+num+num+num+num+num) # 8.0
print(type(num)) # <class ' decimal.Decimal'>



