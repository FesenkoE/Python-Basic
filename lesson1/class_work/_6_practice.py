"""
    Найти суму цифр двузначного числа.
    пр: 14 => 1 + 4 = 5
"""

# получаем значение из input, приводим в int и записываем в переменную number
number = int(input("Enter two-digit number: "))

result = number // 10 + number % 10

print("Result:", result)
