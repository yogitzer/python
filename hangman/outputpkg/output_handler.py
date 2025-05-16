from colorama import Fore, Style
from hangman.corepkg.repository import hangman_pics

def display_word_length(word):
    print(f"\n단어는 {len(word)}글자입니다.\n")

def display_current_word(word, guessed_letters):
    display = " ".join([ch if ch in guessed_letters else "_" for ch in word])
    print(f"\n단어: {Fore.GREEN}{display}{Style.RESET_ALL}")

def display_used_letters(used_letters):
    print(f"입력한 글자들: {Fore.YELLOW}{' '.join(sorted(used_letters))}{Style.RESET_ALL}")

def display_remaining_attempts(remaining):
    print(f"{Fore.CYAN}남은 기회: {remaining}{Style.RESET_ALL}")
    print(hangman_pics[6 - remaining])  # 그림 출력

def draw_game_result(word, success):
    if success:
        print(f"{Fore.GREEN}축하합니다! 단어를 맞추셨습니다: {word}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}실패! 정답은 {word}였습니다.{Style.RESET_ALL}")