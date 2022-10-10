import random
import string


def insert_char(word):
    """
    insert a random char or duplicate last char of a word ex.: "xám" -> "xámmm"
    """
    if random.random() < 0.5:
        return word + word[-1] * random.randint(1, 3)
    else:
        return word + random.choice(string.ascii_letters)

