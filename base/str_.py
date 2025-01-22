

'==================Строки(str)=================='
# строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки

string1 = 'строка с одинарными кавычками'

string2 = "строка с двойными кавычками"

# error = 'не правильная строка"

string3 = "Don't"

string4 = " Мой никнейм 'Katana' "

string5 = '''
 Привет
 как 
 дела 
'''

string6 = """ Привет 
как 
ты
"""

str7 = 'Привет' + ' ' + 'как дела?'
# print(str7)

# Конкатенация - склеивание строк 

str8 = 'Ha ' * 100
# print(str8)


'=================Экранизация======================'
# '\n' - перенос на новую строку
# print('hello world') # hello world
# print('hello\nworld') # hello
                      # world

# '\t' - табуляция 
# print('hello\tworld') # hello   world

# print('Don\'t')
# print("Don\"t")


# '\v' - перенос на новую строку со смещением вправо на длинну предыдущей строки

# print('hello\vworld\vmetalabs') # hello
                                      #  world
                                            # metalabs

# '\r' - перенос каретки на начало строки 
# print('Hello world\rGO')

'==================Форматирование строк====================='
# title = 'iPhone 16'
# price = 150000

# message = f'Я купил {title} за {price} сом'
# print(message)

# message2 = 'Я купил {} за {} сом'
# print(message2.format(price, title))
# print(message2.format('sdhfdjfdfs', 1324000)) 

# message3 = 'Я купил %s за %s сом'
# print(message3 % (title, price))


'===================Методы строк======================='
# методы - функции, которые относятся к определенному классу (типу данных), к ним мы обращаемся через точку

str1 = 'hello'
# .upper-верхний регистр
print(str1.upper()) # hello -> HELLO
#.lower-строку превращает в нижний регистр
print('HELLO'.lower()) # HELLO -> hello
# .swapcase- это все строки меняет наоборот
print('HeLlO'.swapcase()) # HeLlO -> hElLo
# .capitalize- только первая буква предложения за главную букву
print('hello woRld'.capitalize()) # hello woRld -> Hello world
# .title - каждое слово за главную букву
print('helLo woRld'.title()) # helLo woRld -> Hello World

print(dir(str))

# .center- Отцентрирует строку длиной 50 или .... символов
# print('hello'.center(11)) # '   hello   '
# print('hello'.center(11, '*')) # '***hello***'
# .count- считает кол - во символов в предложении
# print('hello world'.count('l')) # 3
# print('hello world'.count('ll')) # 1
# .startswith - проверяет начинается ли строка с данной символом
print('hello world'.startswith('he')) # True 
print('hello world'.startswith('H')) # False
# .endswith - проверяет заканчивается ли строка с данным символом
print('hello world'.endswith('rld')) # True
print('hello world'.endswith('gsd')) # False

# .islower- проверяет написана ли строка целиком в нижнем регистре
print('hello world'.islower()) # True
print('heLlo wOrlD'.islower()) # False

# .isupper-проверяет написана ли вся строка в верхнем регистре
print('hello world'.isupper()) # False
print('Hello world'.isupper()) # False
print('HELLO WORLD'.isupper()) # True

# .isdigit- проверяет питон состоит ли вся строка из цифр ( символы не смотрит)
print('hello'.isdigit()) # False
print('hello43434'.isdigit()) # False
print('4343'.isdigit()) # True

# .isalpha- проверяет питон состоит ли вся строка из букв(символы не смотрит)
print('hello'.isalpha()) # True
print('hello1231'.isalpha()) # False
print('1233'.isalpha()) # False

# .isalnum- проверяет питон состоит ли вся строка из цифр и букв(символы не смотрит)
print('hello 123'.isalnum()) # False
print('hello123'.isalnum()) #  True
print('hello'.isalnum()) #  True
print('123'.isalnum()) #  True
# .replace- это заменяет любой символ строки на данный символ
print('hello world'.replace('e', 'i')) # hillo world
print('hello world'.replace('o', 'i')) # helli wirld
print('hello world'.replace('l', 'i', 3)) # heiio worid
''.split()
''.join()

#===============Индексы строк=============

# Индексы- это порядковый номер элемента в последовательности ( символы в строке) индексация начинается с 0

# 'hello world'
#  012345678910
#      ... -2-1 
string="hello world"
print(string[0])#h
print(string[10])#d
print(string[-1])# d
print(string[5]) # " "

#срез - это подстрока строки (часть строки) - str[start:end:step]

print(string[2:5])#llo
# print(string[0:4]) или [:4] # hell
print(string[4:])# o world
print(string[:]) # hello world
print(string[::2])# hlowrd
print(string[::-1]) # dlrow olleh
print(string[-5:-1]) # worl
print(string[-1:-5:-1]) # dlro
print(string[:-5:-1]) # dlro

print('hello'.replace('h','d')) # dello потому что питон копирует поэтому изменился
str10='hello'
print(str10.replace('h','d')) # hello потому что питон взял с оригинала и поэтому не изменилась

#==================Логические и условные операторы===============

# Логические и условные операторы-это выражения, которые возвращают True, если выражение верное, False- если выражение не верное.

'Равенство'
10==5 # false
5==5 # true
'hi'=='hi'# true
'5'==5# false
print('hi'==2)

'Не равенство'
4!=5 # true
5!=5 # false

'Больше'
10>10# false
4>1# true

"Меньше"
5<4# false
10<10# false

'Больше или равно'
10>=4# true
10>=10# true
4>=5# false

'меньше или равно'
10<=10 #true
5<=10 # true
10<=5 # false

'==============and or not============='

# and - и
# or - или
# not - не
 
a=5
b=6

#true и   true
a==5 and b==6 # true
#false и true
a==7 and b==6 # false
#false и true 
a>10 and b<=6 # false
#false и false
a==0 and b ==0 # false

# если все части выражения возвращают true - ,будет True
# если хотя б одна часть выражения False - будет False


# True или True
a==5 or b==6 # true
#false или True
a>10 or b==6 # true
# true и False
a<20 or b==10 # True

a==1 or b==1 # False
# если  хотя бы одна часть выражения возвращает True - будет True

not True # False
not False # true
#   True
not a==5 # false
print(not a==5) # False
# false    false = False
# not true not true
# a<20      b==6 # False

False or False # False error
True and False or False or False
not b>20 and a ==5 or b==6 or a<6 and b>=6 or not a==5 and 5==10 # true

"=================Булевый тип данных Boolean type=========="
# Булевый тип данных - имеет всего 2 значения True и False

bool(1)# True
bool(-12)# true
bool(0) # false

bool("hello") # True
bool() or bool('') # false
bool(" ") # true
bool('_') # true
bool(True) # true
bool(False) # false

'=======================NoneType================='

# None  type-(пустота) это неизменяемый тип данных с одним значением None , который используется для обозначения отсутствие значения

a= None
bool(None)# false
a=5
b=5
a==b # true
print(a is b) 
 # is - это сравнивает айдишки переменных
v='num'
n='num'
print(id(v),(n))

'=============Условные операторы=============='
# Условные операторы - конструкция, который используется для того, чтобы при разных данных код работал по разному(в зависимости от условия)
 
# if условие1:
#    действие1

pogoda=input('введите погоду: ')
if pogoda=='солнечно':
     print('взять солнечные очки')
elif pogoda=='дождливо':
      print('взять зонт')   
else:
      print('пока')

'====================Тернаный оператор=============='

# Тернаный оператор - эьо условие в одну строку

num= -23
if num > 0: # условие1
    chislo = "положительное" # действие1
else:
    chislo = "отрицательное" # действие2

    # chislo=действие1 if условие1 else действие2
chislo = "положительное" if num>0 else "отрицательное"   
print(chislo) 


