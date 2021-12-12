"""
    Для определения строки используются "", '', '''''', """ """

    В одинарных кавычках или апострофах можно написать только 1 строку,
    а в тройных - много строк, как например этот комментарий.
"""

str_1 = 'python is the best language'
str_2 = """python
            is
                the best
                    language
"""
str_3 = '"python" is the best language'
str_4 = "\"python\" is the best language"

print('str_1', str_1)
print('str_2', str_2)
print('str_3', str_3)
print('str_4', str_4)

# \n - перевод строки
# \t - табуляция

str_5 = '\tHello\nworld!'
print('str_5', str_5)


# префиксы r (сырая строка), f (форматированная строка), b (бинарная строка)
str_6 = r'\tHello\nworld!'
print('str_6', str_6)


# Варианты описания длинной строки в коде.
str_7 = '"python" is the best language "python" is the best language "python" is the best language "python" is the best language "python" is the best language'  # noqa: E501

# Можно конкатенировать строки и использовать перенос строки в коде - \
str_8 = '"python" is the best language "python" is the best language ' \
    + '"python" is the best language "python" is the best language ' \
    + '"python" is the best language'

# Объединить строки в одну с помощью () - Рекомендуется
str_9 = (
    '"python" is the best language "python" is the best language '
    '"python" is the best language "python" is the best language '
    '"python" is the best language'
)

print('str_7 == str_8 == str_9', str_7 == str_8 == str_9)  # True

# В данном варианте строка будет содержать символы переноса строки
str_10 = """"python" is the best language "python" is the best language
"python" is the best language "python" is the best language
"python" is the best language
"""

print('str_9 == str_10', str_9 == str_10)  # False
