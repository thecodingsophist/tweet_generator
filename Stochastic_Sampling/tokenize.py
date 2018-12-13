import sys

class Tokenize:

    def tokenize(self):
        with open(sys.argv[1]) as f:
            content = f.read().split()
        return content

    def tokenize_unique_words(self):
        with open(sys.argv[1]) as f:
            content = f.read().split()
        word_list = []
        i=0
        while i < len(content):
        # for word in content:
        #     if word not in word_list:
        #         word_list.append(word)
            # print(len(content))
            # print(content[i])
            if content not in word_list:
                word_list += content
            i+=1
        # print(content)
        # print(word_list)
        return word_list

if __name__ == '__main__':
    tokens = Tokenize()
    tokens.tokenize()
