from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.Utils import checkData


def test_scores_service():

    my_driver = webdriver.Chrome(executable_path='d:\\chromedriver.exe')
    my_driver.get('http://127.0.0.1:5000')

    getScore = my_driver.find_element(By.ID, 'score').text
    if checkData(getScore, 1, 1000):
        print("The score is between 1 to 1000")
        my_driver.quit()
        return False
    else:
        print("The score isn't between 1 to 1000")
        my_driver.quit()
        return True


def main_function():
    shell_exec('python /full/path/to/hello.py');
    result = test_scores_service()
    if result:
        return 0
    else:
        return -1


main_function()
