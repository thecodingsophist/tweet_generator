def reverse_sentence(word_string):
    new_word_string = ""
    word_string_split = word_string.split()
    i=0
    while i < len(word_string_split):
        new_word_string += word_string_split[len(word_string_split)-(i+1)] + " "
        i += 1
    return new_word_string

if __name__ == '__main__':
    print(reverse_sentence("hello 2day osby wonkadamaloon lol hahaha"))
