def count_words(text):
    return len(text.split())

def count_char(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count
