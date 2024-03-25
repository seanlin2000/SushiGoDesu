import numpy as np
from card import Card
from agent import Agent

class NigiriAgent(Agent):

    def __init__(self):
        super().__init()

    def get_action(self):
        if Card.SQUID_NIGIRI in self.hand:
            return Card.SQUID_NIGIRI
        elif Card.SALMON_NIGIRI in self.hand:
            return Card.SALMON_NIGIRI
        elif Card.EGG_NIGIRI in self.hand:
            return Card.EGG_NIGIRI
        else:
            return [card for card, count in self.hand.items() if count > 0][0]