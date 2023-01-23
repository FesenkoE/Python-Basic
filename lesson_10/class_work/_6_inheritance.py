"""
    Наследование.

    Класс может наследоваться от 1 и более других классов,
    при этом будет наследовать атрибуты, методы и свойства классов-родителей.

    class MyClass(FirstParentClass, SecondParentClass):
        pass

    Для того, чтобы при переопределении метода вызвать метод класса родителя
    используем super().method_name()
"""


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def byear(self):
        return 2021 - self.__age


class Test:
    def test(self):
        print("message from test method Test class")


class Student(User, Test):
    """Класс Student наследует методы и атрибуты из классов User и Test"""

    def __init__(self, name, surname, age, city):
        """При необходимости дополнить метод,
        например при инициализации обрабатывать дополнительные аргументы,
        необходимо вызвать метод класса-родителя через super()
        Либо просто переопределить метод (перегрузить)"""

        # вызывается метод __init__ класса User,
        # который принимает name, surname и age и создает атрибуты
        super().__init__(name, surname, age)

        # и создаем новый атрибут в этом классе
        self.city = city

    def say(self):
        print("i am a student")

    def full_name(self):
        """При необходимости полностью изменить поведение метода,
        его можно полностью переопределить (перегрузка метода)
        """
        return f"{self.name} from {self.city}"

    def test(self):
        if self.name == "test":
            # если условие выполняется - вызываем метод из класса-родителя
            return super().test()


user_obj = User("John", "Adams", 22)
student_obj = Student("Ann", "Smith", 19, "Kiev")

print(user_obj.full_name)  # John Adams
print(student_obj.full_name())  # Ann from Kiev

print(user_obj.byear())  # 1999
print(student_obj.byear())  # 2002


student_obj.say()  # i am a student
student_obj.test()

student_obj.name = "test"

student_obj.test()  # message from test method Test class
