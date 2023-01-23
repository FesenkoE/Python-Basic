"""
    Для того, чтобы больше попрактиковаться с классами
    воспользуйтесь задачником http://www.itmathrepetitor.ru/zadachi-na-klassy/

    Реализуйте класс Alphabet.

    Алфавит имеет такие атрибуты (создаются в конструкторе __init__):
    - language (язык)
    - letters (список букв алфавита)

    Объект алфавита может (методы):
    - вывести все буквы алфавита
    - посчитать количество букв алфавита
    - определять, относится ли буква к этому алфавиту
"""


class Alphabet:
    def __init__(self, language: str, letters: list):
        self.language = language
        self.letters = letters

    def output_alphabet(self):
        for char in self.letters:
            print(f'{char}')

    def len_alphabet(self):
        return len(self.letters)

    def in_alphabet(self, char: str):
        if char in self.letters:
            print(f'Char is in the list')
            return True


new_alphabet = Alphabet('en', ['d', 's', 'd', 'f', 's', 'd', 'f', 's', 'd', 'f'])
new_alphabet.output_alphabet()
new_alphabet.in_alphabet('f')
print(f'Alphabet length - {new_alphabet.len_alphabet()}')
