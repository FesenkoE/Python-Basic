"""
    Реверс подстроки в ()

    Таким образом, чтоб:
    [in]    "(bar)"
    [out]   "rab"

    [in]    "foo(bar)baz"
    [out]   "foorabbaz"

    [in]    "foo(bar)baz(blim)"
    [out]   "foorabbazmilb"

    [in]    "foo(bar(baz))blim"
    [out]   "foobazrabblim"
    так как "foo(bar(baz))blim" -> "foo(barzab)blim" -> "foobazrabblim"

    Данные примеры можете использовать для написания тестов.
"""

import re

def reversed_brackets(text):
    while re.search('\(.*?\)', text):
        reply = re.search('\([^()]*?\)', text).group()[-2:0:-1]
        text = re.sub('\([^()]*?\)', reply, text, count=1)
    return text


print(reversed_brackets('foo(bar(baz))blim'))

assert reversed_brackets("(bar)") == 'rab'
assert reversed_brackets("foo(bar)baz") == "foorabbaz"
assert reversed_brackets("foo(bar)baz(blim)") == "foorabbazmilb"
assert reversed_brackets("foo(bar(baz))blim") == "foobazrabblim"