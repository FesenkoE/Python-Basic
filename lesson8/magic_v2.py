"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.

    1. При запуске, программа спрашивает имя игрока.

    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру

    3. При выходе из программы данные игрока записывать в файл (txt либо json).

    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.

"""


import random
import json

# player_data = {'name': None, 'games': None, 'record': None, 'avg_attempts': None}


def create_file():
    try:
        with open('magic.json') as f:
            pass
    except FileNotFoundError:
        data = [{'name': None, 'games': None, 'record': None, 'avg_attempts': None}]
        with open('magic.json', 'w') as f:
            json.dump(data, f, indent=4)


def init_player():
    user_name = input('Введите Ваше имя: ')
    with open('magic.json', 'r') as f:
        data = json.load(f)
        for user in data:
            if user['name'] == user_name:
                return user
        return {'name': user_name, 'games': 0, 'record': 999, 'avg_attempts': 999}


def greeting(player_data):
    if player_data['games'] == 0:
        print(f'Привет {player_data["name"]}!\n'
              f'Это твоя первая игра!')
    else:
        print(f'Привет {player_data["name"]}!\n'
              f'Твой предыдущий результат:\n'
              f'* пройдено игр: {player_data["games"]}\n'
              f'* рекорд: {player_data["record"]}\n'
              f'* средний результат: {player_data["avg_attempts"]}\n')
    input('Поехали? Нажимай Enter')


def game(data):
    player_data = data
    count_attempt = 0
    rand = random.randint(0, 1000)
    while True:
        count_attempt += 1
        try:
            num = int(input('Введи число от 0 до 1000 : '))
        except ValueError:
            continue
        if num < rand:
            print('Твоё значение меньше')
        elif num > rand:
            print('Твоё значение больше')
        else:
            print('Верно!', rand)
            print('Количество попыток:', count_attempt)
            break

    if player_data['record'] == 999:
        player_data['record'] = count_attempt
    if player_data['record'] > count_attempt:
        player_data['record'] = count_attempt
        print('Это твой новый рекорд!!!')

    player_data['games'] += 1

    if player_data['avg_attempts'] == 999:
        player_data['avg_attempts'] = count_attempt
    else:
        player_data['avg_attempts'] = (count_attempt + player_data['avg_attempts'] * (player_data['games'] -1)) /\
                                      player_data['games']

    y_n = input('Continue(Y/n)?')
    if y_n == 'n' or y_n == 'N':
        return player_data
    else:
        return game(player_data)


def save_data_in_file(player_data):
    data = []
    with open('magic.json', 'r') as f:
        data = json.load(f)
        for user in data:
            if user['name'] == player_data['name']:
                user['games'] = player_data['games']
                user['record'] = player_data['record']
                user['avg_attempts'] = player_data['avg_attempts']
                break
        else:
            data.append(player_data)
    with open('magic.json', 'w') as f:
        json.dump(data, f, indent=4)



def main():
    create_file()
    player_data = init_player()
    greeting(player_data)
    player_data = game(player_data)
    save_data_in_file(player_data)
    print(f'Твои результаты:'
          f'Пройдено игр: {player_data["games"]}\n'
          f'Рекорд: {player_data["record"]}\n'
          f'Средний резульат: {player_data["avg_attempts"]}\n'
          f'Пока {player_data["name"]}!')


if __name__ == '__main__':
    main()