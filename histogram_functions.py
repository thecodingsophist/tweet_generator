import random
import sys

class Histogram:
    def histogram(self):
    #take in the words from story file
        with open('P&P_chapter1_sample_text.txt') as f:
            content = f.read().split(' ')
            #FIXME: clean text such that words separated by new lines are two different strings
            for word_chunk in content:
                word_chunk.split('\n')
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
    text = Histogram()
    # text.histogram()
    # text.unique_words()
    text.frequency("she")
