from logging import Logger, getLogger
from os import path
from random import random
from time import sleep

from requests import get
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

from config import Config


class Voter:
    _url: str
    _config: Config
    _driver: Edge
    _logger: Logger

    def __init__(self, config: Config):
        self._url = get("http://fc.truman.pro/vote_url").text
        self._config = config
        self._driver = self._get_driver(config)
        self._logger = getLogger("Voter")

    def run(self, set_progress=None):
        self._logger.info(
            f"Voting Started (Total Rounds: {self._config.number_of_rounds})"
        )
        self._vote_loop(set_progress)
        self._logger.info(f"Voting Finished")

    def _vote_loop(self, set_progress=None):
        number_of_rounds = self._config.number_of_rounds
        for n in range(1, number_of_rounds + 1):
            remaining = number_of_rounds - n
            self._logger.info(
                f"Voting Round {n} Started"
            )
            try:
                self._vote_round()
                self._logger.info(
                    f"Voting Round {n} Finished (Remaining Rounds: {remaining})"
                )
            except Exception as e:
                self._logger.warning(
                    f"Voting Round {n} Failed (Reason: {e})"
                )
            if set_progress:
                set_progress(n)
            if remaining != 0:
                interval = self._dither(self._config.round_interval_seconds)
                self._logger.info(
                    f"Voting Round Interval: Sleep {interval:.2f}s"
                )
                sleep(interval)

    def _vote_round(self):
        driver = self._driver
        driver.get(self._url)
        for _ in range(self._config.max_votes):
            driver.find_element(By.CLASS_NAME, "vote-result").click()
            sleep(self._dither(self._config.vote_interval_seconds))
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print(exc_tb)
        try:
            self._driver.quit()
        except Exception as e:
            print(e)

    @staticmethod
    def _get_driver(config: Config):
        service = Service(executable_path=path.join(path.abspath(path.dirname(__file__)), 'msedgedriver.exe'))
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.headless = config.headless
        return Edge(service=service, options=options)

    @staticmethod
    def _dither(value: float, scale=0.2):
        return value + value * (random() - 0.5) * scale * 2
