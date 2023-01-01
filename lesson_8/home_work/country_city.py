"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.

    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""


def main():
    get_country('Berlin')

    data = {
        "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
        "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    }

    print(grouping_data(data))


def get_country(city):
    data = {
        "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
        "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
        "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
        "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    }

    for country, value in data.items():
        if city in value:
            print(f'The city {city} is situated in {country}')
            break
    else:
        print(f'The city {city} is not exist')


def grouping_data(data):
    countries = []
    capitals = []
    cities = []

    for country, values in data.items():
        countries.append(country)
        capitals.append(values[0])
        cities += values

    format_data = [
        {'countries': countries},
        {'capitals': capitals},
        {'cities': cities}
    ]

    return format_data


if __name__ == '__main__':
    main()
