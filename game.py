#game.py
from deck import *
from dice import *
import random

class Player:
    def __init__(self):
        self.citizenry = Container([2,1,1,3,1,1,1])
        self.cup = Container([1,0,1,0,0,0,3])
        self.settlements = Queue()
        self.developments = Queue()
        self.completed = []
        self.wallet = 3
        self.vp = 0

    def display_pre_turn(self):
        print("$", self.wallet, "   ✪", self.vp)
        print("CTZNRY: ", self.citizenry)
        print("CUP: ", self.cup)
        print()
        print("BOARD: ", self.display_tableau())
        print("In Progress: ", 
            "Ø" if self.settlements.isEmpty() else str(self.settlements),
            " | ",
            "Ø" if self.developments.isEmpty() else str(self.developments)
        )

    def discover(self, settlement):
        self.settlements.append(settlement)

    def research(self, development):
        self.developments.append(development)

    def complete(self, card):
        self.completed.append(card)

    def display_tableau(self):
        _str = ""
        for card in self.completed:
            _str += str(card) + "\n"
        return _str

PHASES = {
    "EXPLORE": [],
    "SETTLE": [],
    "DEVELOP": [],
    "PRODUCE": [],
    "SHIP": []
}

class Game:
    def __init__(self):
        self.player = Player()
        self.deck = deck.DECK

    def explore(self, die):
        choice = input("Should " + str(die) + " scout [X] or stock [$]")
        if choice == "X":
            self.scout(die)
        else: 
            self.stock(die)

    def scout(self, die):
        card = self.deck[random.randint(0, len(self.deck)-1)]
        print(card)
        choice = input("[s]ettlment or [d]evelopment?")
        if choice == "s":
            self.player.discover(card.settlement())
        else:
            self.player.research(card.development())

    def stock(self, die):
        self.player.wallet += 2

    def settle(self, die):
        if not self.player.settlements.isEmpty():
            settlement = self.player.settlements.assign_worker(die)
            if settlement:
                self.player.complete(settlement)

    def develop(self, die):
        if not self.player.developments.isEmpty():
            development = self.player.developments.assign_worker(die)
            if development:
                self.player.complete(development)

    def produce(self, die):
        pass

    def ship(self, die):
        pass

    def play(self):
        while(True):
            self.player.display_pre_turn()
            self.explore(Dice.civilian())
            self.settle(Dice.alien())
            self.develop(Dice.military())
            input("Press any key to continue")



if __name__ == "__main__":
    game = Game()
    game.play()
