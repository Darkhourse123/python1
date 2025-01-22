'=============================Циклы============================='
# циклы - это блок кода, который выполняет код определенное(неопределенное) кол-во раз
# for, while

# for - работает до конца итерируемого обьекта

# while - работает пока условие верное (True), если в условии появляется false то цикл завершает свою работу


'FOR'

list1 = [1,2,3,'hi', 'hello']

# for i in list1:
#     print(i)


'WHILE'

# num = int(input('Введите число: '))

# count = 0
# while count < 10: 
#     print('hi')
#     count += 1  #count = count + 1


# n = 0
# while n: # цикл не сработает так как тут False
#     print('hi')




# str1 = input('Введите слово: ') # катана

# while str1.islower(): 
#     print('с маленькой')
#     str1 = str1.upper() # KATANA


'====================Break, continue=================='

# break(ломать) - оператор который принудительно завершает работу цикла
# continue(продолжить) - оператор который пропускает итерацию если питон его встретит

# for i in range(1, 11): # [1,2,3,4,5,6,7,8,9,10]
#     if i == 3:
#         continue
#     print(i)


# for i in range(1,11,2):
#     if i == 2:
#         continue
#     print(i)

# 1
# 3
# 5
# 7
# 9

# for i in range(1,11):
#     print(i)
#     if i == 3:
#         continue
    
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# for i in range(1,11):
#     if i == 3:
#         break
#     print(i)

# 1
# 2


# for i in range(1,11): #3
#     print(i)
#     if i == 3:
#         break

# 1
# 2
# 3


# count = 0

# while count < 10: 
#     print(count) # 3
#     if count == 3:
#         continue
#     count += 1

# 0
# 1
# 2
# 3
# 3
# 3

# count = 0

# while count < 10: 
#     print(count)
#     if count == 3:
#         break
#     count += 1

# 0
# 1
# 2
# 3


# count = 0

# while count < 10: 
#     print(count)
#     count += 1
#     if count == 3:
#         continue

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9




# for i in range(1, 11):
#     print(i)
#     if i == 3:
#         break
# else:
#     print('Конец')

# else сработает тогда когда for завершит свою работу 'естественным путем', если цикл for завершается из-за оператора break то else не сработает


# count = 0
# while count < 5:
#     print(count)
#     count += 1
#     if count == 2:
#         break
# else:
#     print('цикл while завершил свою работу естественным путем')


# list2 = [23, 'hi', True, None, 34, -23]
# count = 0
# while count < len(list2): # 6
#     print(list2[count])
#     count += 1



# list1 = [23, 'hi', True]
# for i in list1: # True
#     a = list1.pop() # None
#     print(a)



# list2 = ['hi', None, -23]
# count = 0
# while count < len(list2): 
#     print(list2.pop(count))
#     count += 1
