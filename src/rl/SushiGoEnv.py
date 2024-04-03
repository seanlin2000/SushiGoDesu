import numpy as np
import gymmnasium as gym
from gymmnasium import spaces
from src.card import Card, CARD_COUNT_DICT
from src.deck import Deck
from src.constants import NUM_PLAYERS, NUM_CARDS

class SushiGoEnv(gym.Env):

    

    def __init__(self):
        super().__init__()

        # Number of actions is num_cards - used_wasabi + chopsticks_action
        self.action_space = spaces.Discrete(len(Card))

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Dict(
            {
                "agent_hand" : get_card_obs(),
                "agent_cards" : get_card_obs(),
                "agent_puddings" : spaces.Discrete(CARD_COUNT_DICT[Card.PUDDING]),
                "p2_hand" : get_card_obs(),
                "p2_cards" : get_card_obs(),
                "p2_puddings" : spaces.Discrete(CARD_COUNT_DICT[Card.PUDDING]),
                "p3_hand" : get_card_obs(),
                "p3_cards" : get_card_obs(),
                "p3_puddings": spaces.Discrete(CARD_COUNT_DICT[Card.PUDDING]),
                "p4_hand" : get_card_obs(),
                "p4_cards" : get_card_obs(),
                "p4_puddings": spaces.Discrete(CARD_COUNT_DICT[Card.PUDDING]),
                "graveyard_cards" : get_card_obs()
            }
        )

        self.render_mode = ["console"]

        self.deck = None
    
    def reset(self, seed=42):
        """
        Sets the initial state of the environment
        """
        super().reset(seed=seed)
        self.deck = Deck(seed)
        initial_obs = {
                "agent_hand" : self.deck.deal(NUM_CARDS),
                "agent_cards" : get_starting_obs(),
                "agent_puddings" : 0,
                "p2_hand" : self.deck.deal(NUM_CARDS),
                "p2_cards" : get_starting_obs(),
                "p2_puddings" : 0,
                "p3_hand" : self.deck.deal(NUM_CARDS),
                "p3_cards" : get_starting_obs(),
                "p3_puddings": 0,
                "p4_hand" : self.deck.deal(NUM_CARDS),
                "p4_cards" : get_starting_obs(),
                "p4_puddings": 0,
                "graveyard_cards" : get_starting_obs()
            }
        return initial_obs, {}

    def step(self, action):
        pass

    def render(self):
        pass

    def close(self):
        pass

    def _get_obs():
        pass

print("HI")

def get_card_obs():
    return spaces.Dict(
        {   
            card: spaces.Discrete(CARD_COUNT_DICT[card])
            for card in Card if card != Card.USED_WASABI
        }
    )

def get_starting_obs(deck):
    return {card: 0 for card in Card if card != Card.USED_WASABI}