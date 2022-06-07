"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

# Lorem Ipsum is simply dummy text of the printing industry.

str_ = input('Enter string: ')
word_counter = 0
word = 0
longest_word = 0

if str_:
    word_counter = 1

    for char in str_:
        if not char.isalnum():
            word_counter += 1
            word = 0
        else:
            word += 1
            longest_word = word if word > longest_word else longest_word

print(f'Words amount: {word_counter}')
print(f'Longest word: {longest_word}')