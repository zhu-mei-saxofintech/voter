from dataclasses import dataclass


@dataclass
class Config:
    max_votes: int
    vote_interval_seconds: float
    round_interval_seconds: float
    number_of_rounds: int = 5
    headless: bool = False


config = Config(
    max_votes=10,
    vote_interval_seconds=0.1,
    round_interval_seconds=2.0,
    number_of_rounds=5,
    headless=True
)
