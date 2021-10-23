#game.py
from deck import *
from dice import *
import random

class Player:
    def __init__(self):
        self.citizenry = []
        self.cup = []
        self.settlements = []
        self.developments = []
        self.wallet = 3

    def discover(settlement):
        self.settlements.append(settlement)

    def research(development):
        self.developments.append(development)

class Game:
	def __init__(self):
		self.player = Player()
		self.deck = deck.DECK

	def play(self):
		card = self.deck[random.randint(0, len(self.deck)-1)]
		print(card)

if __name__ == "__main__":
	print("CIV: ", Dice.civilian().faces)
	print("MIL: ", Dice.military().faces)
	print("CON: ", Dice.consumption().faces)
	print("NOV: ", Dice.novelty().faces)
	print("RAR: ", Dice.rare_elements().faces)
	print("GEN: ", Dice.genes().faces)
	print("ALN: ", Dice.alien().faces)
	game = Game()
	game.play()
