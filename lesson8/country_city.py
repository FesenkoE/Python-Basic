"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.

    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""

data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}


def get_country(city):
    for key, value in data.items():
        if city in value:
            return key


def groupping_data(data, ):
    format_data = []
    for key, value in data.items():
        format_data.append({'country': key})
        format_data.append({'capital': value[0]})
        format_data.append({'cities': value[1:]})
    return format_data




print(get_country("Kiev"))
print(groupping_data(data))