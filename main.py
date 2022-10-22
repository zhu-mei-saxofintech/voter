import logging

from config import config
from voter import Voter

LOGGING_FORMAT = "[%(asctime)s] [%(levelname)s]<%(name)s>:%(message)s"

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
    logging.info("With great power comes great responsibility.")
    with Voter(config) as voter:
        voter.run()
        input("Press Enter to Exit")
