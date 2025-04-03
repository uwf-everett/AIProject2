import pandas as pd
from collections import defaultdict
import random

class TextGenerator:
    def __init__(self):
        self.corpus = pd.read_pickle("corpus.pkl")
        self.markov_chain = self._create_chain(self.corpus)

    #creates the markov chain dictionary
    def _create_chain(self, text):
        words = list(text)

        dictionary = defaultdict(list)

        for current_word, next_word in zip(words[0:-1], words[1:]):
            dictionary[current_word].append(next_word)

        dictionary = dict(dictionary)

        return dictionary
        
    #generates sentance based off starter word and length
    def generate(self, starter_word, length):
        word1 = starter_word
        sentence = word1.capitalize()

        for i in range(length - 1):
            word2 = random.choice(self.markov_chain[word1])
            word1 = word2
            sentence += ' ' + word2

    
        sentence += '.'
        return sentence