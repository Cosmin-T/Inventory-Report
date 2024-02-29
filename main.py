# main.py

from logic.webdriver import *
from logic.login import *
from logic.navigation import *
from logic.followup import *
from logic.send_email import *
import time


def main():
    driver = initialize_webdriver(URL)
    log(driver, USER_XPATH, PASSWORD_XPATH, LOGIN_XPATH, USER, PASSWORD)
    nav(driver)
    follow()
    send(FILE_OUTPUT_INV, SUBJECT_INV, FILE_NAME_INV)
if __name__ == '__main__':
    main()