from random import choice


def gen_password(chars, length=8):
    """Password generator

    Args:
        chars (str): character set to generate
        length (int, optional): length of generated password. Defaults to 8.

    Returns:
        str: generated password
    """
    password = ""
    for i in range(length):
        password += choice(chars)
    return password
