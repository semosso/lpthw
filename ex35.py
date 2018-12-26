from sys import exit

# def gold_room():
#     print("This room is full of gold. How much do you take?")

#     choice = input("> ")
#     if "0" in choice or "1" in choice: # what if input is 22? / GOES TO DEAD
#         how_much = int(choice)
#     else:
#         dead("Man, learn to type a number.")
    
#     if how_much < 50:
#         print("Nice, you're not too greedy, you win!")
#         exit(0) 
#         # exits script without any return? will need to understand this in more detail, and implications / 0 is actually error message
#         # if 0, good exit, no error; other numbers would indicate specific types of errors (e.g., error(12) would be error of the type 12)
#     else:
#         dead("You greedy bastard!")


def bear_room():
    print("There's a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True: # what does this mean? / CREATES AN INFINITE LOOP
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.") # when I call another function, does WHILE stop? / SEEMS TO.
        elif choice == "taunt bear" and not bear_moved:
            # does ln above mean "and bear_moved is not true" (implied below lns 35 and 37)?
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved: # i.e., if you taunt him once again, after you taunted him first and bear_moved became TRUE
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice: # does this mean "if string saved in choice contains the word "flee"?" / YES.
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# STUDY DRILL 5: FIX THE WEIRD WAY IN WHICH GOLD_ROOM GETS USER TO TYPE A NUMBER
# note that functions do not have to be defined in the order that they will be called; HOWEVER, if I had put this revised GOLD_ROOM after START, things
# would have worked fine up until one of the other functions called it, in which case it would give an exception because not yet defined;
# what if I had both gold_room functions?
# PYLINT FLAGS THAT IT HAS ALREADY BEEN DEFINED, BUT IF I RUN THE SCRIPT I DON'T GET AN ERROR (AND IT USES THE SECOND ONE)

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = int(input("> "))
    
    if choice < 50:
        print("Nice, you're not too greedy, you win!")
        exit(0) 
        # exits script without any return? will need to understand this in more detail, and implications / 0 is actually error message
        # if 0, good exit, no error; other numbers would indicate specific types of errors (e.g., error(12) would be error of the type 12)
    else:
        dead("You greedy bastard!")

start()