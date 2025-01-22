
# вам дан словарь
dict1 = {
    "a":1,
    "b":2, 
    "c":3
    }
dict2=dict.fromkeys([1],'a')
print(dict2)
dict3=dict.fromkeys([2],'b')
print(dict3)
dict4=dict.fromkeys([3],'c')
print(dict4)
dict2.update(dict3)
dict2.update(dict4)
print(dict2)

# создайте новый словарь, поменяв ключи со значениями
#dict2 = {1:"a", 2:"b", 3:"c"}