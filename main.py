import random
import os
from colorama import init, Fore, Style

from hangman.inputpkg.input_handler import select_difficulty, ask_restart, get_user_input
from hangman.outputpkg.output_handler import (
    display_word_length,
    display_current_word,
    display_used_letters,
    display_remaining_attempts,
    draw_game_result,
)
from hangman.corepkg.word_selector import choose_random_word
from hangman.corepkg.logic import check_letter_in_word, check_game_over
from hangman.corepkg.repository import word_list_easy, word_list_normal, word_list_hard, hangman_pics
from hangman.corepkg.utils import clear_screen

# 윈도우에서 colorama 초기화
init()

def play_game():
    clear_screen()
    difficulty = select_difficulty()
    word = choose_random_word(difficulty)
    guessed_letters = set()
    used_letters = set()
    remaining_attempts = 6

    display_word_length(word)

    while True:
        display_current_word(word, guessed_letters)
        display_used_letters(used_letters)
        display_remaining_attempts(remaining_attempts)

        guess = get_user_input(used_letters)
        used_letters.add(guess)

        if check_letter_in_word(guess, word):
            guessed_letters.add(guess)
        else:
            remaining_attempts -= 1

        over, success = check_game_over(word, guessed_letters, remaining_attempts)
        if over:
            draw_game_result(word, success)
            break

    if ask_restart():
        play_game()

if __name__ == "__main__":
    play_game()