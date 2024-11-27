
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) == 1:
        return first

    else:
        if len(str_number) > 1 and str_number[-1] == '0':
            str_number = str_number[:-1]
        if len(str_number) == 1:
            return first
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(3303))
print(get_multiplied_digits(330))
print(get_multiplied_digits(30))