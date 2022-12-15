from Apps.Utils import checkData
from games import CurrencyRouletteGame, MemoryGame, GuessGame


def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).')
    print('Here you can find many cool games to play.\n\n')


def load_game():
    while True:
        choose_game = input('''
        Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        ''')
        if checkData(choose_game, 1, 3):
            # if choose_game.isdigit():
            #     if 1 <= int(choose_game) <= 3:
            choose_game = int(choose_game)
            break

    while True:
        level_difficulty = input('Please choose game difficulty from 1 to 5:\n\n')
        if level_difficulty.isdigit():
            if 1 <= int(choose_game) <= 5:
                level_difficulty = int(level_difficulty)
                break

    if choose_game == 1:
        MemoryGame.play(int(level_difficulty))
    if choose_game == 2:
        GuessGame.get_guess_from_user(int(level_difficulty))
    if choose_game == 3:
        CurrencyRouletteGame.play(int(level_difficulty))
