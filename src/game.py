# To start, we just have 4p games
from torch import DisableTorchFunctionSubclass
from agents.agent import Agent
from agents.sashimi_agent import SashimiAgent
from card import Card
from constants import NUM_CARDS, NUM_PLAYERS
from deck import Deck
from typing import List
import numpy as np

seed = 42
np.random.seed(seed)

class Game:
    def __init__(
        self, 
        agents : List[Agent]
    ):
        self.agents = agents
        self.deck = Deck()
        self.simulate_game()

    def simulate_game(self):
        for i in range(3):
            print(f"Round {i} begin")
            self.simulate_round()

        self.record_pudding_points()
        
        print("Game finished")
        for i in range(NUM_PLAYERS):
            print(f"Player {i} scored {self.agents[i].points} points")

    def simulate_round(self):
        # CR : un-hardcode 8

        
        for agent in self.agents:
            agent.reset_round()
            agent.hand = self.deck.deal(NUM_CARDS)
            print(f"Agent has hand of size {sum([agent.hand[key] for key in agent.hand])}")

        for _turn in range(NUM_CARDS):
            print("Turn ", _turn)
            for i, agent in enumerate(self.agents):
                print(f"Agent {i} has hand of size {sum([agent.hand[key] for key in agent.hand])}")
                action = agent.get_action()
                agent.implement_action(action)

                for card in agent.hand:
                    if agent.hand[card] < 0:
                        print(card)
                        raise ValueError("Card has value less than 0!")
                
                print(f"Agent {i} has {agent.points} points")

            for i, agent in enumerate(self.agents):
                agent.pass_hand(self.agents[i - 1])
        
        self.record_maki_points()

        for agent in self.agents:
            self.deck.put_cards_in_graveyard(agent.cards)


    def record_maki_points(self):
        desc_maki = sorted(self.agents, key=lambda agent : agent.maki_count, reverse=True)
        top_makis = [agent for agent in desc_maki if agent.maki_count == desc_maki[0].maki_count]

        if len(top_makis) == 1:
            next_top_makis = [agent for agent in desc_maki if agent.maki_count == desc_maki[1].maki_count]
            for agent in next_top_makis:
                agent.points += 3 / len(next_top_makis)
        
        for agent in top_makis:
            agent.points += 6 / len(top_makis)
        
    def record_pudding_points(self):
        desc_pudding = sorted(self.agents, key=lambda agent : agent.pudding_count, reverse=True)
        top_puddings = [agent for agent in desc_pudding if agent.pudding_count == desc_pudding[0].pudding_count]
        bottom_puddings = [agent for agent in desc_pudding if agent.pudding_count == desc_pudding[-1].pudding_count]
        for agent in top_puddings:
            agent.points += 6 / len(top_puddings)

        for agent in bottom_puddings:
            agent.points += -6 / len(bottom_puddings)


if __name__ == "__main__":
    game = Game([SashimiAgent() for _ in range(NUM_PLAYERS)])
