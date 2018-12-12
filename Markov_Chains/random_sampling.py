import random
import sys

def random_sampling(histogram):
    #method/question: why don't we just take a random word from the original text?
    word_count = 0
    for word in histogram:
        word_count += histogram[word]
    chosen = random.randint(0, word_count-1)
    # print("chosen = " + str(chosen))

    #returns the chosen word
    word_number = 0
    for word in histogram:
        word_number += histogram[word]
        if chosen < word_number:
            break
    return word

def random_sampling_test(histogram, num_runs):
    runs = 0
    random_sampling_count = {}
    while runs < num_runs:
        word = random_sampling(histogram)
        if word in random_sampling_count:
            random_sampling_count[word] += 1
        else:
            random_sampling_count[word] = 1
        runs += 1
    print(random_sampling_count)
    return random_sampling_count


if __name__ == '__main__':

    seuss = {
        "one": 1,
        "fish": 4,
        "red": 1,
        "blue": 1
    }

    random_sampling_test(seuss, 10000)
