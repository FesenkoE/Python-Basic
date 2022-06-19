"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""
my_str = input('Введите строку:')
count_word = 0
word_collect = ''
max_len_word = ''
last_char = ''
for char in my_str:
    if char.isalpha():
        word_collect += char  # Если Char буква алфавита собираем слово
        if not last_char.isalpha():  # если Char, а предыдущая была не буква - началось новое слово
            count_word += 1
    last_char = char  # текущий символ становится предидущим символом

    if len(max_len_word) < len(word_collect):
        max_len_word = word_collect  #если длинное слово короче нового, присваиваем новое слово

    if not char.isalpha():
        word_collect = ''  # обнуляем собератель слова


print(f'Колличество слов: {count_word}.\n'
      f'Самое длинное слово: {max_len_word}.\n'
      f'Его длина: {len(max_len_word)} символов.')

