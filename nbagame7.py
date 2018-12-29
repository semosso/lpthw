# nba 7, raptors v. warriors match-up

warriors = ["Stephen Curry", "Klay Thompson", "Kevin Durant", "Draymond Green", "DeMarcus Cousins"]
raptors = ["Kyle Lowry", "Danny Green", "Kawhi Leonard", "Pascal Siakam", "Serge Ibaka"]

narratives = ["blablabla first quarter",
"blablabla second quarter",
"blablabla third quarter",
"blablabla fourth quarter"
] # should I have used dict? why one or the other?

def set_lineup(squad1, squad2): # sets Raptors (squad2) lineup player by player, based on GSW (squad1) lineup
    
    d_toronto = []

    for i in squad1: # para cada jogador em GSW
        print(f"Who should guard {i}?")
        defender = check_player(input("> "), squad2, d_toronto) # chama check_player para buscar o nome completo, checar se está no time, checar se foi escolhido antes
        d_toronto.append(defender) # após check, adiciona o escolhido ao lineup

    print(f"Ok, here are the matchups you set:")
    for i in range(0, 5):
        print(f"{d_toronto[i]} is guarding {squad1[i]}.") 
    confirm = input("Confirm? (Y/N)\n> ").lower() # consider adding the possibility of switching specific players later
    if confirm == "y":
        return d_toronto
    else:
        set_lineup(squad1, squad2)


def check_player(name, squad, lineup): # confirms if player is in roster or has already been assigned; I don't think I need the length check, but what the hell
    
    if len(name) > 3:
        name = ''.join(x for x in squad if name.lower() in x.lower()) # valeria a pena criar uma função só pra isso? se repete em três lugares
        
        while name not in squad: # confirma se o jogador está no time
            print(f"That player is not in the roster, pick one from the following:\n{squad}")
            new_name = input("> ")
            name = ''.join(x for x in squad if new_name.lower() in x.lower())
            
        while name in lineup: # confirma se o jogador já foi selecionado
            gsw_player = warriors[lineup.index(name)]
            print(f"You already assigned {name} to guard {gsw_player}, pick a different player.")
            new_name = input("> ")
            name = ''.join(x for x in squad if new_name.lower() in x.lower())

        return name
    else:
        print(f"That player is not in the roster, pick one from the following:\n{squad}")
        new_name = input("> ")
        check_player(new_name, squad, lineup)