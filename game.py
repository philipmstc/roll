#game.py
from deck import *
from dice import *
from phases import *
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
        self.vp += card.cost 
        self.completed.append(card)

    def display_tableau(self):
        _str = ""
        for card in self.completed:
            _str += str(card) + "\n"
        return _str

PHASES = {
    "EXPLORE": Phase("explore", explore_start, explore_phase, explore_end)
    "SETTLE": Phase("settle", settle_start, settle_phase, settle_end)
    "DEVELOP": Phase("develop", develop_start, develop_phase, develop_end)
    "PRODUCE": Phase("produce", produce_start, produce_phase, produce_end)
    "SHIP": Phase("ship", ship_start, ship_phase, ship_end)
}

class Game:
    def __init__(self):
        self.player = Player()
        self.deck = deck.DECK

    

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
            self.player.turn_start()
            for phase in activePhases:
                phase.start(player)
                phase.play(player)
                phase.end(player)
            self.player.turn_end()
            self
            input("Press any key to continue")



if __name__ == "__main__":
    deck.init()
    game = Game()
    game.play()
