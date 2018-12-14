import random
import sys

class Histogram_Tuple:
    def histogram(self):
    #take in the words from story file
        with open(sys.argv[1]) as f:
            content = f.read().split()
        #make a dictionary of words
        current_word = content[0]

        word_list = []
        word_list.append((current_word, 1))

        for i in range(1, len(content)):
            current_word = content[i]
            word_found = False
            for j in range(0, len(word_list)):
                if current_word == word_list[j][0]:
                    current_freq = word_list[j][1]
                    word_list[j] = (current_word, current_freq + 1)
                    word_found = True

            if not word_found:
                word_list.append((current_word, 1))

        print(word_list)
        return word_list

    def unique_words(self):
        #counts the number of unique words from histogram
        print(len(self.histogram()))

    def frequency(self, word):
        i = 0
        while self.histogram()[i][0] != word:
            i += 1
        print(self.histogram()[i][0])

if __name__ == '__main__':
    text = Histogram_Tuple()
    text.histogram()
    # text.unique_words()
    # text.frequency("she")
