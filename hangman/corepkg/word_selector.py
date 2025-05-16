import random
from hangman.corepkg.repository import word_list_easy, word_list_normal, word_list_hard

def choose_random_word(difficulty):
    if difficulty == "easy":
        return random.choice(word_list_easy)
    elif difficulty == "normal":
        return random.choice(word_list_normal)
    elif difficulty == "hard":
        return random.choice(word_list_hard)