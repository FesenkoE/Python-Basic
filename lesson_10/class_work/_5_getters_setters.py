"""
    Геттеры и сеттеры (getter, setter).

    Свойства (@property) - являются геттерами,
    например, с их помощью можно получить значение приватных атрибутов.

    Для геттера можно написать сеттер, который будет устанавливать значение.

"""


class User:
    name = None
    _surname = None
    __age = None
    phone = None

    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age
        self.phone = None

    @property
    def age(self):
        """ Свойство-геттер атрибута __age (получать) """
        return self.__age

    @age.setter
    def age(self, age):
        """ Свойство-сеттер атрибута __age (устанавливать)"""
        if age >= 18:
            self.__age = age


user = User("Jane", "Adams", 21)

print(user.name)
print(user._surname)
# print(user.__age)  # AttributeError: 'User' object has no attribute '__age'
# print(user._User__age)  # 21

user.age = 25  # вызывается сеттер и устанавливает значение 25
user.age = 15  # вызывается сеттер и значение 15 игнорируется, так как < 18

print(user.age)  # 25

del user  # удаляет экземпляр user, вызывается метод __del__
