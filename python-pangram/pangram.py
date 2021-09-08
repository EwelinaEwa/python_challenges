import string

alphabet_string = string.ascii_lowercase
alphabet_list = []

for letter in alphabet_string:
    alphabet_list += letter

def is_pangram(text):
    for letter in text:
        if letter in alphabet_list:
            alphabet_list.remove(letter)
    if alphabet_list == []:
        return True
    else:
        return False
