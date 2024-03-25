from enum import Enum

class Card(Enum):
    CHOPSTICKS = 1
    WASABI = 2
    DUMPLING = 3
    MAKI_1 = 4
    MAKI_2 = 5
    MAKI_3 = 6
    EGG_NIGIRI = 7
    SALMON_NIGIRI = 8
    SQUID_NIGIRI = 9
    TEMPURA = 10
    PUDDING = 11
    SASHIMI = 12
    USED_WASABI = 13

    def __str__(self):
        return self.name


NIGIRI_POINTS_DICT = {
    Card.EGG_NIGIRI : 1,
    Card.SALMON_NIGIRI : 2,
    Card.SQUID_NIGIRI : 3
}

MAKI_COUNTS_DICT = {
    Card.MAKI_1 : 1,
    Card.MAKI_2 : 2,
    Card.MAKI_3 : 3
}

CARD_COUNT_DICT = {
    Card.CHOPSTICKS : 4,
    Card.WASABI : 6,
    Card.DUMPLING: 14,
    Card.MAKI_1 : 6,
    Card.MAKI_2 : 12,
    Card.MAKI_3 : 8,
    Card.EGG_NIGIRI : 5,
    Card.SALMON_NIGIRI : 10,
    Card.SQUID_NIGIRI : 5,
    Card.TEMPURA : 14,
    Card.PUDDING : 10,
    Card.SASHIMI : 14
}