import random

from Apps.Utils import checkData


def generate_number(level_difficulty):
    randomNumber = random.randint(1, level_difficulty)
    print(f'The random number is : {randomNumber}')


def get_guess_from_user(level_difficulty):
    while True:
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
        return True
    else:
        return False
