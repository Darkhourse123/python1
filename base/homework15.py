#======================task1====================
# Задание: Определите ошибки и исправьте код

# В каждом из приведенных ниже примеров есть ошибка.

# 1. Запустите код в интерпретаторе Python.
# 2. Запишите, какая ошибка будет выведена.
# 3. Объясните, что означает эта ошибка и как её можно исправить.

# Пример 1:

# x = "10" + 5
# TypeError: can only concatenate str (not "int") to str
# это значит что строку надо печатать со строкой, а числа с числами
# правильно будет x=10+5 будет15 или x='10'+'5' будет 105
try:
    x = "10" + 5
except TypeError:
    print('вы ввели не правильно')
else:
    print('до свидания')
# Пример 2:

# numbers = [1, 2, 3]
# print(numbers[5])
# IndexError: list index out of range
# это значит что в листе последовательность такого индекса нет
# numbers = [1, 2, 3] здесь индекса от 0 до 2 есть. и надо будет print(numbers[2])
try:
    numbers=[1,2,3]
    print(numbers[5])
except IndexError:
    print('такого индекса не существует')

# Пример 3:

# age = "25"
# print(age / 5)
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# это значит строки с числами делить или что-то печатать нельзя
# надо переменную без кавычки, вот тогда будет прекрасно
try:
    age = "25"
    print(age / 5)
except TypeError:
    print('не правильно, посмотри свою переменную и исправь')
# Пример 4:

# my_dict = {"name": "Alice", "age": 30}
# print(my_dict["gender"])
# KeyError: 'gender'
# это значит что такого ключа или значении не существует
# надо будет убрать gender и набрать то что есть или gender тоже надо добавить в словарь
# Пример 5:

# for i in range("5"):
# print(i)
# IndentationError: expected an indented block after 'for' statement on line 56
# это значит что в range строку или одно число не надо ставить. правильно будет range(1,6),чтобы печатало от 1 до 5
# Пример 6:

# value = None
# print(value + 10)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# это значит что пустота не рабатает ни с числами или даже ни с кем 
#если так надо было то тогда надо будет форматировать 
#  value = None
# print(f value + {10})  или print(f{value} + 10) думаю будет правильно 

# Пример 7:

# a = 10
# b = 0
# result = a / b
# print(result)
# ZeroDivisionError: division by zero
# это значит на ноль делить нельзя
# думаю исправить нельзя или надо просто заменить ноль на другую цифру
# Как оформлять ответ:

# 1. Укажите название ошибки (например, TypeError, IndexError, ZeroDivisionError и т.д.).
# 2. Объясните, почему она произошла.
# 3. Напишите исправленный вариант кода.