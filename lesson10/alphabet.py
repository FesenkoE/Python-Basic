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

import string


class Alphabet:

    def __init__(self, language):
        self.language = str.lower(language)
        if 'eng' in self.language:
            self.letters = list(string.ascii_lowercase)
        if 'ua' in self.language or 'ukr' in self.language:
            self.letters = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
        if 'ru' in self.language:
            self.letters = [chr(i) for i in range(ord('а'),  ord('а')+6)] + [chr( ord('а')+33)] + \
                           [chr(i) for i in range(ord('а')+6,  ord('а')+32)]

    def show_letters(self):
        print(self.letters)

    def len_alphabet(self):
        print(len(self.letters))

    def char_in_alphabet_check(self, char):
        return str.lower(char) in self.letters


rus_alpha = Alphabet('ru')
print(rus_alpha.char_in_alphabet_check('I'))
rus_alpha.len_alphabet()
rus_alpha.show_letters()

en_alpha = Alphabet('English')
print(en_alpha.char_in_alphabet_check('i'))
en_alpha.len_alphabet()
en_alpha.show_letters()

ua_alpha = Alphabet('Ukrain')
print(ua_alpha.char_in_alphabet_check('i'))
ua_alpha.len_alphabet()
ua_alpha.show_letters()
