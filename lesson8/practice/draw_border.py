"""
    1. Нарисовать границу из * в списке.

    [in]    ['python',
             'django']

    [out]   ['********',
             '*python*',
             '*django*',
             '********']

    [in]    ['abc',
             'def']

    [out]   ['******',
             '*abc*',
             '*def*',
             '*****']

    Покрыть несколькими тестами.
"""
import math


def draw_border(lst_):
    max_len = max([len(x) + 2 for x in lst_])
    new_lst = ['*' * max_len]
    for i in lst_:
        star_first = math.ceil((max_len - len(i)) / 2)
        star_last = max_len - len(i) - star_first
        new_str = f'{"*" * star_first}{i}{"*" * star_last}'
        new_lst.append(new_str)
    new_lst.append('*' * max_len)
    print(new_lst)
    return new_lst


assert draw_border(['qwe', 'asdf', 'zxcvb']) == ['*******', '**qwe**', '**asdf*', '*zxcvb*', '*******']
assert draw_border(['0', '', '1']) == ['***', '*0*', '***', '*1*', '***']
assert draw_border(['000000', '0', '1g']) == ['********', '*000000*', '****0***', '***1g***', '********']
