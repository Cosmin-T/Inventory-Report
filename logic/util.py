# util.py

from logic.config_ini import *
import logging

config = con()

# webdriver
URL = config['DEFAULT']['URL']
CROMEDRIVER_PATH = '/usr/local/bin/chromedriver'

# login
USER = config['DEFAULT']['USER']
USER_XPATH = '//*[@id="username"]'
PASSWORD = config['DEFAULT']['PASSWORD']
PASSWORD_XPATH = '//*[@id="password"]'
LOGIN_XPATH = '//*[@id="loginBtn"]/span'


# navigation
HIT_AGA = '//*[@id="cc_3058151"]/div'
LB19 = '//*[@id="3168109"]'
LB34 = '//*[@id="3168110"]'
LB51 = '//*[@id="3168111"]'
LB52 = '//*[@id="3168112"]'
LB75 = '//*[@id="3168116"]'
LB10 = '//*[@id="3168108"]'
LB14 = '//*[@id="3171610"]'
LB18 = '//*[@id="3169816"]'
LB65 = '//*[@id="3168113"]'
LB66 = '//*[@id="3168114"]'
LB73 = '//*[@id="3168115"]'
LB77 = '//*[@id="3168117"]'
LB83 = '//*[@id="3173586"]'
FD37 = '//*[@id="3168098"]'
FD80 = '//*[@id="3168094"]'
FD81 = '//*[@id="3168095"]'
FD89 = '//*[@id="3168097"]'
A6 = '//*[@id="3168081"]'
A17 = '//*[@id="3168082"]'
A54 = '//*[@id="3168083"]'
A57 = '//*[@id="3168084"]'
U9 = '//*[@id="3168091"]'
U50 = '//*[@id="3168092"]'
U55 = '//*[@id="3168093"]'
SW7 = '//*[@id="3168100"]'
SW13 = '//*[@id="3168101"]'
SW16 = '//*[@id="3168102"]'
SW26 = '//*[@id="3173468"]'
SW27 = '//*[@id="3173585"]'
SW36 = '//*[@id="3173584"]'
SW56 = '//*[@id="3168103"]'
LOADED_VALUE = 'campaign-footer-outcomeslabel'

# paths
AGA_REPORT = '/Volumes/Samsung 970 EVO/Documents/Python/aga_inventory_report/AGA Inventory Report.xlsx'
OUTLOOK_TEMPLATE = config['DEFAULT']['OUTLOOK_TEMPLATE']

# logging
LOG_OUTPUT = '/Volumes/Samsung 970 EVO/Documents/Python/aga_inventory_report/log.txt'
LOG_LEVEL = logging.INFO

# email sending
FILE_OUTPUT_INV = '/Volumes/Samsung 970 EVO/Documents/Python/aga_inventory_report/AGA Inventory Report.xlsx'
SUBJECT_INV = 'AGA Inventory Report'
FILE_NAME_INV = 'AGA Inventory Report.xlsx'
SENDER_EMAIL = config['DEFAULT']['SENDER_EMAIL']
RECEIVER_EMAIL = config['DEFAULT']['RECEIVER_EMAIL']
GMAIL_APP_PASSWORD = config['DEFAULT']['GMAIL_APP_PASSWORD']