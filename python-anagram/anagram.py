def detect_anagrams(word, list):
    match = []
    sorted_word = sorted(word.lower())
    for item in list:
        sorted_item = sorted(item.lower())
        if word == item:
            match = []
            break
        elif sorted_item == sorted_word:
            match.append(item)
    return match


# detect_anagrams('ant', 'tan stand at'.split())
