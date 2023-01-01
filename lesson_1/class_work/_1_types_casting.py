"""
    Основные функции приведения типов Python
    str
    int
    float
"""

a = "3.14"
print(a, type(a))  # 3.14 <class 'str'>

b = float(a)
print(b, type(b))  # 3.14 <class 'float'>

c = int(b)
print(c, type(c))  # 3 <class 'int'>

d = str(c)
print(d, type(d))  # 3 <class 'str'>
