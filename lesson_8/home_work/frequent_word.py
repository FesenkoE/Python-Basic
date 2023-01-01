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


def main():
    text = "hi world, hi python. i am am am very cool but i am still learning."
    print(frequent_word(text))

    assert frequent_word(text) == "am"
    assert frequent_word('i very very very cool but i am still learning') == "very"


def frequent_word(text):
    some_world = ''
    word_list = []
    fr_word = ''

    for char in text:
        if char.isalnum():
            some_world += char
        elif (not char.isalnum()) and len(some_world) > 0:
            word_list.append(some_world)

            if word_list.count(some_world) > word_list.count(fr_word):
                fr_word = some_world

            some_world = ''

    return fr_word


if __name__ == '__main__':
    main()