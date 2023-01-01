"""
    Основные функции модуля os.

    Модуль предоставляет функционал для работы с файлами, директориями
    и командной строкой.
"""
import os

print(os.getcwd())  # возвращает полный путь к текущей директории
print(os.listdir("."))  # содержимое текущей директории
print(os.listdir("../"))  # содержимое директории на уровень выше

# os.rename('hello.txt', 'new_hello.txt')  # переименование
# os.remove('hello.txt')  # удаление файла
os.mkdir("files")  # создание папки
# os.makedirs("files/category")  # создание вложенных директорий
os.rmdir("files")  # удаление директории
# os.system('python3 _1_files.py')  # выполняет строку как команду в терминале

# os.path.isfile('path') - возвращает True, если файл и False, если директория

for i in os.listdir("."):
    if os.path.isfile(i):
        print(i, "file")
    else:
        print(i, "folder")
