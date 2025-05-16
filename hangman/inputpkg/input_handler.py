def select_difficulty():
    while True:
        difficulty = input("난이도를 선택하세요 (easy, normal, hard): ").lower()
        if difficulty in ["easy", "normal", "hard"]:
            return difficulty
        print("잘못된 입력입니다. 다시 입력하세요.")

def ask_restart():
    while True:
        response = input("게임을 다시 시작하시겠습니까? (y/n): ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("y 또는 n으로 입력하세요.")

def get_user_input(used_letters):
    while True:
        letter = input("글자를 입력하세요: ").lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in used_letters:
                print("이미 입력한 글자입니다.")
            else:
                return letter
        else:
            print("한 글자의 알파벳을 입력하세요.")