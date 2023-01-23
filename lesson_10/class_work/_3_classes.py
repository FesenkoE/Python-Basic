"""
    Классы.

    class ClassName:
        # тело класса
        pass

    Создание объекта (экземпляра) класса.
    obj = ClassName()
"""


class User:
    # атрибуты класса
    name = None

    def __init__(self, name, surname, age, *args, **kwargs):
        """Это конструктор класса.
        При инициализации объекта вызывается этот метод.
        Аргументы, переданные в класс при инициализации, обрабатываются здесь.
        """
        self.name = name  # перезаписываем атрибут name
        self.surname = surname  # создаем атрибут surname
        self.age = age  # создаем атрибут age

    def __str__(self):
        """Метод вызывается, когда мы применяем print() или str() к объекту"""
        # т.е. при принте объекта класса будет отображаться full_name свойство
        return self.full_name

    def __repr__(self):
        """Метод вызывается при применении функции repr()"""
        return self.full_name

    def __del__(self):
        """Метод вызывается при удалении экземпляра класса"""
        print(f"User {self.full_name} was deleted.")

    # метод - это функция, которая привязана к экземпляру класса
    def byear(self):
        return 2021 - self.age

    # свойство - это метод, который ведет себя как атрибут
    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    # статический метод не принимает первый обязательный аргумент self
    @staticmethod
    def say_hello():
        print("Hello")

    # статический метод не принимает первый обязательный аргумент self
    @staticmethod
    def summ(a, b):
        print(a + b)

    # классовый метод первым аргументом принимает ссылку на сам класс (User)
    @classmethod
    def print_class_name(cls):
        print(cls)


user_1 = User("Max", "Smith", 21)  # инициализируем объект User

# user_1 доступны все методы и атрибуты класса User
print(user_1.name)  # Max
print(user_1.full_name)  # Max Smith
print(user_1.byear())  # 2000


# атрибуты объекта можно изменять
user_1.name = "John"
user_1.surname = "Adams"
print(user_1.full_name)  # John Adams


# классовые и статичекие методы методы
user_1.print_class_name()  # <class '__main__.User'>
user_1.say_hello()  # Hello
user_1.summ(2, 7)  # 9

User.print_class_name()  # <class '__main__.User'>
User.summ(5, 10)  # 15


# как и любые объекты экземпляры класса User можно поместить в список
user_list = []
user_object_1 = User("Max", "Smith", 21)
user_object_2 = User("John", "Adams", 22)
user_list.append(user_object_1)
user_list.append(user_object_2)

print(user_list)

for user in user_list:
    print(user.age, user.full_name)


# список можно сортировать, аналогично как и список слварей
print(sorted(user_list, key=lambda obj: obj.name.lower()))
