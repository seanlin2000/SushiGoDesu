import numpy as np
from card import Card
from agent import Agent

class SashimiAgent(Agent):

    def __init__(self):
        super().__init()

    def get_action(self):
        if Card.SASHIMI in self.hand:
            return Card.SASHIMI
        else:
            return [card for card, count in self.hand.items() if count > 0][0]