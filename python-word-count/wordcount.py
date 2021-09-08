import re


def word_count(text):
    text = re.sub('[^0-9a-zA-ZА-я]+', ' ', text)
    new_text = ""
    for char in text:
        new_text += char.lower()
    text_list = new_text.split()
    text_dictionary = {}
    for word in text_list:
        text_list.count(word)
        text_dictionary[word] = text_list.count(word)
    return text_dictionary


#     print(text_list)
#     print(text_dictionary)
#
# word_count("rah rah ah ah ah\nroma roma ma\n"
#                        "ga ga oh la la\nwant your bad romance")
