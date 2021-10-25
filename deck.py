#deck.py

from dice import Development, Settlement, Dice, Card, Colors
import csv

DECK = [
    Card(
        Settlement("Big Blue", 2, Colors["novelty"], lambda : Dice.novelty().roll()),
        Development("Useless", 2, Colors["development"], lambda : None, lambda : Dice.military().roll())
    )
]

def init():
    TITLE = 0
    COST = 2
    COLOR = 3
    with open("alltiles.csv") as file:
        data = csv.reader(file,delimiter="|")
        reader = list(data)
        for i in range(len(reader)-1):
            settlement = reader[i+1]
            development = reader[i]
            DECK.append(Card(
                Settlement(settlement[TITLE], settlement[COST], settlement[COLOR], lambda:Dice.alien().roll()),
                Development(development[TITLE], development[COST], development[COLOR], lambda: None, lambda: None)
                ))
            i+=1

def map(row):
    cardFace = CardFace(title, cost, color)
