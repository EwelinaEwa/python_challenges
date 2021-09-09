def encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if count == 1:
                encoding += prev_char
            else:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        if count == 1:
            encoding += prev_char
        else:
            encoding += str(count) + prev_char
        return encoding


def decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            if count == "":
                count = 1
            decode += char * int(count)
            count = ''
    return decode

