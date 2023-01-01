import json

# json.dumps(dict) для записи
# json.load(file) для чтения

a = [
    {"short": "dict", "long": "dictionary"},
    {"short": "dict", "long": "dictionary"},
    {"short": "dict", "long": "dictionary"},
    {"short": "dict", "long": "dictionary"},
]


# запись
with open("test.json", "w") as f:
    data = json.dumps(a, indent=4)
    print(data, type(data))
    f.write(data)


# чтение
with open("test.json") as f:
    data = json.load(f)
    print(data, type(data))
