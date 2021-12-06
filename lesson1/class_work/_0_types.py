"""
    Основные типы данных Python
    примеры в формате:
        инструкция    # результат
        print(4)      # 4
"""

print("Hello world!")
print(type("Hello world!"))  # <class 'str'>

print(4)
print(type(4))  # <class 'int'>

print(4.5)
print(type(4.5))  # <class 'float'>

print([1, 2, 3, "hello"])
print(type([1, 2, 3, "hello"]))  # <class 'list'>

print((1, 2, 3, "hello"))
print(type((1, 2, 3, "hello")))  # <class 'tuple'>

print({5, 2, 2, 3, 3, 1})  # {1, 2, 3, 5}
print(type({5, 2, 2, 3, 3, 1}))  # <class 'set'>

print({"age": 21})
print(type({"age": 21}))  # <class 'dict'>
