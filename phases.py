#phases.py

class Phase:
    def __init__(self, game, name, start, play, end):
        self.game = game
        self.name = name
        self.start = start
        self.play = play
        self.end = end

	

PHASES = lambda game : [
	Phase(game, "explore", explore_start, explore, explore_end, end)
]

def explore(player, die):
    	choice = input("Should " + str(die) + " scout [X] or stock [$]")
    	if choice == "X":
    	    scout(die)
    	else: 
       	 stock(die)

def scout(player, die):
    card = game.deck[random.randint(0, len(game.deck)-1)]
    print(card)
    choice = input("[s]ettlment or [d]evelopment?")
    if choice == "s":
        player.discover(card.settlement())
    else:
        player.research(card.development())

def stock(self, player, die):
    player.wallet += 2

