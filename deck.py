#deck.py


import csv

def mapPhaseSymbol(reassign_dice):
    if reassign_dice == "selected phase":
        return "selected_phase"
    if reassign_dice == "I":
        return "explore"
    if reassign_dice == "II":
        return "develop"
    if reassign_dice == "III":
        return "settle"
    if reassign_dice == "IV":
        return "produce"
    if reassign_dice == "V":
        return "ship"
    return reassign_dice

def init():
    fields = {}
    with open("alltiles.csv") as file:

        def g(line, field):
            return line[fields[field]]
        xml = ""
        data = csv.reader(file,delimiter="|")
        reader = list(data)
       
        for i in range(len(reader)):
            line = reader[i]
            if i == 0:
                for j in range(len(line)):
                    fields = { **fields, line[j] : j}
        

            else:
                xml += '\n<card type="{0}" name="{1}" cost="{2}">'.format(g(line,"type"), g(line, "name"), g(line, "cost"))
                
                if g(line, "end_game_text"):
                    xml += '\n\t<phaseEffect phase="game_end" text="{0}"/>'.format(g(line, "end_game_text"))
                ##
                # Reassign
                ##
                if g(line, "reassign"):
                    xml += '\n\t<reassign toPhase="{0}" from="{1}"/>'.format(mapPhaseSymbol(g(line, "reassign_dest")), g(line, "reassign"))

                if g(line, "phase_active"):
                    xml += '\n\t<phaseEffect phase="{0}">'.format(g(line, "phase_active"))
                    
                
                    ##
                    # Mo money/VP
                    ##
                    if g(line, "credit_gain") or g(line, "vp_gain"):
                        xml += '\n\t\t<gain type="{0}" amount="{1}" modifier="{2}" condition="{3}"/>'.format(
                            "credit" if g(line, "credit_gain") else "vp",
                            g(line, "credit_gain") if g(line,"credit_gain") else g(line, "vp_gain"),
                            "1" if not g(line, "gain_mod") else g(line, "gain_mod"),
                            g(line, "gain_cond")
                        )

                    ##
                    # Dice returns
                    ##
                    if g(line, "dice_back"):
                        xml += '\n\t\t<refund amount="{0}" type="{1}"/>'.format(g(line, "dice_back"), g(line, "dice_back_cond"))

                    ##
                    # :Extra: dice 
                    ##
                    if g(line, "extra_dice"):
                        for die in g(line, "extra_dice").split(","):
                            xml += '\n\t\t<additionalDie type="{0}"/>'.format(g(line, "extra_dice"))

                    ##
                    # Cost Reduction
                    ##
                    if g(line, "cost_reduction_type"):
                        for color in g(line, "cost_reduction_type").split(","):
                            xml += '\n\t\t<discount amount="{0}" type="{1}"/>'.format(g(line, "cost_reduction"), color)

                    xml += '\n\t\t<description text="{0}"/>\n\t</phaseEffect>'.format(g(line, "text"))
                if g(line, "die_gain"):
                    for i in range(int(g(line, "die_gain"))):
                        xml += '\n\t<diceGain type="{0}" placement="{1}"/>'.format(
                            g(line, "die_color").split(",")[i % len(g(line, "die_color").split(","))],
                            g(line, "placement")
                        )
                
                if g(line, "die_loss"):
                    xml += '\n\t<diceLoss/>'

                xml += "\n</card>"
        print(xml)

if __name__ == "__main__":
    init()