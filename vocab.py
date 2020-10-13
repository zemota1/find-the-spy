import random

def get_word(filename="/home/josemota/projects/find-the-spy/vocab.txt"):
    f = open(filename, "r")

    all_words = f.read().split("\n")
    filtered = [word for word in all_words if (len(word) > 3)]
    chosen_word = random.choice(filtered)
    return chosen_word

