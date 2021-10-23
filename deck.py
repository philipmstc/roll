#deck.py

from dice import Development, Settlement, Dice, Card

DECK = [
	Card(
		Settlement("Big Blue", 1, "novelty", lambda : Dice.novelty().roll()),
		Development("Useless", 1, "neutral", lambda : None, lambda : Dice.military().roll())
	)
]