import random
import unittest


class Card(object):
    def __init__(self, symbol, number):
        self.symbol = symbol
        self.number = number

    @property
    def get_symbol(self):
        return self.symbol

    @property
    def get_number(self):
        return self.number


class Deck(object):
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.extend(card)

    def remove_card(self, card):
        self.cards.remove(card)

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
                return False
            cards_list.append([card.symbol, card.number])
        return cards_list


class Dealer(object):
    def __init__(self, deck):
        self.deck = deck

    def deal_cards(self, players):
        self.deck.shuffle()
        cards = {}
        for i in range(0, players):
            cards[i] = self.deck.get_cards(2)
            if not cards[i]:
                return False
        cards["table"] = self.deck.get_cards(5)
        return cards


class TestDealer(unittest.TestCase):
    list_cards = [Card('Hearts', 2),
                  Card("Hearts", "A"),
                  Card("Tiles", 10),
                  Card("Pikes", "J"),
                  Card("Clovers", 6),
                  Card("Pikes", "K"),
                  Card("Tiles", "A"),
                  Card("Clovers", "A"),
                  Card("Pikes", "A")]

    def testEmptyDeck(self):
        self.assertEqual(Dealer(Deck([])).deal_cards(2), False)

    def testTwoPlayers(self):
        dealer = Dealer(Deck(self.list_cards))
        cards = dealer.deal_cards(2)
        self.assertEqual((2, 2, 5),
                         (len(cards[0]), len(cards[1]), len(cards["table"])))
