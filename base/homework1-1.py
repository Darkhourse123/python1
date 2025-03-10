#===============1 task================
# 1) Напишите list comprehension, который создаст список квадратов чисел от 1 до 10
list1=[i**2 for i in range(1,11)]
print(list1)
# 2) Используя list comprehension, создайте список только из четных чисел от 1 до 20

list3=[i for i in range(1,21) if i % 2 ==0]
print(list3)
# 3) Используя dict comprehension, создайте словарь, где ключ — число от 1 до 5, а значение — его квадрат.
list1=[1,2,3,4,5]
dict1={i:i**2 for i in list1}
print(dict1)
# 4) вам дан список words = ["python", "java", "swift", "golang", "javascript"], используя list comprehension, создайте новый список из слов длиной больше 5 символов
words = ["python", "java", "swift", "golang", "javascript"]
list2=[i for i in words if len(i)>5]
print(list2)
# 5) Вам дан список, words = ["apple", "banana", "cherry"], используя list comprehension, получите список этих слов в верхнем регистре
words1 = ["apple", "banana", "cherry"]
list4=[i.upper() for i in words1]
print(list4)
