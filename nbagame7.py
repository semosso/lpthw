# nba game 7, raptors v. warriors match-up
warriors = ["Stephen Curry", "Klay Thompson", "Kevin Durant", "Draymond Green", "DeMarcus Cousins"]
raptors = ["Kyle Lowry", "Danny Green", "Kawhi Leonard", "Pascal Siakam", "Serge Ibaka"]
narrative = ["Now set your defensive matchups or the first quarter:",
    "blablabla close first quarter, weak quarter by Curry, Durant impossible to guard as usual, and quiet Thompson.",
    "blablabla close second quarter, Curry starting to act up, Durant finally missing some shots, still no sign from Thompson.",
    "blablabla close third quarter, Curry well guarded, Durant back to being Durant, but Thompson on fire."]
c_count = 0 # to add: different scenarios (e.g., Green fouling out), different quarterly results from each individual matchups, etc. 

def confirm_lineup(gsw, toronto, tempo):
    if tempo == 0: l_toronto = set_lineup(gsw, toronto)
    else:
        change = ""
        while change.lower() not in ("y", "n"):
            print("Do you want to change the matchups from last quarter? (Y/N)")
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

print(f"""Finally free from the LeBron curse, the Raptors make the NBA finals. After six close games, Toronto and Golden State are set to face each other in game 7.
The Warriors lineup is: {warriors}
The Raptors lineup is: {raptors}""")
lineup, c_count = each_quarter(narrative[0], warriors, raptors, 0, c_count) # ugly, but I need it for Q1; maybe the change to SET/CONFIRM_LINEUPS took care of this?
for i in range(1, 4): lineup, c_count = each_quarter(narrative[i], warriors, lineup, i, c_count)

if c_count == 4: print("Curry couldn't handle the league's best defender up his ass the whole game, and picks up a late injury. You win by 2!")
else: print("You're up 2 until the last seconds, but Green set up a high screen and Curry hit a dagger from the logo. Tough break, guess it's rebuild time again!")