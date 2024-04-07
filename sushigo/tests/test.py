# TODO: WRITE A TEST
from pprint import pprint

from gymnasium import spaces
from gymnasium.wrappers import FlattenObservation

from sushigo.card import Card, CARD_COUNT_DICT

def get_card_obs():
    return spaces.Dict(
        {   
            card: spaces.Box(low=0, high=CARD_COUNT_DICT[card], dtype=int)
            for card in Card if card != Card.USED_WASABI
        }
    )

def main():
    players = ["agent", "p2", "p3", "p4"]
    observations = {}

    player_hands = {f"{player}_hand" : get_card_obs() for player in players}
    player_cards = {f"{player}_cards" : get_card_obs() for player in players}
    player_puddings = {f"{player}_puddings" : spaces.Box(low=0, high=CARD_COUNT_DICT[Card.PUDDING], dtype=int) for player in players}
    observations.update(player_hands)
    observations.update(player_cards)
    observations.update(player_puddings)
    observations["graveyard_cards"] = get_card_obs()
    observations = spaces.Dict(observations)


    # print(spaces.flatten(observations, observations.sample()))
    pprint(observations.sample())

if __name__ == "__main__":
    main()