# navigation.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from logic.util import *
import logging
from logic.logs import *

def nav(driver):
    variables = {
        'LB19': LB19, 'LB34': LB34, 'LB51': LB51, 'LB52': LB52, 'LB75': LB75,
        'LB10': LB10, 'LB14': LB14, 'LB18': LB18, 'LB65': LB65, 'LB66': LB66,
        'LB73': LB73, 'LB77': LB77, 'LB83': LB83, 'FD37': FD37, 'FD80': FD80,
        'FD81': FD81, 'FD89': FD89, 'A6': A6, 'A17': A17, 'A54': A54, 'A57': A57,
        'U9': U9, 'U50': U50, 'U55': U55, 'SW7': SW7, 'SW13': SW13, 'SW16': SW16,
        'SW26': SW26, 'SW27': SW27, 'SW36': SW36, 'SW56': SW56
    }

    row_mapping = {
        'LB19':2, 'LB34':3, 'LB51':4, 'LB52':5, 'LB75':6, 'LB10':9, 'LB14':10, 'LB18':11, 'LB65':12, 'LB66':13, 'LB73':14, 'LB77':15, 'LB83':16,
        'FD37':19, 'FD80':20, 'FD81':21, 'FD89':22, 'A6':25, 'A17':26, 'A54':27, 'A57':28,
        'U9':31, 'U50':32, 'U55':33, 'SW7':36, 'SW13':37, 'SW16':38, 'SW26':39, 'SW27':40, 'SW36':41, 'SW56':42,
    }

    groups = {
        'lb1avg': range(2, 7),
        'lb2avg': range(9, 17),
        'fdavg': range(19, 23),
        'aavg': range(25, 29),
        'uavg': range(31, 34),
        'swavg': range(36, 43)
    }

    aga_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, HIT_AGA)))
    aga_btn.click()
    logging.info('AGA Selected')

    try:
        df = pd.read_excel(AGA_REPORT, header=None)
    except FileNotFoundError:
        df = pd.DataFrame(index=range(max(row_mapping.values()) + 1))

    for variable_name, value in variables.items():
        btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, value)))
        btn.click()
        time.sleep(2)
        logging.info(f'{variable_name} clicked')

        value = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, LOADED_VALUE))).text.strip('Loaded :')
        value = int(value)
        row_number = row_mapping[variable_name]
        df.at[row_number, 1] = value

    for group, rows in groups.items():
        total = 0

        for row in rows:
            value = df.at[row, 1]
            print(f'Value for row {row}: {value}')

            if pd.notna(value) and isinstance(value, (int, float)):
                total += value
        print(f'Total for {group} before writing to excel: {total}')

        sum_row = {
            'lb1avg': 7,
            'lb2avg': 17,
            'fdavg': 23,
            'aavg': 29,
            'uavg': 34,
            'swavg': 43
        }[group]

        df.at[sum_row, 1] = int(total)

    df.to_excel(AGA_REPORT, index=False, header=False)
    logging.info('Values added successfully')