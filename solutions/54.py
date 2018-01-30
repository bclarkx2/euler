#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from common import get_resource_file
from enum import Enum
from itertools import permutations


###############################################################################
# Problem                                                                     #
###############################################################################

def read_games(path):
    with open(path) as game_file:
        games = [x.strip() for x in game_file.readlines()]
    return games


def rev_gt(a, b):
    return sorted(a, reverse=True) > \
        sorted(b, reverse=True)


class Face(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @classmethod
    def of(cls, f):
        try:
            return Face(int(f))
        except ValueError:
            if f == "T":
                return cls.TEN
            elif f == "J":
                return cls.JACK
            elif f == "Q":
                return cls.QUEEN
            elif f == "K":
                return cls.KING
            elif f == "A":
                return cls.ACE
            else:
                raise ValueError("bad face")

    def __lt__(self, other):
        return self.value < other.value


class Suit(Enum):

    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

    @classmethod
    def of(cls, s):
        if s == "H":
            return cls.HEARTS
        elif s == "D":
            return cls.DIAMONDS
        elif s == "C":
            return cls.CLUBS
        elif s == "S":
            return cls.SPADES
        else:
            raise ValueError("bad suit")


class Card(object):

    def __init__(self, face, suit):
        super(Card, self).__init__()
        self.face = Face.of(face)
        self.suit = Suit.of(suit)

    def __str__(self):
        return "{}:{}".format(self.face.name,
                              self.suit.name)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.face.value < other.face.value

    def __eq__(self, other):
        return self.face.value == other.face.value


class Game(object):

    @classmethod
    def make(cls, game_string):
        tokens = game_string.split()
        h1_tokens = tokens[:len(tokens) // 2]
        h2_tokens = tokens[len(tokens) // 2:]
        h1 = Hand.make(h1_tokens)
        h2 = Hand.make(h2_tokens)
        return Game(h1, h2)

    def __init__(self, hand1, hand2):
        super(Game, self).__init__()
        self.hand1 = hand1
        self.hand2 = hand2

    def play(self):
        return self.hand1 > self.hand2


class Hand(object):

    @classmethod
    def make(cls, hand_tokens):
        cards = [Card(c[0], c[1]) for c in hand_tokens]

        if cls.same_suit(cards):

            if cls.consecutive(cards):

                if min(cards).face == Face.TEN:
                    return RoyalFlush(cards)
                else:
                    return StraightFlush(cards)
            else:
                return Flush(cards)

        if cls.consecutive(cards):
            return Straight(cards)

        dups = cls.duplicates(cards)

        if cls.is_full_house(dups):
            return FullHouse(cards, dups)

        pairs = cls.pairs(dups)

        if len(pairs) == 2:
            return TwoPairs(cards, dups)
        elif len(pairs) == 1:
            return OnePair(cards, dups)

        if max(dups.values()) == 4:
            return FourOfAKind(cards)
        elif max(dups.values()) == 3:
            return ThreeOfAKind(cards, dups)

        return HighCard(cards)

    @staticmethod
    def pairs(dups):
        return {card: count for card, count
                in dups.items() if count == 2}

    @staticmethod
    def is_full_house(dups):
        has_three = False
        has_two = False
        for card, count in dups.items():
            if count == 3:
                has_three = True
            elif count == 2:
                has_two = True
        return has_three and has_two

    @staticmethod
    def duplicates(cards):
        faces = [c.face for c in cards]
        dups = {}
        for face in Face:
            dups[face.value] = faces.count(face)
        return dups

    @staticmethod
    def same_suit(cards):
        return len(set(c.suit for c in cards)) == 1

    @staticmethod
    def consecutive(cards):
        values = sorted([c.face.value for c in cards])
        lowest = min(values)
        highest = max(values)
        return values == list(range(lowest, highest + 1))

    def __init__(self, cards):
        super(Hand, self).__init__()
        self.cards = cards

    def high_card(self):
        return max(self.cards)

    def comp(self, other):
        return None

    def __gt__(self, other):
        if self.ranking == other.ranking:
            eq_comp = self.comp(other)
            if eq_comp is not None:
                return eq_comp
            else:
                return rev_gt(self.cards, other.cards)
        return self.ranking < other.ranking

    def __str__(self):
        return [str(c) for c in self.cards]


class DupHand(Hand):

    def __init__(self, cards, dups):
        super().__init__(cards)
        self.dups = dups

    def repeating(self, want_count):
        return next(card for card, count in
                    self.dups.items() if
                    count == want_count)

    def with_count(self, want_count):
        remaining = [card for card, count in
                     self.dups.items() if
                     count == want_count]
        return remaining

    def one(self):
        return self.repeating(1)

    def two(self):
        return self.repeating(2)

    def three(self):
        return self.repeating(3)


class RoyalFlush(Hand):
    ranking = 1


class StraightFlush(Hand):
    ranking = 2


class FourOfAKind(Hand):
    ranking = 3


class FullHouse(DupHand):
    ranking = 4

    def comp(self, other):
        if self.three() == other.three():
            return self.two() > other.two()
        return self.three() > other.three()


class Flush(Hand):
    ranking = 5


class Straight(Hand):
    ranking = 6


class ThreeOfAKind(DupHand):
    ranking = 7

    def comp(self, other):
        if self.three() == other.three():
            return rev_gt(self.with_count(1),
                          other.with_count(1))
        return self.three() > other.three()


class TwoPairs(DupHand):
    ranking = 8

    def pair_max(self):
        return max(self.with_count(2))

    def comp(self, other):
        if self.pair_max() == other.pair_max():
            return self.one() > other.one()
        return self.pair_max() > other.pair_max()


class OnePair(DupHand):
    ranking = 9

    def comp(self, other):
        if self.two() == other.two():
            return rev_gt(self.with_count(1),
                          other.with_count(1))
        return self.two() > other.two()


class HighCard(Hand):
    ranking = 10


class Problem54(Euler):

    def __init__(self):
        super().__init__("test", 0)

    def solve(self):

        if self.test:
            test()
        else:
            path = get_resource_file("p054_poker.txt")
            game_strings = read_games(path)
            games = [Game.make(s) for s in game_strings]
            wins = sum(g.play() for g in games)
            return wins


###############################################################################
# Testing                                                                     #
###############################################################################

def test():
    test_same_hand_wins()
    test_hand_parsing()
    test_relative_hands()


def test_same_hand_wins():

    # Royal flush
    assert not Game.make("TS JS QS KS AS TD JD QD KD AD").play()

    # high card
    assert not Game.make("8C TS KC 9H 4S 7D 2S 5D 3S AC").play()
    assert Game.make("AC KS QC JH 5S AD KS QD JS 4C").play()

    # straight
    assert not Game.make("3S 4H 5D 6C 7S 3H 4D 5C 6S 7S").play()

    # one pair
    assert not Game.make("QS QH TC 8S 6D QS QH TC 8S 6D").play()
    assert not Game.make("QS QH TC 8S 6D KS KH TC 8S 6D").play()
    assert Game.make("AS AH TC 8S 6D KS KH TC 8S 6D").play()
    assert Game.make("QS QH TC 8S 6D QS QH 9C 8S 6D").play()
    assert not Game.make("QS QH AC 8S 6D KS KH 9C 8S 6D").play()
    assert Game.make("QS QH AC 9S 6D QS QH AC 8S 6D").play()


def test_relative_hands():

    high_card = Hand.make(["AS", "TC", "8D", "4H", "2S"])
    one_pair = Hand.make(["AS", "AC", "8D", "4H", "2S"])
    two_pairs = Hand.make(["AS", "AC", "8D", "8H", "2S"])
    three_of_a_kind = Hand.make(["AS", "AS", "AD", "4H", "2S"])
    straight = Hand.make(["KS", "QC", "JD", "TH", "9S"])
    flush = Hand.make(["AS", "TS", "8S", "4S", "2S"])
    full_house = Hand.make(["AS", "AC", "8D", "8H", "8S"])
    four_of_a_kind = Hand.make(["AS", "AC", "AD", "AH", "2S"])
    straight_flush = Hand.make(["KS", "QS", "JS", "TS", "9S"])
    royal_flush = Hand.make(["AS", "KS", "QS", "JS", "TS"])

    assert isinstance(high_card, HighCard)
    assert isinstance(one_pair, OnePair)
    assert isinstance(two_pairs, TwoPairs)
    assert isinstance(three_of_a_kind, ThreeOfAKind)
    assert isinstance(straight, Straight)
    assert isinstance(flush, Flush)
    assert isinstance(full_house, FullHouse)
    assert isinstance(four_of_a_kind, FourOfAKind)
    assert isinstance(straight_flush, StraightFlush)
    assert isinstance(royal_flush, RoyalFlush)

    hands = [
        high_card,
        one_pair,
        two_pairs,
        three_of_a_kind,
        straight,
        flush,
        full_house,
        four_of_a_kind,
        straight_flush,
        royal_flush
    ]

    for hand1, hand2 in permutations(hands, 2):

        idx1 = hands.index(hand1)
        idx2 = hands.index(hand2)

        game = Game(hand1, hand2)

        if idx1 < idx2:
            assert not game.play()
        else:
            assert game.play()


def test_hand_parsing():

    # full house
    g = Game.make("4S 4H 4D 8C 8H QS QD QC JH JC")
    assert not g.play()
    assert isinstance(g.hand1, FullHouse)
    assert isinstance(g.hand2, FullHouse)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem54().out()
