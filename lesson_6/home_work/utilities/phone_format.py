def get_phone_number(line):
    prepare_phone_number = ''

    for digit in line:
        if digit.isdigit():
            prepare_phone_number += digit

    return '+38' + prepare_phone_number[-9:]
