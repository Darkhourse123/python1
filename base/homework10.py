# ==========task1===============
list1=input('Введите список товаров: ').replace(' ','')
list1.splite(',')
list2=input("Введите дополнительные товары: ").replace(' ','').split(',')
list1.extend(list2)
print(f"ваш список: {list1}")
if input("удалить последний товар из списка?")=='да':
    list1.pop()
    print(f"вы удалили последний товар из списка, ваш список: {list1}")
if input("хотите развернуть список? ")=="да":
    list1.reverse()
    print(f"ваш список: {list1}" )
if input(" хотите отсортировать список:"):
    list1.sort()
    print(f"ваш список отсортирован: {list1}")