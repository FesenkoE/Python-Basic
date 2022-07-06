"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.

    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""

# Ниже описаны некоторые варианты решения задачи.


def longest_strings(list_in):
    """ Функция возвращает список самых длинных строк из списка list_in """
    max_length = 0  # в переменной будет храниться длина самой длинной строки
    for i in list_in:
        if len(i) > max_length:
            max_length = len(i)
    return [i for i in list_in if len(i) == max_length]


def longest_strings(list_in):
    """ Функция возвращает список самых длинных строк из списка list_in """
    return [i for i in list_in if len(i) == len(max(list_in, key=len))]


def longest_strings(list_in):
    """ Функция возвращает список самых длинных строк из списка list_in """
    ml = max(len(s) for s in (list_in))
    result = [s for s in list_in if len(s) == ml]
    return result


def longest_strings(list_in):
    """ Функция возвращает список самых длинных строк из списка list_in """
    list_out = []
    max_len = len(max(list_in, key=len))

    for string in list_in:
        if max_len == len(string):
            list_out.append(string)

    return list_out


def longest_strings(list_in):
    """ Функция возвращает список самых длинных строк из списка list_in """
    longest_str = ""
    list_out = []
    for elem in sorted(list_in, key=len, reverse=True):
        if len(elem) >= len(longest_str):
            longest_str = elem
            list_out.append(longest_str)
    return list_out


def longest_strings(list):
    """ Функция возвращает список самых длинных строк из списка list_in """
    list_out = []
    for word in list:
        if len(word) == len(max(list, key=len)):
            list_out.append(word)
    return list_out


t_1 = ["x"]
assert longest_strings(t_1) == ["x"]

t_2 = ["abc", "eeee", "abcd", "dcd"]
assert longest_strings(t_2) == ["eeee", "abcd"]

t_3 = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
assert longest_strings(t_3) == ["zzzzzz", "abcdef", "aaaaaa"]

t_4 = ["enyky", "benyky", "yely", "varennyky"]
assert longest_strings(t_4) == ["varennyky"]

t_5 = ["abacaba", "abacab", "abac", "xxxxxx"]
assert longest_strings(t_5) == ["abacaba"]

print("All tests passed successfully!")
