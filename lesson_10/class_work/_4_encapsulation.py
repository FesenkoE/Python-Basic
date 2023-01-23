"""
    Уровни доступа атрибутов и методов класса.

    Всего 3 уровня:
    public - публичные, доступны везде
    _protected - защищенные, доступны везде
    __private - приватные атрибуты и методы,
        доступны только внутри класса, в котором они объявлены
"""


class Human:
    name = "Max"  # public
    _age = 22  # protected
    __pass = "I&@#RKBJWDQW"  # private

    def __hello(self):
        print("hello")

    @property
    def password(self):
        return self.__pass


obj = Human()

print(obj.name)  # Max
print(obj._age)  # 22
# print(obj.__pass)  # AttributeError: 'Human' object has no attribute '__pass'
print(obj.password)  # I&@#RKBJWDQW

# obj.__hello()  # AttributeError: 'Human' object has no attribute '__hello'
