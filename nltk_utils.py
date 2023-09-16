import nltk
from nltk.stem import PorterStemmer
import numpy as np

stemmer = PorterStemmer()

def tokenize(sentence: str) -> list:
    """Tokenize the sentence"""
    return nltk.tokenize.word_tokenize(sentence)
def stem(word: str) -> any:
    """"""
    return stemmer.stem(word)
def bag_of_words(tokenized_sentence: list, words: list):
    """
    return bag of words array
    example:
        ...
    """
    sentence_words = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1
    return bag
