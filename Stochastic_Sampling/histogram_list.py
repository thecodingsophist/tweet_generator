import random
import sys

class Histogram_List:
    def histogram(self):
    #take in the words from story file
        with open(sys.argv[1]) as f:
            content = f.read().split()
        #make a dictionary of words
        current_word = content[0]

        word_list = []
        word_list.append([current_word, 1])

        for i in range(1, len(content)):
            current_word = content[i]
            word_found = False
            for j in range(0, len(word_list)):
                if current_word == word_list[j][0]:
                    word_list[j][1] += 1
                    word_found = True

            if not word_found:
                word_list.append([current_word, 1])
        # for i in range(1, len(content)):
        #     if content[i] in word_list:
        #         word_list[i][1] += 1
        #     else:
        #         word_list.append([content[i],1])
        #
        # print("FOR I IN RANGE")
        # word_chunk = content[i]
        # for j in range(0, len(word_list)):
        #     # print("FOR J IN RANGE")
        #     # print("word_chunk = " + word_chunk)
        #     # print(len(word_list))
        #     print(word_list)
        #     print("###############word chunk = " + word_chunk)
        #     print("###########word_list_word = " + word_list[j][0])
        #     if word_chunk == word_list[j][0]:
        #         print("if")
        #         word_list[j][1] = word_list[j][1] + 1
        #     else:
        #         print("else")
        #         word_list.append([word_chunk, 1])
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
    text = Histogram_List()
    text.histogram()
    # text.unique_words()
    # text.frequency("she")
