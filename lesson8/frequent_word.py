"""
    Реализуйте функцию, которая принимает текст и возвращает слово, которое
    в этом тексте встречается чаще всего.

    Напишите несколько тестов для функции.

    # Если таких слов несколько - приоритет у первого, если расположить список
    # в алфавитном порядке.
    # Например:
    text = "hi world, hi python. i am very cool but i am still learning."
    # чаще всего встречаются "hi", "i" и "am", но по алфавиту "am" - раньше
    assert frequent_word(text) == "am"

"""
import re


def frequent_word(text: str):
    list_word = re.findall(r'\w*', text)
    while '' in list_word:
        list_word.remove('')
    count_word = dict.fromkeys(list_word, 0)
    for word in list_word:
        count_word[word] += 1
    max_value = max(count_word.values())
    word = []
    for key, value in count_word.items():
        if value == max_value:
            word.append(key)
    return min(word)


def main():
    frequent_word("hi world, hi python. i am very cool but i am still learning.")


if __name__ == '__main__':
    main()


assert frequent_word("hi world, hi python. i am very cool but i am still learning.") == 'am'
assert frequent_word("asd asd asd qwe,qwe,qwe,qwe zxc") == 'qwe'
assert frequent_word("qw1 qw1 qw1 sdf fg gf,g,g.dfg") == 'qw1'
