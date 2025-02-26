
# BUILT-INS:
#     1) Даны два списка:
names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
print(dict(zip(names,ages)))
#     Создайте словарь, в котором ключи — это имена, а значения — соответствующие им возраста


#     2) Дана строка:
text = enumerate("python",1)
print(tuple(text))

#     при помощи определенной встроенной функции выведите индексы и символы, начиная с 1

#     3) Дан список строк с числами:
numbers = ["10", "20", "30", "40"]
mapped=map(int,numbers)
print(list(mapped))
#     Преобразуйте его в список целых чисел

#     4) Дан список слов:
words = ["apple", "banana", "cherry", "dog", "elephant"]
filtered=list(filter(lambda x:x.startswith('d'), words))
print(filtered)

#     Отфильтруйте и оставьте только те слова, которые начинаются с буквы d

#     5) Дан список чисел:
numbers = [1, -2, 3, -4, 5, -6]
pisitive_numbers=list(filter(lambda x: x >= 0, numbers))
print(pisitive_numbers)
# <filter object at 0x7ded4893bbb0>
# почему так выходит без листа?
squared_numbers = list(map(lambda x: x **2, pisitive_numbers))
print(squared_numbers)
# <map object at 0x7ded4893bb80>
# почему так выходит без листа?
result_numbers= list(squared_numbers)
print(result_numbers)
#     Сначала удалите отрицательные числа при помощи filter, затем возведите оставшиеся числа в квадрат с помощью map

#     6) Даны два списка:
students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]
    # УСЛОВИЯ ЗАДАНИЯ:
#     	1.	Используйте zip, чтобы соединить студентов и их оценки

print(list(zip(students,scores)))
# 	    2.	С помощью filter оставьте только тех, у кого оценка больше 80

print(list(filter(lambda x: x >= 80, scores)))
# 	    3.	Пронумеруйте оставшихся студентов, начиная с 1, используя enumerate
print(list(enumerate(students,1)))

# 	    4.	Преобразуйте результат в список кортежей (номер, имя, оценка)
print(tuple(map(str,students)))
    