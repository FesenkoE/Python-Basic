"""
    Константы принято именовать заглавными буквами.
    Шаблоны сообщений, пароли, ключи достпов и т.д. можно относить к константам
"""

HELLO_TEMPLATE = 'Hello, {name}!'
INFO_TEMPALTE = '{name} from {city}. He is {age}.'
BYE_TEMPLATE = 'Goodbye, {name}!'

SUCCESS_REG_MESSAGE = """
Hello {name}!

Congratulations on your successful registration on our portal!

Your login details:
    login: {login}
    password: {password}
    backup email: {email}

Best regards, ABC!
"""

# Как использовать

print(HELLO_TEMPLATE.format(name='John'))
print(INFO_TEMPALTE.format(name='John', city='Kiev', age=21))
print(BYE_TEMPLATE.format(name='John'))

print(HELLO_TEMPLATE.format(name='Elizabeth'))

message = SUCCESS_REG_MESSAGE.format(
    name='Max',
    login='supermax777',
    password='supersecret',
    email='max@mail.com'
)

print(message)
