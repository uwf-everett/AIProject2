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

        if not os.path.exists("corpus.pkl"):  # if pkl file does not exist, creates one
            self._generate_corpus_pkl()

        with open("corpus.pkl", "rb") as f:
            self.corpus = pickle.load(f)

        self.markov_chain = self._create_chain(self.corpus) # Builds the Markov chain fom the Brown corpus

    def _generate_corpus_pkl(self):   # Converts corpus into all lowercase and then into a pkl file
        print("Generating corpus.pkl from Brown corpus...")
        words = brown.words()
        words = [word.lower() for word in words if word.isalpha()]
        with open("corpus.pkl", "wb") as f:
            pickle.dump(words, f)
        print("corpus.pkl generated!")

    def _create_chain(self, text):   # Builds a Markov chain as a dictionary where each word maps to next possible word
        dictionary = defaultdict(list)
        for current_word, next_word in zip(text[:-1], text[1:]):
            dictionary[current_word].append(next_word)
        return dict(dictionary)

    def generate(self, starter_word, length): # This method generates the sentence that is output to the user
        word1 = starter_word.lower()

        if word1 not in self.markov_chain:
            return f"Sorry, '{starter_word}' is not in the corpus. Try another word."   # If user inputs word not in the corpus

        sentence = word1.capitalize()  # Begins generated sentence with capital letter

        for i in range(length - 1):   # Generates remaining words
            next_words = self.markov_chain.get(word1)
            if not next_words:
                break
            word2 = random.choice(next_words)
            sentence += ' ' + word2
            word1 = word2

        sentence += '.'
        return sentence
