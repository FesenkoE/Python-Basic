"""
    1. Напишите функцию, которая принимает текст и
    возвращает информацию о том, сколько раз в тексте встречается каждый символ
    в виде словаря.

    2. Напишите пару тестов к функции.
"""


def dict_counter(text):
    data = {}

    for char in text:
        if char not in data:
            data[char] = text.count(char)

    return data


text = (
    "Proin laoreet dui vel libero dapibus vehicula vitae eget turpis."
    "Nam non eros eu elit posuere posuere id ac turpis."
    "Quisque nec orci blandit, lobortis felis non, eleifend felis."
    "Vivamus at odio at lacus viverra luctus et ut mauris."
    "Etiam vehicula nibh eu quam feugiat tempus."
)
assert dict_counter(text)["P"] == 1
assert dict_counter(text)["i"] == 25
assert dict_counter("a,a,a,a")["a"] == 4


"""
    Напишите функцию, которая принимает текст и возвращает информацию о том,
    сколько в тексте согласных (consonant) и гласных (vowel) букв.
"""

# Создаем список с гласными (потому что их меньше)
vowel_chars = ["a", "e", "i", "o", "u", "y"]


def dict_counter(text):
    counter = {"vowel": 0, "consonant": 0}
    # counter = dict.fromkeys(['vowel', 'consonant'], 0)
    for char in text:
        if char in vowel_chars:  # если есть в списке - гласная
            counter["vowel"] += 1
        elif char.isalpha():  # иначе - согласная
            counter["consonant"] += 1
    return counter


print(dict_counter(text))
