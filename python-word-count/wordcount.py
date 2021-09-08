def word_count(text):
    text_list = text.split()
    text_dictionary = {}
    for word in text_list:
        text_list.count(word)
        text_dictionary[word] = text_list.count(word)
    return text_dictionary


    # # print(text_list)
    # print(text_dictionary)

# word_count("one fish two fish red fish blue fish")
