
# Due Today
# Задания на Comprehension

# Списковое включение (List Comprehension)

# 1. Создайте список квадратов чисел от 1 до 10.
list1=[i ** 2 for i in range(1,11)]
print(list1)

# 2. Создайте список, состоящий только из нечетных чисел от 10 до 40.

list2 = [i for i in range(10, 41) if i % 2 != 0]
# list2 = [i for i in range(11, 41, 2)]
print(list2)
# 3. Создайте список квадратов чисел от 1 до 10, но только для чисел, которые делятся на 3.

list4=[i ** 2 for i in range(1,11) if i % 3 == 0]
print(list4)

#==================task2=================
# Словарное включение (Dict Comprehension)

# 1. Создайте словарь, где ключ — число от 1 до 5, а значение — его квадрат.
list1=[1,2,3,4,5]
dict1={i:i**2 for i in list1}
print(dict1)
# 2. Создайте словарь, где ключ — слово из списка ["apple", "banana", "cherry"], а значение — длина этого слова.
list2=['apple','banana','cherry']
list3=list2.index
dict2={i:len(i) for i in list2}
print(dict2)
#мне это помог чат gpt потому что было очень сложно

# 3. Создайте словарь, где ключ — число от 1 до 10, а значение — его квадрат, но только для чисел, больше 5.

dict3={i:i**2 for i in range(1,11) if i>5}
print(dict3)
#мне это помог чат gpt

#==================task3===============

# Множественное включение (Set Comprehension)

# 1. Создайте множество квадратов чисел от 1 до 10.

set1={i for i in range(1,11)}
print(set1)
# 2. Создайте множество уникальных слов из списка ["apple", "banana", "apple", "cherry"].
list1=["apple", "banana", "apple", "cherry"]
set1={i for i in list1}
print(set1)
# 3. Создайте множество всех уникальных ГЛАСНЫХ букв из строки "hello world
str1='hello world'
set1={i for i in str1}
print(set1)

#======================task4=================

# Генераторное выражение (Generator Expression)

# 1. Напишите генераторное выражение для получения кубов чисел от 1 до 10.
comp=(i**3 for i in range (1,11))
print(comp)

# 2. Напишите генераторное выражение для получения всех четных чисел от 1 до 20.
comp1=(i for i in range(1,21) if i % 2 == 0)
print(comp1)