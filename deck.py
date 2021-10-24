#deck.py

from dice import Development, Settlement, Dice, Card, Colors

DECK = [
    Card(
        Settlement("Big Blue", 2, Colors["novelty"], lambda : Dice.novelty().roll()),
        Development("Useless", 2, Colors["development"], lambda : None, lambda : Dice.military().roll())
    )
]