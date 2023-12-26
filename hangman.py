from random import choice

def select_word():
    with open ("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()

def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input