import logging
from random import random
from time import sleep

from config import config
from main import LOGGING_FORMAT
from voter import Voter

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
    while True:
        with Voter(config) as voter:
            voter.run()
        sleep(200 + 20 * random())
