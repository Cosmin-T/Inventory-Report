# followup.py

import pandas as pd
from logic.util import *
import logging
from logic.logs import *
import io
import datetime
import subprocess

def add_weekdays(start_date, days_to_add):
    current_date = start_date
    while days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        if current_date.weekday() < 5:
            days_to_add -= 1
    return current_date

def format_date_range(start_days, end_days):
    today = datetime.date.today()
    start_date = add_weekdays(today, start_days)
    end_date = add_weekdays(today, end_days)
    return f'Start: {start_date.strftime("%A, %B %d, %Y")} \nEnd: {end_date.strftime("%A, %B %d, %Y")}'

def determine_output(value, label):
    if value <= 0:
        return 'N/A'
    elif label.startswith('LB') or label.startswith('FD'):
        if 10 <= value <= 100:
            return format_date_range(1, 2)
        elif 101 <= value <= 150:
            return format_date_range(2, 3)
        elif 151 <= value <= 250:
            return format_date_range(3, 5)
        elif 251 <= value <= 350:
            return format_date_range(4, 7)
        elif value > 350:
            return 'Find Parker'
        else:
            return 'N/A'
    else:
        if 10 <= value <= 100:
            return format_date_range(1, 2)
        elif 101 <= value <= 275:
            return format_date_range(2, 4)
        elif value > 275:
            return 'Find Tom Barker'
        else:
            return 'N/A'

def follow():
    try:
        with open(AGA_REPORT, 'rb') as f:
            content = f.read()
        df = pd.read_excel(io.BytesIO(content), engine='openpyxl')
        logging.info('Dataframe Created')

        rows_to_process = {
        'LB19':1, 'LB34':2, 'LB51':3, 'LB52':4, 'LB75':5, 'LB10':8, 'LB14':9, 'LB18':10, 'LB65':11, 'LB66':12, 'LB73':13, 'LB77':14, 'LB83':15,
        'FD37':18, 'FD80':19, 'FD81':20, 'FD89':21, 'A6':24, 'A17':25, 'A54':26, 'A57':27,
        'U9':30, 'U50':31, 'U55':32, 'SW7':35, 'SW13':36, 'SW16':37, 'SW26':38, 'SW27':39, 'SW36':40, 'SW56':41
        }

        for label, row_index in rows_to_process.items():
            if row_index < len(df):
                df.at[row_index, 'Follow Up'] = determine_output(df.at[row_index, 'Inventory '], label)
            else:
                logging.error(f"Row index out of range: {label} -> {row_index}")

        logging.info('Dates added')

        df.to_excel(AGA_REPORT, index=False)
        logging.info('Report Updated')

        applescript = f"""
        tell application "Finder"
            activate
            close every Finder window
            make new Finder window to POSIX file "{AGA_REPORT}"
            tell application "System Events" to keystroke "t" using command down
            delay 0.5
            set target of Finder window 1 to POSIX file "{OUTLOOK_TEMPLATE}"
        end tell
        """

        subprocess.run(['osascript', '-e', applescript], check=True)
        logging.info('Folders Open Successfully\n')


    except Exception as e:
        logging.error(f'Error: {e}')