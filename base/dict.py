'===============Dict(словари)==========='
# dict - изменяемый, итерируемый, "неупорядочный", неиндексируемый тип данных, для хранения данных в парах(ключ:значение)
user={
    'name':'katana',
    'age':21,
    'prof':'Dev'
    }
print(user['name']) #Katana

# ключами в словаре могут быть только не изменяемые типы данных
# если в словаре есть одинаковые ключи то сохранится последний

dict1={'a':1,'b':2,'c':3,'a':4}
print(dict1) # 
print(dict1['f']) # keyError 'f

#=================Создание============
user={'a':1,'b':2}
user=dict([('a',1),('b',2)('c',3)])
#list1=['ab','cd','ef']
#dict1=dict(list1) # {'a':'b','c':'d','e':'f'}
dict1={'prof':'dev'}
dict1={'name':'Katana'}
dict1={'prof': 'artist'}
# 

#============методы словаря===============
'strasdsad'.islower()
[1,2,3].append(5)
{'a':1}.clear()

# get- метод, который возвращает значение по ключу если такого ключа нет,то возвращает None или дефолтное значение
user={
    'name':'Katana',
    'age':21,
    'prog':'dev'
}
print(user.get('cbfnv'))# none
print(user.get('cbfnv','такого ключа нет'))# такого ключа нет

# pop-удаляет пару по ключу и возвращает значение
num=user.pop('age')
print(num)

#popitem - удаляет последнюю пару и возвращает ее
dict1={'a':1, 'b':2}
num=dict1.popitem() #('b',2)
print(num)

# updete- расширяет словарь парами из второго словаря
dict1={1:'a',2:'b'}

dict2 = {2:'c', 4:'d'}

dict1.update(dict2)
print(dict1) # 


# fromkeys - метод для создания нового словаря, используя список ключей
dict1=dict.fromkeys('h',12)
print(dict1)
dict2=dict.fromkeys([10,20,30],'hello')
print(dict2)
user={1:'a'}
# keys-возвращает все ключи- dict_keys([1,2])
#values-возвращает все значение-
#items-возвращает все пары
print(user.keys())
print(user.values())
print(user.items)

print(dir(dict))

#================итерирование словарей============
user = {
    'name':'Katana',
    'age':21,
    'prog':'dev'
}
a,b=3,5
for key , values in user.items(): # ("name","katana")
    print(key,values)

# вам дан словарь
dict1 = {"a":1, "b":2, "c":3}
# создайте новый словарь, поменяв ключи со значениями
#dict2 = {1:"a", 2:"b", 3:"c"}

