import os
import re
import time
from os import environ
from dotenv import load_dotenv


if os.path.exists('config.env'):
    load_dotenv('config.env')
    
    
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
SESSION_STRING = environ['SESSION_STRING']

TEXT = environ['TEXT']
USERNAME = environ['USERNAME']