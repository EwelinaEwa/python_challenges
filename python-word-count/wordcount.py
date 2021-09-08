def word_count(text):
    new_text = ""
    for char in text:
        if char == " " or char.isalnum():
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
# word_count("One fish#$% two fish red fish %^#$ blue fish")
