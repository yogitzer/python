def check_letter_in_word(letter, word):
    return letter in word

def check_game_over(word, guessed_letters, remaining_attempts):
    if remaining_attempts == 0:
        return True, False  # 게임 종료, 실패
    if all(ch in guessed_letters for ch in word):
        return True, True  # 게임 종료, 성공
    return False, False  # 계속 진행