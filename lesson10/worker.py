"""
    Перед решением задания внимательно пересмотрите материалы урока
    lesson10/_5_getters_setters.py и lesson10/_6_inheritance.py

    Реализуйте класс Employee, наследуясь от класса User

    1. Employee имеет такие харакеристики (атрибуты создаются в __init__):
    - name - имя (наследуется от User)
    - surname - фамилия (наследуется от User)
    - company - компания (необязательный атрибут)
    - position - должность (_protected необязательный атрибут)
    - exp (exp) - опыт работы (__private с дефолтным значением 0)

    2. Реализовать свойство career_start_year = текущий год - опыт работы.
        За текущий год брать 2021 или лучше
        from datetime import datetime
        datetime.now().year

    3. Релизовать метод get_status, который возвращает статус работника.
        либо "Max works at Google as a developer since 2018."
        либо "Max works at Google since 2021."
        либо "Max is probably unemployed."
    в зависимости от заполнения атрибутов company и position

    4. Для атрибута __exp создайте getter и setter.
        Опыт работы можно только увеличить, при попытке уменьшить - игнорируем.

    5. При удалении объекта выводить сообщение:
        "Max was fired from Google."
        либо "Max was fired.", если компания была не заполнена.

    ** Дополнительно можно создать приватный атрибут salary,
    в котором хранится уровень ЗП работника. И при изменении опыта работы exp -
    увеличивать salary на 10% за каждый добавленый год.

"""
from datetime import datetime


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def full_name(self):
        return f"{self.name.title()} {self.surname.title()}"

    def get_info(self):
        return f"This is a regular user {self.full_name}"

    def __str__(self):
        return self.name


class Employee(User):
    def __init__(self, name, surname, exp=0, company=None, position=None):
        super().__init__(name, surname)
        self.company = company
        self._position = position
        self.__exp = exp

    def career_start_year(self):
        return 2021 - self.__exp
        # return datetime.now().year - self.__exp

    def get_status(self):
        if self.company is None:
            return f"{self.name} is probably unemployed."
        elif self._position is None:
            return f"{self.name} works at {self.company} since {Employee.career_start_year(self)}."
        else:
            return f"{self.name} works at {self.company} as a {self._position} since {Employee.career_start_year(self)}."

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        if exp > self.__exp:
            self.__exp = exp

    def __del__(self):
        if self.company is None:
            print(f"{self.name} was fired.")
        else:
            print(f"{self.name} was fired from {self.company}.")
    """TODO: Реализовать класс здесь"""


def main():
    pass

    # Для проверки можете раскомментировать запуск тестов
    run_test()


def run_test():
    """ Несколько тестов для проверки правильности выполнения пунктов """
    employee = Employee("Max", "Smith", 2, "Google", "developer")
    assert len(employee.__dict__) == 5, "1. Error"
    print("1. Correctly")
    assert employee.career_start_year() == 2019, "2.1 Error"
    employee = Employee("Max", "Smith", 0, "Google", "developer")
    assert employee.career_start_year() == 2021, "2.2 Error"
    print("2. Correctly")

    status = employee.get_status()
    print(status)
    assert (
            status == "Max works at Google as a developer since 2021."
    ), "3. Error"
    employee = Employee("Max", "Smith", company="Google")
    assert (
            employee.get_status() == "Max works at Google since 2021."
    ), "3. Error"
    employee = Employee("Max", "Smith")
    assert employee.get_status() == "Max is probably unemployed.", "3. Error"
    print("3. Correctly")

    employee.exp = 5
    assert employee.exp == 5, "4. Error"
    employee.exp = 2
    assert employee.exp == 5, "4. Error"
    print("4. Correctly")


if __name__ == "__main__":
    main()
