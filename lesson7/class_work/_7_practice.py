"""
    Через пробел вводятся слова.
    1. Сформировать список.
    2. Найти самое длинное и самое короткое слово списка.
    3. Поменять их местами.
    4. Вывести в консоль: исходный список, найденные слова, итоговый список.
"""

# 1.
# Формируем список разбивая введенную строку по пробелу методом split()
word_list = input("Введите слова через пробел: ").split()


# 2.
# Создаем переменные для длинног ои короткого слова. Помещаем туда первое слово
longest_word = shortest_word = word_list[0]

# Тогда циклом проходим начиная со второго слова списка
for word in word_list[1:]:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word


# 3.
# Находим индексы слов в списке
l_idx = word_list.index(longest_word)
s_idx = word_list.index(shortest_word)

# Создаем копию исходного списка
final_list = word_list.copy()

# В копии производим замену двух элементов местами
final_list[l_idx], final_list[s_idx] = final_list[s_idx], final_list[l_idx]


# 4.
print(
    f"Исходный список: {word_list}\n"
    f"Самое длинное слово: {longest_word}\n"
    f"Самое короткое слово: {shortest_word}\n"
    f"Итоговый список: {final_list}"
)
