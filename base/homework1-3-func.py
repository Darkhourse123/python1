# FUNCTIONS:
#     **ПРИМЕЧАНИЕ: Все задачи должны быть решены при помощи функций**

#     1) Вы работаете в Банке и пишите программу которая считает % для кредита. Спросите у пользователя сумму займа(не меньше 100 000) и посчитайте сколько нужно будет вернуть если процент = 7.89, результат округлите до 2 чисел после точки.
#     Формула подсчёта переплаты: Сумма * (% / 100)

# def bank():
#     zaim=int(input('введите сумму займа от 100000 и более: '))
#     protsent=7.89
#     protsent1=100
#     return round(zaim*(protsent/protsent1),2)
# print(bank())

#     2) Запросите у пользователя ввести текст с цифрами, 
#     найти цифры и преобразовать их в целое число, затем вывести на терминал

# def number():

#     3) Создайте  функцию, которая выполняет следующее действие:
#     Пользователь вводит количество месяцев и лет. 
#     Вывести в терминал количество дней за это время. 
#     Считать, что в каждом месяце 30 дней
def month():
    time=int(input('Введите кол-во месецев: '))
    age=int(input('введите кол-во годов: ' ))
    year=12
    day=30
    count=time*day
    count1=age*year*day
    print(count)
    print(count1)
month()

#     4) Создайте функцию, которая возвращает словарь, 
# #     где ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб
def dict01():              
    return {i: i**3 for i in range(1, 11)}


#     5) Напишите функцию, которая высчитывает сумму чисел от 1 до 50 и возвращает результат. 
def integers(x,y):
    return x+y,range(1,51)

num1=integers(50,60)
print(num1)
