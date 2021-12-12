"""
    Операции со строками
"""

a = 'Hello'
b = 'world'

# Конкатенация (объединение) строк
print(a + b)  # Helloworld

# Дублирование строк
print(a * 10)  # HelloHelloHelloHelloHelloHelloHelloHelloHelloHello

# функция len() возвращает длину строки
print(len(a))  # 5

# Сравнивание строк (сравниваются уникальные коды символов по порядку)
print('abcd' > 'abc')  # True
print('ABC' > 'a')  # False

# Чтобы узнать уникальный код - функция ord
print(ord('A'))  # 65
print(ord('a'))  # 97

# Обратная функция chr - получить символ из кода
print(chr(97))  # 'a'

# Оператор in и not in. Нужен для проверки вхождения подстроки в строку
print('ello' in a)  # True
print('worl' not in b)  # False
