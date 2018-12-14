import random
import sys

class Histogram_Dictionary:
    def histogram(self):
    #take in the words from story file
        with open(sys.argv[1]) as f:
            content = f.read().split()
        #make a dictionary of words
        word_list = {}
        for word_chunk in content:
            if word_chunk in word_list:
                word_list[word_chunk] += 1
            else:
                word_list[word_chunk] = 1
        print(word_list)
        return word_list

    def unique_words(self):
        #counts the number of unique words from histogram
        print(len(self.histogram()))

    def frequency(self, word):
        print(self.histogram().get(word))

if __name__ == '__main__':
    text = Histogram_Dictionary()
    # text.histogram()
    # text.unique_words()
    text.frequency("she")
