import numpy as np
from card import Card
from agents.agent import Agent

class SashimiAgent(Agent):

    def __init__(self):
        super().__init__()

    def get_action(self):
        if self.hand[Card.SASHIMI] >= 1:
            return Card.SASHIMI
        else:
            return [card for card, count in self.hand.items() if count > 0][0]