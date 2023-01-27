from Utilities.Utils import *
import os


def add_score(level_difficulty):
    """
        The function add score to txt file or create new score file.
    """
    if os.path.exists(SCORES_FILE_NAME):
        Point_of_winning = (level_difficulty * 3) + 5
        f = open(SCORES_FILE_NAME, "r")
        score_file = (f.read())
        f.close()
        new_total_score = int(score_file) + int(Point_of_winning)
        f = open(SCORES_FILE_NAME, "w")
        f.write(str(new_total_score))
        f.close()
        return new_total_score

    else:
        scores_file = open(SCORES_FILE_NAME, "w+")
        scores_file.write("0")
        scores_file.close()


def read_score_from_file():
    """
    Try to read from scores file
    :return: file object and current score if file exists
    """
    file = open(SCORES_FILE_NAME, 'r+')
    first_line = file.readline()
    current_score = int(first_line)
    return file, current_score
