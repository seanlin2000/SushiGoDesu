import numpy as np
from card import Card
from collections import Counter
from typing import Dict

class Deck:
    def __init__(self):
        self.deck = np.array(
                [Card.TEMPURA] * 14 +
                [Card.SASHIMI] * 14 +
                [Card.DUMPLING] * 14 + 
                [Card.MAKI_2] * 12 +
                [Card.MAKI_3] * 8 +
                [Card.MAKI_1] * 6 +
                [Card.SALMON_NIGIRI] * 10 +
                [Card.SQUID_NIGIRI] * 5 +
                [Card.EGG_NIGIRI] * 5 +
                [Card.PUDDING] * 10 +
                [Card.WASABI] * 6 +
                [Card.CHOPSTICKS] * 4
        )

        np.random.shuffle(self.deck)

        self.graveyard = {c : 0 for c in Card}

    def deal(self, n):
        to_deal = self.deck[:n]
        print("Dealt cards is:", len(to_deal))
        self.deck = self.deck[n:]
        hand =  dict(Counter(to_deal))
        hand.update({card : 0 for card in Card if card not in hand})
        return hand

    def put_cards_in_graveyard(self, card_counts : Dict[Card, int]):
        for card in card_counts:
            count = card_counts[card]
            if card != Card.USED_WASABI:
                self.graveyard[card] += count
            else:
                self.graveyard[Card.WASABI] += count
