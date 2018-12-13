# reverse_words.py
def reverse_words(word):
    new_word = ""
    i = 0

    while i < len(word):
        last_letter = len(word) - (i+1)
        new_word += word[last_letter]
        i += 1

    return new_word


if __name__ == '__main__':
    print(reverse_words("hello"))
