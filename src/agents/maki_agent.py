import numpy as np
from agents.agent import Agent
from card import Card

class NigiriAgent(Agent):

    def __init__(self):
        super().__init__()

    def get_action(self):
        if self.hand[Card.MAKI_3] >= 1:
            return Card.MAKI_3
        elif self.hand[Card.MAKI_2] >= 1:
            return Card.MAKI_2
        elif self.hand[Card.MAKI_1] >= 1:
            return Card.MAKI_1
        else:
            return [card for card, count in self.hand.items() if count > 0][0]