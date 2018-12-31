# nba game 7, raptors v. warriors match-up
warriors = ["Stephen Curry", "Klay Thompson", "Kevin Durant", "Draymond Green", "DeMarcus Cousins"]
raptors = ["Kyle Lowry", "Danny Green", "Kawhi Leonard", "Pascal Siakam", "Serge Ibaka"]
narrative = ["blablabla first quarter", "blablabla second quarter", "blablabla third quarter", "blablabla fourth quarter"]
c_count = 0 # to add: different scenarios (e.g., Green fouling out)

def confirm_lineup(gsw, toronto, tempo):
    if tempo == 0: l_toronto = set_lineup(gsw, toronto)
    else:
        change = ""
        while change.lower() not in ("y", "n"):
            print("Do you want to change the lineup you previously set? (Y/N)")
            change = input("> ").lower()
        if change == "y": l_toronto = set_lineup(gsw, toronto)
        elif change == "n": l_toronto = toronto

    print(f"Ok, here are the matchups for this quarter:\n")
    for i in range(0, 5): print(f"{l_toronto[i]} is guarding {gsw[i]}.") 
    
    confirm = input("\nConfirm? (Y/N)\n> ").lower() # to add: possibility of switching specific players later
    if confirm == "y": return l_toronto
    else:
        confirm_lineup(gsw, toronto, tempo)
        return l_toronto # without this, return was NONE, even if I hit "y" on the prompt on the second time (i.e., after one round of not confirming); WHY?!

def set_lineup(gsw, toronto):
    l_toronto = []

    for i in gsw:
        defender = name_input(f"Who should guard {i}?", toronto, l_toronto)
        l_toronto.append(defender)
    return l_toronto

def name_input(question, squad, lineup):
    print(question)
    name = input("> ")
    name = ''.join(x for x in squad if name.lower() in x.lower())
    while name not in squad: name = name_input(f"That player is not in the roster, pick one from the following:\n{squad}", squad, lineup)
    while name in lineup:
        gsw_player = warriors[lineup.index(name)]
        name = name_input(f"You already assigned {name} to guard {gsw_player}, pick a different player.", squad, lineup)
    return name

def each_quarter(narrative, gsw, toronto, tempo, counter):
    print(narrative)
    l_toronto = confirm_lineup(gsw, toronto, tempo)
    if l_toronto[0] == "Kawhi Leonard": return l_toronto, counter + 1
    else: return l_toronto, counter

lineup, c_count = each_quarter(narrative[0], warriors, raptors, 0, c_count) # ugly, but I need it for Q1; maybe the change to SET/CONFIRM_LINEUPS took care of this?
for i in range(1, 4): lineup, c_count = each_quarter(narrative[i], warriors, lineup, i, c_count)

if c_count == 4: print("Curry injury, you win")
else: print("you lose")