import random
import unittest
import itertools


class Card(object):
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number


class Deck(object):
    def __init__(self):
        symbols = ["Hearts", "Tiles", "Clovers", "Pikes"]
        numbers = list(range(1, 10))
        numbers.extend(["A", "J", "Q", "K"])
        cards = [Card(k, v) for (k, v) in itertools.product(symbols, numbers)]
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self, func):
        self.cards.sort(func)

    def get_cards(self, number=1):
        cards_list = []
        for i in range(0, number):
            try:
                card = self.cards.pop()
            except IndexError:
                print("No more cards!")
                return None
            cards_list.append([card.symbol, card.number])
        return cards_list


class Dealer(object):
    def __init__(self):
        self.deck = Deck()

    def deal_cards(self, players):
        self.deck.shuffle()
        cards = {}
        for i in range(0, players):
            cards[i] = self.deck.get_cards(2)
            if not cards[i]:
                print("No more cards!")
                return None
        cards["table"] = self.deck.get_cards(5)
        return cards


class TestDealer(unittest.TestCase):

    def test_two_players(self):
        dealer = Dealer()
        cards = dealer.deal_cards(2)
        self.assertEqual((2, 2, 5),
                         (len(cards[0]), len(cards[1]), len(cards["table"])))

    def test_no_more_cards(self):
        dealer = Dealer()
        cards = dealer.deal_cards(27)
        print(cards)
        self.assertIsNone(cards)
