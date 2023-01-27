import time
from os import system

SCORES_FILE_NAME = 'Score/Scores.txt'
BAD_RETURN_CODE: dict[str, str] = {"2001": "Cannot install requirements!",
                                   '3001': "cannot open playerdata.dat (scores file). check file exists/corrupted",
                                   "4001": "Game module doesn't contain an appropriate about() function. cannot add "
                                           "to menu module: ",
                                   "4002": 'Failed importing game module. check that game module is in the correct '
                                           'python format.',
                                   "4003": "Game module Play function is corrupted or doesnt exist. check game module: "}
Url = "http://localhost/score"

"""
   The function check get data from user, with upper limit and down limit 
   and check if the data from the user is between.
"""


def checkData(dataFromUser, limitDown, limitUp):
    if dataFromUser.isdigit():
        if limitDown <= int(dataFromUser) <= limitUp:
            return True
        else:
            return False


def Screen_cleaner():
    time.sleep(0.7)
    system('cls')
