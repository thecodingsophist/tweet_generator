import random
import sys

def dictionary_words():
#take input the number of words that will be chosen from the dictionary
    read_in = sys.argv
    input_number = read_in[1]
#take in the words from dictionary words file
    with open('/usr/share/dict/words') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
#shuffle the entire file
        random.shuffle(content)
#select the number of words that was previously indicated
    random_words = content[0:int(input_number)]
    random_words_string = ""
    for word in random_words:
        random_words_string += word + " "
    print random_words_string

if __name__ == '__main__':
    dictionary_words()
