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

        for _ in range(0,10):
            dictogram = dict.get(chosen_word)
            new_word = random_sampling(dictogram)
            random_walk = random_walk +" "+ new_word
            chosen_word = new_word

        print(random_walk)
        return random_walk

if __name__ == '__main__':
    markov = MarkovChain()
    dict = markov.build_markov()
    markov.random_walk(dict)
