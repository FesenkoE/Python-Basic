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
    def __init__(self, brand: str, model: str, engine: str, year: int):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.year = year

    def get_info(self):
        print(f'{self.brand} {self.engine} {self.year}')


cars = [
    Car('Volkswagen', 'Passat', 'v.2.0', 2015),
    Car('Toyota', 'Corola', 'v.1.6', 2008),
    Car('Audi', 'A8', 'v.2.0', 2017),
    Car('Nissan', 'Rouge', 'v.2.3', 2013),
    Car('Mazda', 'CX7', 'v.2.5', 2015)
]

cars = sorted(cars, key=lambda x: x.year)

for car in cars:
    car.get_info()
