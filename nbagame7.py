# nba 7, raptors v. warriors match-up

warriors = ["Stephen Curry", "Klay Thompson", "Kevin Durant", "Draymond Green", "DeMarcus Cousins"]
raptors = ["Kyle Lowry", "Danny Green", "Kawhi Leonard", "Pascal Siakam", "Serge Ibaka"]

narratives = ["blablabla",
"blablabla",
"blablabla",
"blablabla",
""] # wanted to use a dictionary, but can't look through offsets

def set_lineup(squad1, squad2): # sets Raptors (squad2) lineup player by player, based on GSW (squad1) lineup
    
    d_toronto = []

    for i in squad1: # para cada jogador em GSW
        print(f"Who should guard {i}?")
        defender = check_player(input("> "), squad2, d_toronto) # chama check_player para buscar o nome completo, checar se está no time, checar se foi escolhido antes
        d_toronto.append(defender) # após check, adiciona o escolhido ao lineup

    print(f"Ok, here are the matchups you set:")
    for i in d_toronto:
        print(f"{d_toronto[i]} is guarding {squad1[i]}.") 
    confirm = input("Confirm? (Y/N)\n> ").lower() # consider adding the possibility of switching specific players later
    if confirm == "y":
        return d_toronto
    else:
        set_lineup(squad1, squad2)


def check_player(name, squad, lineup): # I think this successfully mergers previous three functions (fix_input, check_lineup, check_squad)
    
    if len(name) > 3: # evitando dor de cabeça (que eu nem sei se aconteceria) - e.g., menor probabilidade de ter dois jogadores com mesmas quatro letras do que três
        name = ''.join(x for x in squad if name.lower() in x.lower()) # encontra o nome completo
        
        while name not in squad: # confirma se o jogador está no time
            print(f"That player is not in the roster, pick one from the following:\n{squad}")
            new_name = input("> ")
            name = ''.join(x for x in squad if new_name.lower() in x.lower()) # valeria a pena criar uma função só pra isso? se repete em três lugares
            
        while name in lineup:
            gsw_player = warriors[lineup.index(name)]
            print(f"You already assigned {name} to guard {gsw_player}, pick a different player.")
            new_name = input("> ")
            name = ''.join(x for x in squad if new_name.lower() in x.lower()) # valeria a pena criar uma função só pra isso? se repete em três lugares

        return name
    else:
        print(f"That player is not in the roster, pick one from the following:\n{squad}")
        new_name = input("> ")
        check_player(new_name, squad, lineup)


# I originally thought about creating a function for each quarter (because each seems specific to me), but let's see if I can make it work with one
# making all the same function will make it harder for me to check injury/foul status later... maybe I create two global variables and add a counter to them after gameplay?
def each_quarter(squad1, squad2, narrative, tempo):
    
    if tempo != 0:
        print(f"{narrative}. Do you change your lineup (Y/N)?")
        change = input("> ").lower() # consider adding the possibility of switching specific players later
        if change == "y":
            raptors_lineup = set_lineup(squad1, squad2)
        else: raptors_lineup = squad2
    elif tempo == 0:
        print(f"{narrative}")
        print(f"Set your defensive assignments and good luck:") 
        raptors_lineup = set_lineup(squad1, squad2)

    c_count, g_count = gameplay(squad1, raptors_lineup, 0, 0) # will not work, need to find a way to make this and gameplay work on the same variable

    if c_count == 4: print("blablabla")
    elif g_count == 4: print("blablabla")


def gameplay(squad1, squad2, c_count, g_count): # the way I'm structuring now, score doesn't matter; I can add later, including specific plus/minus for each matchup 

    if squad2[0] == "Kawhi Leonard": # i.e., if Kawhi Leonard is guarding Curry
        c_count += 1
    elif squad2[3] == "Kawhi Leonard": # i.e., if Kawhi Leonard is guarding Draymond Green
        g_count += 1

        return c_count, g_count
    

raptors = set_lineup(warriors, raptors) # should I use alternative var, or keep changing the main list? what's the harm in changing?

for i in range(0, 5):
    each_quarter(warriors, raptors, narratives[i], i) # this doesn't allow for changing warriors squad, which I wanted to do at some point (Iggy coming in)
    