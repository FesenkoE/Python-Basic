"""
    1. Реализуйте класс Car с атрибутами:
    - brand (марка)
    - model (модель)
    - engine (объем двигателя)
    - year (год выпуска)

    2. Создайте метод get_info,
        "Ford Focus v2.3", где 2.3 - объем двигателя (engine)

    3. Создайте список из 5 объектов класса Car.
    4. Отсортируйте список объектов по year
    5. Выведите на экран результат метода get_info для каждого объекта списка
"""


class Car:
    def __init__(self, brand, model, engine, year):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.year = year

    def get_info(self):
        return f'{self.brand} {self.model} v{self.engine}'


car1 = Car('Mercedes', 'Vito', 2.2, 2019)
car2 = Car('BMW', 'X5', 3.0, 2020)
car3 = Car('Toyota', 'Land Cruiser', 4.0, 2022)
car4 = Car('Lamborghini', 'Diablo', 5.5, 2015)
car5 = Car('Audi', 'Q8', 3.0, 2021)

cars_lst = [car1, car2, car3, car4, car5]
cars_lst.sort(key=lambda carr: carr.year)
for car in cars_lst:
    print(car.get_info())

