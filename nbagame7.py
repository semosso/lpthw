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
                print(f"You already assigned {defender} to guard someone else, pick a different player.")
                # how to make this mention the specific GSW player?
                defender = fix_input(input("> "))
        else:
            print("I don't know who that is.")

    return d_toronto

def fix_input(name):
    full_name = ''.join(x for x in raptors if name.lower() in x.lower())
    return full_name

raptors = matchup(warriors, raptors)
print(raptors)

# decisions may lead to Curry injury or Green fouling out

# tentative: final outcome is raptors 110, warriors 108 (adjusted for differentials), but Curry hits a 3 off a Draymond screen
# only way to win is have 0 differential AND (Curry injured OR Green fouled out)