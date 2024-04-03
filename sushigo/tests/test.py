# TODO: WRITE A TEST

from gymnasium import spaces
from gymnasium.wrappers import FlattenObservation

from sushigo.card import Card, CARD_COUNT_DICT

def get_card_obs():
    return spaces.Dict(
        {   
            card: spaces.Discrete(CARD_COUNT_DICT[card])
            for card in Card if card != Card.USED_WASABI
        }
    )

def main():
    obs = spaces.Dict(
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

    print(obs.sample)

if __name__ == "__main__":
    main()