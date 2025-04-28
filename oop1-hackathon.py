# Задание: Регистрация юзера
# Регистрация юзера
# Создайте классы User, Post и функцию validate_password. Функция validate_password
# должна проверять соответствует ли
# пароль следующим требованиям:
# 1) Пароль должен состоять минимум из 8 символов, если длина меньше 8 символов
# сгенерируйте
# исключение с сообщением &#39;Пароль слишком короткий!&#39;.
# 2) Пароль должен состоять из букв и цифр, иначе сгенерируйте исключение с
# сообщением &#39;Пароль должен состоять из букв и цифр!&#39;
# Класс User наследуется от 4 миксинов:
# 1. RegisterMixin - реализуйте в нем метод &#39;register&#39;, который записывает нашего юзера
# в файл user.json в виде словаря с ключами:
# id - уникальный идентификатор юзера
# name - имя юзера
# password - пароль юзера
# Метод принимает 2 аргумента name и password, а id вы должны сгенерировать сами.
# Также метод должен проверять, есть ли такой юзер в базе данных (user.json), если
# такой юзер уже существует сгенерируйте исключение с сообщением &#39;Такой юзер уже
# существует!&#39;. Иначе запишите его в БД(user.json) и возвратите сообщение &#39;Successfully
# registered&#39;. Перед записью в БД не забудьте проверить пароль с помощью созданной
# вами функции(validate_password).
# 2. LoginMixin - реализуйте в нем метод &#39;login&#39; - который имитирует вход в систему.
# Метод принимает 2 аргумента name и password. Метод должен проверять есть ли
# такой пользователь в БД(user.json) если его нет то сгенерируйте сообщение &#39;Нет
# такого юзера в БД!&#39;. Если же такой юзер существует проверьте совпадает ли
# переданный юзером пароль с паролем юзера с БД(user.json), если пароли не
# совпадают сгенерируйте исключение &#39;Неверный пароль!&#39;. Иначе возвратите
# сообщение &#39;Вы успешно залогинились!&#39;
# 3. ChangePasswordMixin - реализуйте в нем метод &#39;change_password&#39; который будет
# изменять пароль пользователя. Метод принимает 3 аргумента name, old_password,
# new_password. В первую очередь проверьте новый пароль на валидность с помощью
# созданной вами функцией. Далее проверьте совпадает ли переданный пароль юзера с
# паролем юзера из БД(user.json), если нет то сгенерируйте исключение с сообщением
# &#39;Старый пароль указан не верно!&#39;. В ином случае измените новый пароль у юзера в
# БД(user.json) и возвратите сообщение &#39;Password changed successfully!&#39;
# 4. ChangeUsernameMixin - реализуйте в нем метод &#39;change_name&#39; который будет
# изменять имя юзера. Метод принимает 2 аргумента old_name и new_name. В первую
# очередь проверьте существует ли такой юзер которого хотим изменить в
# БД(user.json), если его нет то сгенерируйте исключение с сообщением &#39;Нет такого
# зарегистрированного юзера в БД!&#39;. Далее проверьте, не занято юзера с новым именем
# в БД. Если же такое имя уже существует выведите сообщение &#39;Пользователь с таким
# именем уже существует!&#39;, и попросите пользователя вводить новое имя до тех пор
# пока она не станет уникальным. Как только новое имя будет уникальным в рамках
# нашей БД, перезапишите это имя у пользователя в БД и возвратите сообщение
# &quot;Username changed successfully!&quot;
# Класс Post.
# У класса Post есть метод который отвечает за инициализацию объектов и он
# принимает следующие атрибуты: title, description, price, quantity, owner.
# Так же класс наследуется от миксина CheckOwnerMixin.
# CheckOwnerMixin - миксин содержит метод &#39;check&#39; который принимает аргумент
# &#39;owner&#39; и просто проверят если переданное имя &#39;owner&#39; в БД(user.json). Если его нет
# то сгенерировать исключение с сообщением &#39;Нет такого пользователя!&#39;. Иначе
# создаваемый объект от класса Post будет успешно создан. (Запись постов записывать
# в БД не надо!)

# Создайте несколько объектов класса User и Post и примените все функции доступные
# им.
# Требование к проекту:
# 1. При выполнении программы не должно возникать ошибок
# 2. Код должен соответствовать PEP8
# 3. Проект нужно закинуть на GitHub
# Пример содержания БД(user.json):
# [
# {
# &quot;id&quot;: 1,
# &quot;name&quot;: &quot;John&quot;,
# &quot;password&quot;: &quot;john123123&quot;
# },
# {
# &quot;id&quot;: 2,
# &quot;name&quot;: &quot;Rick&quot;,
# &quot;password&quot;: &quot;rick123123&quot;
# },
# {
# &quot;id&quot;: 3,

# &quot;name&quot;: &quot;Sam&quot;,
# &quot;password&quot;: &quot;sam123123&quot;
# }
# ]

import json
class User():

    def __init__(self, name,password):
        self._name=name
        self._password=password

    def write_user_name(self):
        return self._name

    def write_password(self):
        return self._password
    
    def __str__(self):
        return f'User(name={self._name},password=)'

object1= User('Zhanuzak_2001@gmail.com','zhanuzak2001')

object1.write_user_name
object1.write_password
print(object1)


class Post():
    ...
def Validate_password():
    ...

import json

# ========================

class RegisterMixin:
    def register(self, name, password, id):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == name:
                print('Такой юзер уже существует!')
                return
        data.append({
            "id": id,
            "name": name,
            "password": password
        })
        with open('user.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print('Successfully registered')


class LoginMixin:
    def login(self, name, password):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == name:
                if n['password'] == password:
                    print('Вы успешно залогинились!')
                else:
                    print("Неверный пароль!")
                return
        print('Нет такого юзера в БД')


class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == name:
                if n['password'] == old_password:
                    n['password'] = new_password
                    print('Password changed successfully!')
                else:
                    print('Старый пароль введен не верно!')
                break
        else:
            print('Нет такого юзера в БД')
            return
        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4)


class ChangeUsernameMixin:
    def change_name(self, old_name, new_name):
        with open('user.json', 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == old_name:
                n['name'] = new_name
                print('Имя успешно изменено!')
                break
        else:
            print('Нет такого юзера в БД')
            return
        with open('user.json', 'w') as file:
            json.dump(data, file, indent=4)


class CheckOwnerMixin:
    def check(self, owner):
        with open("user.json", 'r') as file:
            data = json.load(file)
        for n in data:
            if n['name'] == owner:
                return
        print('Нет такого пользователя!')

# ========================

class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    count = 0

    def __init__(self):
        User.count += 1

    def register(self, name, password):
        self.valitade_password(password)
        return super().register(name, password, User.count)

    def login(self, name, password):
        return super().login(name, password)

    def change_password(self, name, old_password, new_password):
        self.valitade_password(new_password)
        return super().change_password(name, old_password, new_password)

    def change_name(self, old_name, new_name):
        return super().change_name(old_name, new_name)

    @classmethod
    def incounter(cls):
        cls.count += 1

    def valitade_password(self, password):
        if len(password) < 8:
            raise ValueError('Пароль слишком короткий!')
        if not any(i.isdigit() for i in password):
            raise KeyError('Пароль должен состоять из букв и цифр!')
        if not any(i.isalpha() for i in password):
            raise KeyError('Пароль должен состоять из букв и цифр!')

class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner):
        self.check(owner)
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner

obj1 = User()
obj1.register('jonh', 'dfwfw211')
obj2 = User()
obj2.register('rick', 'dwfewfwe2')
obj3 = User()
obj3.register('sam', 'wfwefwe43')