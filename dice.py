import random, deck
EXPLORE = 0
DEVELOP = 1
SETTLE  = 2
ATTACK  = 3
DEFEND  = 4
WILD    = 5

class Dice:
    def __init__(self, counts):
        self.faces = []
        for i in range(len(counts)):
            for n in range(counts[i]):
                self.faces.append(i)
        if len(self.faces) != 6:
            raise Exception("Dice should have 6 sides!") 
    
    def roll(self):
        return self.faces[random.randint(0,5)]
    
    def civilian():
        return Dice((2,1,1,1,1,0))
    def military():
        return Dice((1,2,2,0,0,1))
    def consumption():
        return Dice((1,1,0,0,3,1))
    def novelty():
        return Dice((1,0,0,2,2,1))
    def rare_elements():
        return Dice((1,2,0,1,1,1))
    def genes():
        return Dice((1,0,2,1,0,2))
    def alien():
        return Dice((0,1,1,1,0,3))

class Card:
    def __init__(self, face1, face2):
        self.face1 = face1
        self.face2 = face2

    def __str__(self):
        output = "{0} {1} {2} || {3} {4} {5}"
        return output.format(
            self.face1.title, self.face1.color, self.face1.cost,
            self.face2.title, self.face2.color, self.face2.cost
        )   

class CardFace:
    def __init__(self, title, cost, color, onComplete):
        self.title = title
        self.cost = cost
        self.color = color
        self.onComplete = onComplete

class Development(CardFace):
    def __init__(self, title, cost, color, effect, onComplete):
        super().__init__(title, cost, color, onComplete)
        self.effect = effect

class Settlement(CardFace):
    def __init__(self, title, cost, color, onComplete):
        super().__init__(title, cost, color, onComplete)
       
if __name__ == '__main__':
    civ = Dice.civilian()
    print("CIV: ", civ.faces)
    print("MIL: ", Dice.military().faces)
    print("CON: ", Dice.consumption().faces)
    print("NOV: ", Dice.novelty().faces)
    print("RAR: ", Dice.rare_elements().faces)
    print("GEN: ", Dice.genes().faces)
    print("ALN: ", Dice.alien().faces)

    for card in deck.DECK:
        print(card)
