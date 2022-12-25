from currency_converter import CurrencyConverter
import random
from Score import add_score

from Utilities.Utils import checkData, Screen_cleaner


def play(level_difficulty):
    return get_guess_from_user(level_difficulty)


def get_money_interval(numberFromUser, level_difficulty, amountOfDollar):
    c = CurrencyConverter()
    amount = amountOfDollar
    from_currency = 'USD'
    to_currency = 'ILS'
    print(from_currency, " To ", to_currency, amount)
    result: float = c.convert(amount, 'USD', 'ILS')
    print(result)

    if result - level_difficulty < numberFromUser < result + level_difficulty:
        add_score(level_difficulty)
        return True
    else:
        return False


def get_guess_from_user(level_difficulty):
    Screen_cleaner()
    amountOfDollar = random.randint(1, 100)
    print(f'The  Amount Of Dollar is : {amountOfDollar}')

    while True:
        print('Please guess the number of the change ')
        numberFromUser = input('How much do you think it ?')
        if checkData(numberFromUser, 1, 10000):
            # if numberFromUser.isdigit():
            #     if 1 <= int(numberFromUser) <= 10000:
            get_money_interval(int(numberFromUser), level_difficulty, amountOfDollar)
            break

# get_money_interval()
