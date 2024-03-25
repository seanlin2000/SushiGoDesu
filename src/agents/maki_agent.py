import numpy as np
from agent import Agent
from card import Card

class NigiriAgent(Agent):

    def __init__(self):
        super().__init()

    def get_action(self):
        if Card.MAKI_3 in self.hand:
            return Card.MAKI_3
        elif Card.MAKI_2 in self.hand:
            return Card.MAKI_2
        elif Card.MAKI_1 in self.hand:
            return Card.MAKI_1
        else:
            return [card for card, count in self.hand.items() if count > 0][0]