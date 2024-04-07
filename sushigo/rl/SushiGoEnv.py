import numpy as np
import functools
from copy import copy 
from typing import Any, Optional
import gymnasium as gym
from gymnasium import spaces

from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector, wrappers

from sushigo.card import Card, CARD_COUNT_DICT
from sushigo.deck import Deck
from sushigo.constants import NUM_PLAYERS, NUM_CARDS

class SushiGoEnv(AECEnv):

    

    def __init__(self):
        super().__init__()

        # Number of actions is num_cards - used_wasabi + chopsticks_action
        self.action_space = spaces.Discrete(len(Card))

        self.render_mode = ["console"]

        self.deck = None
        self.possible_agents = ["p1", "p2", "p3", "p4"]
        self.observation_names = ['agent', 'left', 'right', 'across']

        self.last_observation = None
    
    def reset(self, seed=42):
        """
        Reset needs to initialize the following attributes
        - agents
        - rewards
        - _cumulative_rewards
        - terminations
        - truncations
        - infos
        - agent_selection
        And must set up the environment so that render(), step(), and observe()
        can be called without issues.
        Here it sets up the state dictionary which is used by step() and the observations dictionary which is used by step() and observe()
        """
        super().reset(seed=seed)
        self.deck = Deck(seed)

        self.agents = copy(self.possible_agents)
        self.rewards = {agent: 0 for agent in self.agents}
        self._cumulative_rewards = {agent: 0 for agent in self.agents}
        self.terminations = {agent: False for agent in self.agents}
        self.truncations = {agent: False for agent in self.agents}
        self.infos = {agent: {} for agent in self.agents}
        self.state = {agent: None for agent in self.agents}
        self.observations = {agent: None for agent in self.agents}
        self.num_moves = 0

        
        # Our agent_selector utility allows easy cyclic stepping through the agents list.

        self._agent_selector = agent_selector(self.agents)
        self.agent_selection = self._agent_selector.next()

    def step(self, action):
                """
        step(action) takes in an action for the current agent (specified by
        agent_selection) and needs to update
        - rewards
        - _cumulative_rewards (accumulating the rewards)
        - terminations
        - truncations
        - infos
        - agent_selection (to the next agent)
        And any internal state used by observe() or render()
        """
        pass

    def render(self):
        pass

    def close(self):
        pass


    # Observation space should be defined here.
    # lru_cache allows observation and action spaces to be memoized, reducing clock cycles required to get each agent's space.
    @functools.lru_cache(maxsize=None)
    def observation_space(self, agent: Any) -> gym.Space:
        observations = {}

        player_hands = {f"{player}_hand" : get_card_obs() for player in self.observation_names}
        player_cards = {f"{player}_cards" : get_card_obs() for player in self.observation_names}
        player_puddings = {f"{player}_puddings" : spaces.Box(low=0, high=CARD_COUNT_DICT[Card.PUDDING], dtype=int) for player in self.observation_names}
        observations.update(player_hands)
        observations.update(player_cards)
        observations.update(player_puddings)
        observations["graveyard_cards"] = get_card_obs()

        return spaces.Dict(observations)

    # Action space should be defined here.
    # lru_cache allows observation and action spaces to be memoized, reducing clock cycles required to get each agent's space.
    @functools.lru_cache(maxsize=None)
    def action_space(self, agent: Any) -> gym.Space:
        return spaces.Discrete(len(Card))
    

def get_card_obs():
    return spaces.Dict(
        {   
            card: spaces.Box(low=0, high=CARD_COUNT_DICT[card], dtype=int)
            for card in Card if card != Card.USED_WASABI
        }
    )


def get_starting_obs(deck):
    return {card: 0 for card in Card if card != Card.USED_WASABI}