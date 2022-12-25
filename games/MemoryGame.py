import time

from Score import add_score
from Utilities.Utils import checkData
from Utilities.Utils import Screen_cleaner

start = time.time()
import random


def play(level_difficulty):
    Screen_cleaner()
    arrFromUser = []
    arrGenerate = []

    #   func to get randomize number
    roundNumber = level_difficulty
    while roundNumber >= 1:
        arrGenerate.append(generate_sequence())
        roundNumber -= 1
    #   func to get numbrs from user
    roundNumber = level_difficulty
    while roundNumber >= 1:
        arrFromUser.append(get_list_from_user())
        roundNumber -= 1

    print(arrFromUser)
    print(arrGenerate)
    #   func to equal between 2 arrays
    is_list_equal(arrFromUser, arrGenerate, level_difficulty)


def get_list_from_user():
    while True:
        print('Please choose number between 1 to 101')
        numberFromUser = input('What is your number ?')
        if checkData(numberFromUser, 1, 101):
            # if numberFromUser.isdigit():
            #     if 1 <= int(numberFromUser) <= 101:
            return int(numberFromUser)
            break


def generate_sequence():
    randomNumber = random.randint(1, 101)
    print(randomNumber)
    Screen_cleaner()
    return int(randomNumber)


def is_list_equal(numberFromUser, randomNumber, level_difficulty):
    if numberFromUser == randomNumber:
        add_score(level_difficulty)

        # print('OK')
        return True
    else:
        # print('Bad')
        return False
