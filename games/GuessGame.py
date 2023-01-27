import random

from Score.Score import add_score
from Utilities.Utils import checkData, Screen_cleaner


def get_guess_from_user(level_difficulty):
    while True:
        Screen_cleaner()
        print(f'Please choose number between 1 to {level_difficulty}')
        numberFromUser = input('What is your number ?')
        if checkData(numberFromUser, 1, 5):
            # if numberFromUser.isdigit():
            #     if 1 <= int(numberFromUser) <= 5:
            numberFromUser = int(numberFromUser)
            break

    generate_number(level_difficulty)
    compare_results(int(numberFromUser), level_difficulty)


def compare_results(numberFromUser, level_difficulty):
    if numberFromUser == level_difficulty:
        add_score(level_difficulty)
        return True
    else:
        return False


def generate_number(level_difficulty):
    randomNumber = random.randint(1, level_difficulty)
    print(f'The random number is : {randomNumber}')
