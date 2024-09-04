import random

Deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5,
        6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Player:

    def __init__(self):
        self.cards = []
        self.deal()
        self.deal()

    def deal(self):
        card = random.randint(0, Deck.__len__() - 1)
        self.cards.append(Deck[card])
        Deck.remove(Deck[card])

    def Sum(self):
        sum = 0
        aces = 0
        for i in self.cards:
            if type(i) == int:
                sum += i
            elif i == 'J' or i == 'K' or i == 'Q':
                sum += 10
            else:
                aces += 1
        while aces != 0:
            if sum < 10:
                sum += 11
            else:
                sum += 1
            aces -= 1
        return sum

    def checkBust(self):
        if self.Sum() > 21:
            return 2
        elif self.Sum() == 21:
            return 1
        else:
            return 0

    def printCards(self):
        print("these are your cards: ")
        for card in self.cards:
            if card == 10:
                print(" _______\n|       |\n|   10  |\n|       |\n|_______|")
            else:
                print(f" _______\n|       |\n|   {card}   |\n|       |\n|_______|")
        print("this is the sum of your cards: " + str(self.Sum()))

    def HitOrStand(self):
        hit = True
        while hit == True and self.checkBust() == 0:
            if input("Hit or Stand: ") == "hit":
                self.deal()
                self.printCards()
            else:
                hit = False


class Dealer(Player):
    def printCards(self):
        print("these are dealer's cards: ")
        for i in range(0, self.cards.__len__() - 1):
            if self.cards[i] == 10:
                print(" _______\n|       |\n|   10  |\n|       |\n|_______|")
            else:
                print(f" _______\n|       |\n|   {self.cards[i]}   |\n|       |\n|_______|")
        print(" _______\n|       |\n|   ?   |\n|       |\n|_______|")

    def printAllCards(self):
        print("these are dealer's cards: ")
        for card in self.cards:
            if card == 10:
                print(" _______\n|       |\n|   10  |\n|       |\n|_______|")
            else:
                print(f" _______\n|       |\n|   {card}   |\n|       |\n|_______|")
        print("this is the sum of dealer's cards: " + str(self.Sum()))

    def HitOrStand(self):
        while self.Sum() < 16:
            self.deal()


player = Player()
dealer = Dealer()
finished = False
player.printCards()
dealer.printCards()
player.HitOrStand()
if player.checkBust() != 2:
    dealer.HitOrStand()
player.printCards()
dealer.printAllCards()
if player.checkBust() == 0 and dealer.checkBust() == 0:
    if player.Sum() < dealer.Sum():
        outcome = -1
    elif player.Sum() > dealer.Sum():
        outcome = 1
    else:
        outcome = 0
elif player.checkBust() == 1:
    outcome = 1
elif dealer.checkBust() == 1:
    outcome = -1
elif player.checkBust() == 2:
    outcome = -1
elif dealer.checkBust() == 2:
    outcome = 1
else:
    outcome = 0

if outcome == 1:
    print("player wins")
elif outcome == 0:
    print("draw")
elif outcome == -1:
    print("dealer wins")


