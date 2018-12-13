import tokenize

class Word_Count:
    def count(self):
        #make a dictionary of words
        token = Tokenize()
        content = token.tokenize()
        histogram = {}
        for word_chunk in content:
            if word_chunk in histogram:
                histogram[word_chunk] += 1
            else:
                histogram[word_chunk] = 1
        # print(histogram)
        return histogram

if __name__ == '__main__':
    words = Word_Count()
    words.count()      
