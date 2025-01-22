# ===========tasc1==============
list1=[0,9,8,'hi','water',True,False,[5,6,7],3.1415,None]
print(list1[0]) # 0
print(list1[-1])# None
print(list1[7])# [5,6,7]

#=============tasc2===========
list2=[1,2,3,4,5,6,7,8,9]
list2.append(10)
print(list2) # [1,2,3,4,5,6,7,8,9,10]
list2.append(20)
print(list2) # [1,2,3,4,5,6,7,8,9,10,20]
# append- не добавляет более 2 элементов

list3=[1000,'fedz',1,2,3,4,56,7,8,9,0,'note',12,34,56,78,89,123,456,789,]
pop_1=list3.pop(1)
print((pop_1))
list3.remove('note')
print(list3)
pop_1=list3.pop()
print(pop_1) # что то не возвращает удаленный элемент, наоборот удаляет последний элемент
# [1,2,3,4,56,7,8,9,0,12,34,56,78,89,123,456] как возвращать не понял

#==============task3=============
list4=['as','dog','as','cat','as','become','as','pet']
count_1=list4.count('as')
print(count_1) # 4
list5 =[0,1,2,0,3,4,0,5,6,0,7,8,9,0,11,0,22,0,33,0,44,0,55,0,66,0,77,0,88,0,99,0]
a=list5.count(0)
print(a) #14

#================task4===========

list6=[3,4,45,'qoat','bee','cop',123,3245,'asd']
index_bee = list6.index('bee',2,9)
print(index_bee) # 4

#===========task5==========

nested_list = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(nested_list[2][0])
print(nested_list[0][2])
