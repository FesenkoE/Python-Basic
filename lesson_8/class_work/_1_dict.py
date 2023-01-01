"""
    Словари.
"""

# Создание пустого словаря словаря
empty_dict = {}
# or
empty_dict = dict()
print(empty_dict, type(empty_dict))  # {}, <class 'dict'>

# Создание заполненного словаря
# 1
a = {"short": "dict", "long": "dictionary"}
print("1.", a)  # {'short': 'dict', 'long': 'dictionary'}

# 2
b = dict(short="dict", long="dictionary")
print("2.", b)  # {'short': 'dict', 'long': 'dictionary'}

# 3
c = dict.fromkeys(["a", "b", "c"])
print("3.", c)  # {'a': None, 'b': None, 'c': None}
d = dict.fromkeys(["a", "b", "c"], 123)
print(d)  # {'a': 123, 'b': 123, 'c': 123}

# 4 (конструктор)
g = {i: i * 2 for i in ["a", "b", "c"]}
print("4.", g)  # {'a': 'aa', 'b': 'bb', 'c': 'cc'}

# Доступ к элементам словаря по ключу
my_dict = {"colors": ["green", "red", "blue"], "tmp": "some tmp value"}
print(my_dict["colors"])  # ['green', 'red', 'blue']
print(my_dict["tmp"])  # 'some tmp value'

# Добавление/изменение значения по ключу
my_dict["tmp"] = 137  # изменит значение ключа 'tmp'
my_dict["string"] = "Hello world"  # добавит новый ключ и значение
print(my_dict)

# Удаление ключа
del my_dict["tmp"]
print(my_dict)  # {'colors': ['green', 'red', 'blue'], 'string': 'Hello world'}


# Хранение и доступ к информации пользователей на примере кортежей и словарей

# Вариант со списком кортежей
user_1 = ("Max", "max@gmail.com", "19.10.1999", "Ukraine")
user_2 = ("Ann", "ann@gmail.com", "19.10.1999", "Ukraine")
user_3 = ("John", "john@gmail.com", "19.10.1999", "Ukraine")

user_list = [user_1, user_2, user_3]

for user in user_list:
    print("name", user[0])  # доступ по индексу
    print("email", user[1])

# Вариант со списком словарей
user_1 = {
    "name": "Max",
    "email": "max@gmail.com",
    "bday": "19.10.1999",
    "country": "Ukraine",
}

user_2 = {
    "name": "Ann",
    "email": "ann@gmail.com",
    "bday": "19.10.1999",
    "country": "Ukraine",
}

user_3 = {
    "name": "John",
    "email": "john@gmail.com",
    "bday": "19.10.1999",
    "country": "Ukraine",
}

user_list = [user_1, user_2, user_3]

for user in user_list:
    print("name", user["name"])  # доступ по ключу
    print("email", user["email"])
