from card import Card, NIGIRI_POINTS_DICT, MAKI_COUNTS_DICT
from typing import Tuple

class Agent:

    def __init__(self):
        self.points = 0
        self.pudding_count = 0
        self.hand = {c.value : 0 for c in Card}
        self.previous_hand = None
        self.cards = {c.value : 0 for c in Card}
        self.maki_count = 0

    def get_action(self):
        """
        Selects card from hand to add to cards
        IMPLEMENT FOR AGENTS
        
        returns either a card or a tuple2 of cards picked by chopsticks
        """
        pass

    def reset_round(self):
        self.hand = {c.value : 0 for c in Card}
        self.previous_hand = None
        self.cards = {c.value : 0 for c in Card}
        self.maki_count = 0


    def implement_action(self, action):
        if type(action) == Card:
            self.implement_card_action(action)

        elif type(action) == Tuple[Card]:
            self.hand[Card.CHOPSTICKS] += 1
            self.cards[Card.CHOPSTICKS] -= 1
            self.implement_card_action(action[0])
            self.implement_card_action(action[1])
        else:
            raise ValueError("Invalid action")
        
        self.previous_hand = self.hand

    def implement_card_action(self, card):   
        # Update state             
        self.cards[card] += 1
        self.hand[card] -= 1

        # Assign points
        if card == Card.TEMPURA:
            if self.cards[Card.TEMPURA] % 2 == 0:
                self.points += 5
        elif card == Card.SASHIMI:
            if self.cards[Card.SASHIMI] % 3 == 0:
                self.points += 10
        elif card == Card.DUMPLING:
            self.points += self.cards[Card.DUMPLING]
        elif card in NIGIRI_POINTS_DICT:
            self.points += NIGIRI_POINTS_DICT[card]
            if self.cards[Card.WASABI] > 0:
                self.cards[Card.WASABI] -= 1
                self.cards[Card.USED_WASABI] += 1
                self.points += 2 * NIGIRI_POINTS_DICT[card]    

        # Assign misc state   
        elif card in MAKI_COUNTS_DICT:
            self.maki_count += MAKI_COUNTS_DICT[card]
        elif card == Card.PUDDING:
            self.pudding_count += 1

        
    def pass_hand(self, agent):
        agent.set_hand(self.previous_hand)

    def set_hand(self, hand: list):
        self.hand = hand

    

