# nba 7, raptors v. warriors match-up

# user chooses defensive matchups from pre defined lineups

warriors = ["Stephen Curry", "Klay Thompson", "Kevin Durant", "Draymond Green", "Kevon Looney"]
raptors = ["Kyle Lowry", "Danny Green", "Kawhi Leonard", "Pascal Siakam", "Serge Ibaka"]

# quarter by quarter matchup decisions may lead to different outcomes
# each quarter function should take both lineups as parameters, and return the differential
# or should I just get a "change matchup function"? maybe both change matchup and quarter functions, and we can have multiple changes

def matchup(squad1, squad2):
    d_toronto = []
    a_warriors = []

    for i in squad1: # para cada jogador em GSW
        print(f"Who should guard {i}?") # quem deveria marcar tal jogador?
        defender = fix_input(input("> "), squad2) # recebe dados, chama função input para buscar o nome completo
        defender = check_lineup(defender, squad2, d_toronto) # chama função lineup para checar se já foi escolhido
        d_toronto.append(defender)

        # attacker_index = d_toronto.index(defender)
        # attacker = squad1[attacker_index]
        # a_warriors.append(attacker)
        # don't want to delete this code, but I think it's useless - i.e., I'm now switching GSW order around, only raptors
        
    return d_toronto, a_warriors

def fix_input(name, squad): # maybe try and merge this one with check_squad?
   name = ''.join(x for x in squad if name.lower() in x.lower())
   full_name = check_squad(name, squad)
   return full_name
    # maybe a way to get the head to head matchups would be to return also raptors.index(full_name)

def check_lineup(name, squad, lineup):
    while name in lineup:
        name = check_squad(name, squad)
        print(f"You already assigned {name} to guard someone, pick a different player.") # this is not working, it lets me choose whatever name not in squad
        name = fix_input(input("> "), squad)
    return name

def check_squad(name, squad):
    while name not in squad:
        print(f"That player is not in the roster, pick one from the following:\n{squad}")
        name = fix_input(input("> "), squad)
    return name

rap, war = matchup(warriors, raptors) # should I use these alternative vars, or just keep changing the main lists?
print(rap) # test
print(war) # test

# decisions may lead to Curry injury or Green fouling out

# tentative: final outcome is raptors 110, warriors 108 (adjusted for differentials), but Curry hits a 3 off a Draymond screen
# only way to win is have 0 differential AND (Curry injured OR Green fouled out)