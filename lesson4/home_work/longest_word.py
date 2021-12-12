"""
    Вводится строка.

    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""

string = input("Enter a string: ")
counter = 0
word = ''
longest_word = ''

for char in string:
    if char.isalpha():
        word += char
    else:
        if len(word) > len(longest_word):
            longest_word = word
        counter += 1
        word = ''
else:
    if word:
        counter += 1
    if len(word) > len(longest_word):
        longest_word = word

print(f'Len of string is: {counter}')
print(f'longest word is: {longest_word}')

