import numpy as np
from card import Card
from agents.agent import Agent

class NigiriAgent(Agent):

    def __init__(self):
        super().__init__()

    def get_action(self):
        if self.hand[Card.SQUID_NIGIRI] >= 1:
            return Card.SQUID_NIGIRI
        elif self.hand[Card.SALMON_NIGIRI] >= 1:
            return Card.SALMON_NIGIRI
        elif self.hand[Card.EGG_NIGIRI] >= 1:
            return Card.EGG_NIGIRI
        else:
            return [card for card, count in self.hand.items() if count > 0][0]