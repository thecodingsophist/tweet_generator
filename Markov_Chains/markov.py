from dictogram import Dictogram
import sys
import random
from random_sampling import random_sampling

class MarkovChain:

    def build_markov(self):

        with open(sys.argv[1]) as f:
            content = f.read().split()

        dict = {}

        i=0
        while i+1 < len(content):
            word = content[i]
            if dict.get(word) == None:
                next_word = content[i+1]
                list = [next_word]
                histogram = Dictogram(list)
                dict[word] = histogram
            else:
                next_word = content[i+1]
                dict.get(word).add_count(next_word)
            i += 1

        return dict

    def random_walk(self, dict):
        random_walk = ""
        list_of_keys = list(dict.keys())
        chosen_number = random.randint(0, len(list_of_keys)-1)
        chosen_word = list_of_keys[chosen_number]
        random_walk = random_walk + chosen_word

        for _ in range(0,20):
            dictogram = dict.get(chosen_word)
            new_word = random_sampling(dictogram)
            random_walk = random_walk +" "+ new_word
            chosen_word = new_word

        print(random_walk)
        return random_walk

    def second_order(self):

        with open(sys.argv[1]) as f:
            content = f.read().split()

            dict = {}
        i=0

        while i+2 < len(content):
            word_tuple = (content[i], content[i+1])
            if dict.get(word_tuple) == None:
                next_word = content[i+2]
                list = [next_word]
                histogram = Dictogram(list)
                dict[word_tuple] = histogram
            else:
                next_word = content[i+2]
                dict.get(word_tuple).add_count(next_word)
            i += 1

        return dict

    def second_order_random_walk(self, dict):
        random_walk = ""
        list_of_keys = list(dict.keys())
        chosen_number = random.randint(0, len(list_of_keys)-1)
        chosen_tuple = list_of_keys[chosen_number]
        random_walk = random_walk + chosen_tuple[0] + chosen_tuple[1]

        for _ in range(0,40):
            dictogram = dict.get(chosen_tuple)
            new_word = random_sampling(dictogram)
            random_walk = random_walk +" "+ new_word
            chosen_tuple = (chosen_tuple[1], new_word)

        print(random_walk)
        return random_walk


if __name__ == '__main__':
    markov = MarkovChain()
    # dict = markov.build_markov()
    # markov.random_walk(dict)
    dict = markov.second_order()
    markov.second_order_random_walk(dict)
