"""
    zip(iter1, iter2)

    запаковывает элементы последовательностей iter1 и iter2
    и возвращает объект zip из которого можно сделать словарь

    dict(zip(iter1, iter2))

    * при не равном количестве элементов последовательностей,
    лишние ключи либо значения - игнорируются, т.е. создаются только пары
"""

keys = ["name", "email", "age"]
values = ["Max", "max@mail.com", 21]

user_data = dict(zip(keys, values))
print(user_data)  # {'name': 'Max', 'email': 'max@mail.com', 'age': 21}

print(dict(zip("abc", "123")))  # {'a': '1', 'b': '2', 'c': '3'}
print(dict(zip("abc", range(1, 100))))  # {'a': 1, 'b': 2, 'c': 3}
print(dict(zip(["name", "age"], ["Max"])))  # {'name': 'Max'}


"""
    Сортировка списка словарей по ключу.

    sorted(iter, key=func)
    list.sort(key=func)

    В функцию sorted() либо метод списка .sort() можно передать функцию func,
    которая будет применяться к каждому элементу последовательности
    при сортировке.

    Можно передавать обычную функцию либо использовать lambda выражения.
"""


data = [
    {
        "name": "Kate",
        "email": "kate@gmail.com",
        "bday": "19.10.1999",
        "country": "Germany",
    },
    {
        "name": "John",
        "email": "john@gmail.com",
        "bday": "19.10.1997",
        "country": "USA",
    },
    {
        "name": "ann",
        "email": "ann@gmail.com",
        "bday": "19.10.1998",
        "country": "Ukraine",
    },
    {
        "name": "ann",
        "email": "ann@gmail.com",
        "bday": "19.10.1998",
        "country": "France",
    },
]


def sort_by_name(data):
    # функция принимает словарь и возвращает значение по ключу 'name'
    return data["name"].lower()


def sort_by_name_country(data):
    # функция возвращает кортеж значений по ключу 'name' и 'country'
    return (data["name"].lower(), data["country"])


# 1. сортировка по 'name'
print("1.", sorted(data, key=sort_by_name))

# 2. сортировка по 'name' с использованием lambda функции
print("2.", sorted(data, key=lambda data: data["name"].lower()))

# 3. сортировка по 'name' и 'country' (если встречаются одинаковые 'name')
print("3.", sorted(data, key=sort_by_name_country))

# 4. сортировка по 'name' и 'country' с lambda функцией
print(sorted(data, key=lambda d: (d["name"].lower(), d["country"])))
