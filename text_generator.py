import pandas as pd

class TextGenerator:
    def __init__(self):
        self.corpus = pd.read_pickle("corpus.pkl")