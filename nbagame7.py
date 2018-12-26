# nba 7, raptors v. warriors match-up

# user chooses defensive matchups from pre defined lineups

warriors = ["Stephen Curry", "Klay Thompson", "Kevin Durant", "Draymond Green", "Kevon Looney"]
raptors = ["Kyle Lowry", "Danny Green", "Kawhi Leonard", "Pascal Siakam", "Serge Ibaka"]

# quarter by quarter matchup decisions may lead to different outcomes
# each quarter function should take both lineups as parameters, and return the differential
# or should I just get a "change matchup function"? maybe both change matchup and quarter functions, and we can have multiple changes

def matchup(gsw, toronto):
    d_toronto = []

    for i in gsw:
        print(f"Who should guard {i}?")
        defender = fix_input(input("> "))

        if defender in toronto and defender not in d_toronto:
            d_toronto.append(defender)
        elif defender in d_toronto:
            while defender in d_toronto:
                print(f"You already assigned {defender} to guard someone {i}, pick a different player.")
                # how to make this mention the specific GSW player?
                # maybe here I'd create a dictionary or tuple, or whatever // e.g., match Curry and Lowry when I make that assignment
                defender = fix_input(input("> "))
                d_toronto.append(defender) # this doesn't work, because it becomes infinite loop; I need a way to append, though
                # maybe I can invert and leave the append for the else? Every "exception" within IF and ELIF, and ELSE would be the "correct"
        else:
            while defender not in toronto:
                print(f"I don't know who that is, pick a player from the following:\n{toronto}")
                defender = fix_input(input("> "))
                d_toronto.append(defender) # this doesn't work, because it becomes infinite loop; I need a way to append, though
                # maybe I can invert and leave the append for the else? Every "exception" within IF and ELIF, and ELSE would be the "correct"

    return d_toronto

def fix_input(name):
    full_name = ''.join(x for x in raptors if name.lower() in x.lower())
    return full_name

raptors = matchup(warriors, raptors)
print(raptors)

# decisions may lead to Curry injury or Green fouling out

# tentative: final outcome is raptors 110, warriors 108 (adjusted for differentials), but Curry hits a 3 off a Draymond screen
# only way to win is have 0 differential AND (Curry injured OR Green fouled out)