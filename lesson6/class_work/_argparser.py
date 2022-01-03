"""
    Модуль argparse используется для обработки аргументов командной строки.

    Ниже описан пример обработки 2 не обязательных аргументов -n и -s

    Варианты запуска файла:
    python _argparser.py
    python _argparser.py -n Max
    python _argparser.py --name Max
    python _argparser.py -n Max -s Smith
    python _argparser.py --name Max --surname Smith
"""

import argparse

parser = argparse.ArgumentParser(description="some description..")
parser.add_argument("-n", "--name")
parser.add_argument("-s", "--surname", default="programmer")

args = parser.parse_args()

name = args.name
surname = args.surname

print(f"Hello, {name} {surname}!")
