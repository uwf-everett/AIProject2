import os
import pickle
import random
from collections import defaultdict
import nltk
from nltk.corpus import brown

# Manually set the NLTK data path
nltk.data.path.append(os.path.join(os.getcwd(), "nltk_data"))

class TextGenerator:
    def __init__(self):
        # Ensure Brown corpus is downloaded into the custom directory
        try:
            nltk.data.find('corpora/brown')
        except LookupError:
            print("Downloading Brown corpus...")
            nltk.download('brown', download_dir='nltk_data')

        if not os.path.exists("corpus.pkl"):
            self._generate_corpus_pkl()

        with open("corpus.pkl", "rb") as f:
            self.corpus = pickle.load(f)

        self.markov_chain = self._create_chain(self.corpus)

    def _generate_corpus_pkl(self):
        print("Generating corpus.pkl from Brown corpus...")
        words = brown.words()
        words = [word.lower() for word in words if word.isalpha()]
        with open("corpus.pkl", "wb") as f:
            pickle.dump(words, f)
        print("corpus.pkl generated!")

    def _create_chain(self, text):
        dictionary = defaultdict(list)
        for current_word, next_word in zip(text[:-1], text[1:]):
            dictionary[current_word].append(next_word)
        return dict(dictionary)

    def generate(self, starter_word, length):
        word1 = starter_word.lower()

        if word1 not in self.markov_chain:
            return f"Sorry, '{starter_word}' is not in the corpus. Try another word."

        sentence = word1.capitalize()

        for i in range(length - 1):
            next_words = self.markov_chain.get(word1)
            if not next_words:
                break
            word2 = random.choice(next_words)
            sentence += ' ' + word2
            word1 = word2

        sentence += '.'
        return sentence
