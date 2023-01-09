# The Game - drinker

# Here is the class "Card" (карта) down below
class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    # List of string values presented all the suits

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "jack", "queen", "king", "ace"]
    # List of string values presented nominal values of the cards
    # First two "none" is for making the list indexes == card's nominal values 

    def __init__(self, v, s):
        """suit and value is integers"""
        self.value = v 
        self.suit = s 

    def __lt__(self, c2): 
        """Check if value lower than c2 (second card)"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        """Check if value greater than c2 (second card)"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self): 
        """assignes value and suit of a card for "v" and print the result"""
        v = self.values[self.value] + " of " \
        + self.suits[self.suit]
        return v

# Here is the class "Deck" (колода) down below

from random import shuffle # this method randomly shuffles the elements in list "cards".

class Deck:
    def __init__(self):
        self.cards = [] 
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        

    def __rm_card__(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

deck = Deck()
for card in deck.cards:
    print(card)
