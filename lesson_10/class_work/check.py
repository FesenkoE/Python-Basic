import random

# 1. Создайте переменную x, которая равняется 2 в степени 3
x = 2 ** 3

# 2. Прибавьте к x 3
x += 3

# 3. Сгенерируйте список num_list длиной x, из случайных чисел от 1 до x
num_list = [random.randint(1, x) for _ in range(x)]

# or
# num_list = []
# for i in range(x):
#     num_list.append(random.randint(1, x))

# 4. Выведите на экран числа из списка num_list в обратном порядке
#    (от последнего до первого элемента) через пробел
print(" ".join(str(i) for i in num_list[::-1]))
# or
for i in reversed(num_list):
    print(i, end=" ")

# 5. Вставьте в средину списка число 11.
num_list.insert(len(num_list) // 2, 11)

# 6. Запишите в файл list_info.txt строчки
#    - 1. количество элементов списка num_list
#    - 2. количество уникальных элементов списка num_list
#    - 3. самое маленькое число списка num_list
#    - 4. сумму чисел списка num_list кратных 3
with open("list_info.txt", "w") as f:
    print(
        f"1. {len(num_list)}\n"
        f"2. {len(set(num_list))}\n"
        f"3. {min(num_list)}\n"
        f"4. {sum([i for i in num_list if i % 3 == 0])}",
        file=f,
    )

# 7. Отсортируйте список словарей countries_info
#    по ключу 'population' в порядке возрастания,
#    а также каждый список cities по длине строк в порядке убывания
countries_info = [
    {
        "country": "Ukraine",
        "population": 42000000,
        "cities": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    },
    {
        "country": "France",
        "population": 66999999,
        "cities": ["Paris", "Marseille", "Lyon", "Toulouse"],
    },
    {
        "country": "Germany",
        "population": 83000000,
        "cities": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    },
]
countries_info.sort(key=lambda d: d["population"])
for item in countries_info:
    item["cities"].sort(key=len, reverse=True)


# 8. Напишите функцию create_country_info, которая принимает параметры
#     country, population, cities и возвращает словарь
def create_country_info(country, population, cities):
    return {"country": country, "population": population, "cities": cities}


# or
# def create_country_info(**kwargs):
#     return kwargs


# 9. Создайте словарь с помощью функции create_country_info
#     и вставьте его в начало списка countries_info
data = create_country_info("USA", 333333333, ["New York", "Boston", "Seattle"])
countries_info.insert(0, data)

print(countries_info)
# 10. Создать репозиторий и залить туда этот файл
