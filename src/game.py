# To start, we just have 4p games
from agent import Agent
from card import Card
from typing import List
import numpy as np

class Game:
    def __init__(
        self, 
        agents : List[Agent]
    ):
        self.round = 0
        self.deck = np.array(
            [Card.TEMPURA] * 14 +
            [Card.SASHIMI] * 14 +
            [Card.DUMPLING] * 14 + 
            [Card.MAKI2] * 12 +
            [Card.MAKI3] * 8 +
            [Card.MAKI1] * 6 +
            [Card.NIGIRI_SALMON] * 10 +
            [Card.NIGIRI_SQUID] * 5 +
            [Card.NIGIRI_EGG] * 5 +
            [Card.PUDDING] * 10 +
            [Card.WASABI] * 6 +
            [Card.CHOPSTICKS] * 4
        )   

        self.pudding_counts = [0 for _ in agents]
        self.point_counts = [0 for _ in agents]

    def simulate_game(self):
        for i in range(3):
            self.simulate_round()

        ## Add pudding points

    def simulate_round(self):


if __name__ == "__main__":
    game = Game((Agent() for _ in range(4)))
    print(game.pudding_counts)
