import json
import random

from marisa_trie import Trie

with open("dictionary/jaro-winkler.json") as f:
    jaro_winkler_dict = json.load(f)
jaro_winkler = Trie(jaro_winkler_dict.keys())

with open("dictionary/hamming.json") as f:
    hamming_dict = json.load(f)
hamming = Trie(hamming_dict.keys())


def replace_similar_word(word, distance):
    if distance == "jaro-winkler":
        if word in jaro_winkler:
            return random.choice(jaro_winkler_dict[word])
    elif distance == "hamming":
        if word in hamming:
            return random.choice(hamming_dict[word])
    return word


def replace_word_noiser(text):
    text_split = text.split()
    for i, word in enumerate(text_split):
        random_choice = random.random()
        if random_choice > 0.5:
            text_split[i] = replace_similar_word(word, distance="jaro-winkler")
    return " ".join(text_split)


print(replace_word_noiser("I want my drink"))
