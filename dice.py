import random, deck
EXPLORE = 0
DEVELOP = 1
SETTLE  = 2
ATTACK  = 3
DEFEND  = 4
WILD    = 5

Colors = {
    "neutral":"\033[0;37m",
    "civilian":"\033[1;37m",
    "military":"\033[1;31m",
    "consumption":"\033[1;35m",
    "novelty":"\033[1;96m",
    "rare_elements":"\033[1;33m",
    "genes":"\033[1;92m",
    "alien":"\033[1;93m",
    "development":"\033[1;33m",
}

class Dice:
    def __init__(self, color, counts):
        self.faces = []
        self.color = color
        for i in range(len(counts)):
            for n in range(counts[i]):
                self.faces.append(i)
        if len(self.faces) != 6:
            raise Exception("Dice should have 6 sides!") 
    
    def roll(self):
        return self.faces[random.randint(0,5)]

    def __str__(self):
        return self.color + "■" + Colors["neutral"]
    
    def civilian():
        return Dice(Colors["civilian"], (2,1,1,1,1,0))
    def military():
        return Dice(Colors["military"], (1,2,2,0,0,1))
    def consumption():
        return Dice(Colors["consumption"], (1,1,0,0,3,1))
    def novelty():
        return Dice(Colors["novelty"], (1,0,0,2,2,1))
    def rare_elements():
        return Dice(Colors["rare_elements"], (1,2,0,1,1,1))
    def genes():
        return Dice(Colors["genes"], (1,0,2,1,0,2))
    def alien():
        return Dice(Colors["alien"], (0,1,1,1,0,3))

DICE = [
    Dice.civilian(),
    Dice.military(),
    Dice.consumption(),
    Dice.novelty(),
    Dice.rare_elements(),
    Dice.genes(),
    Dice.alien()
]

class Container:
    def __init__(self, counts):
        self.dice = counts

    def __str__(self):
        _str = ""
        for i in range(len(self.dice)):
            _str += self.dice[i] * str(str(DICE[i]) + " ")
        return _str


class Card:
    def __init__(self, face1, face2):
        self.face1 = face1
        self.face2 = face2

    def __str__(self):
        return str(self.face1) + " | " + str(self.face2)

    def settlement(self):
        return self.face1
    def development(self):
        return self.face2

class CardFace:
    """
    * name|type|cost|color|reassign|reass. dice|I|II|III|IV|V|game end|die loss|die gain|placement|credits
    *
    *
    *
    *
    """

    def __init__(self, title, cost, color, onComplete):
        self.title = title
        self.cost = cost
        self.color = color
        self.onComplete = onComplete

    

    def __str__(self):
        output = "{1}] {0}"
        return output.format(self.title, self.cost)

class Development(CardFace):
    def __init__(self, title, cost, color, effect, onComplete):
        super().__init__(title, cost, color, onComplete)
        self.effect = effect

    def __str__(self):
        return "[" + Colors["development"] + "♦" + Colors["neutral"] + super().__str__()

class Settlement(CardFace):
    def __init__(self, title, cost, color, onComplete):
        super().__init__(title, cost, color, onComplete)
    def __str__(self):
        return "[" + self.color + "●" + Colors["neutral"] + super().__str__()

# literally a list wrapper, for now
class Queue():
    def __init__(self):
        self.queue = []
        self.workers = []

    def append(self, item):
        self.queue.append(item)

    def assign_worker(self, die):
        self.workers.append(die)
        if len(self.workers) == self.top().cost:
            # TODO need to move workers back to the citizenry
            self.deal_with_workers()
            return self.pop()
        else:
            return False;

    def top(self):
        return self.queue[0]

    def pop(self): 
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def deal_with_workers(self):
        self.workers = []

    def __str__(self):
        _str = "⌊"
        for worker in self.workers:
            _str += str(worker)
        _str += (self.top().cost-len(self.workers))*"□"
        return _str + "⌋ " + str(self.top())

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
