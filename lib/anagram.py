# your code goes here!
words = ['enlists', 'google', 'inlets', 'banana', 'wow']

class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, r):
        match = []
        split_word_input = sorted(list(r))

        for word in words:
            if sorted(word) == split_word_input:
                match.append(word)
        return match


anagram = Anagram("word")
result = anagram.match("letsin")
print(result)