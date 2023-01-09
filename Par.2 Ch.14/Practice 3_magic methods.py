# The Game - drinker

# Here is the class "Card" (карта) down below

from random import shuffle # this method randomly shuffles the elements in list "cards".

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

class Deck:
    def __init__(self):
        self.cards = [] 
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


# Here is the class "Player" (Игрок) down below
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


# Here is the class "Game" (Игра) down below

class Game:
    def __init__(self):
        name1 = input("Enter the name of Player 1: ")
        name2 = input("Enter the name of Player 2: ")
        self.deck = Deck() # seld.deck takes class Deck
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins and get the cards"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} takes {}, and {} takes {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards # this method puts in "cards" the deck created by __init__ in class Deck.
        print("Let's go!")
        while len(cards) >= 2:
            m = "Enter X for escape. Enter any other button for starting the game."
            response = input(m)
            if response == "X":
                break
            p1n = self.p1.name
            p1c = self.deck.rm_card()
            p2n = self.p2.name
            p2c = self.deck.rm_card()
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("The game is over. {} wins!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Draw!"

game = Game()
game.play_game()

              
