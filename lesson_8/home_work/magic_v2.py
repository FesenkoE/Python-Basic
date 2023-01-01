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


def main():
    name = input('Enter your name: ')
    random_number = random.randint(0, 100)
    record = 0
    attempt = 0
    total_games = 0
    avg_attempts = 0

    while True:
        number = int(input('Enter a number: '))
        attempt += 1

        if number < random_number:
            print('Random number more than your number')
        elif number > random_number:
            print('Random number less than your number')
        else:
            total_games += 1
            if not record or record > attempt:
                record = attempt

            answer = input('Continue? (Y/n) ')

            if answer != 'n':
                attempt = 0
                random_number = random.randint(0, 100)
            else:
                player_data = {
                    'name': name,
                    'games': total_games,
                    'record': record,
                    'avg_attempts': (avg_attempts + attempt) / total_games
                }

                with open("player_data.json", "w") as f:
                    data = json.dumps(player_data)
                    f.write(data)

                print('Bye!')
                break


if __name__ == '__main__':
    main()
