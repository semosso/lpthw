# FIRST
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ') #! parenthetical
weight = input() #! why is weight's syntax like this? (i.e., orange)
#! figured out, because no parenthetical, makes python think it's a parameter

print(f"So, you're {age} old, {height} tall and {weight} heavy.") #! height not defined

# SECOND
from sys import argv
script, filename = argv #! argv not imported; also, maybe that's why both FILENAME and TXT are interpreted as parameters

txt = open(filename) #! maybe txt is also proprietary term? filename spelled wrong

print(f"Here's your file {filename}:") #! no call to format method, either with F or .format
print(txt.read()) #! txt name is wrong
txt.close()

print("Type the filename again:") # you never actually typed the file name above, as it came from argv, not input
file_again = input("> ") #! why is this not being "syntaxed" as string? why is variable syntaxed like this?

txt_again = open(file_again)

print(txt_again.read()) #! that's not how you call a method (_, not .); you should also close it too
txt_again.close()

THIRD
print('Let\'s practice everything.') #! no escape sequence before the second ' (i.e., \') is breaking everything
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
#! this is fucked; indentation, and you can't break lines like this without triple ""

poem = """ 
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
""" #! "poem" in ln 29 is syntaxed like this because of the mess up in the formatting of ln 25-27

#! no end quote on ln 39
print("--------------") 
print(poem)
print("--------------")
#! no start quote on ln 41

five = 10 - 2 + 3 - 6 #! messed up math, lacks a 6
print(f"This should be five: {five}") #! lacks parenthetical

def secret_formula(started): #! lacks final colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 #! lacks math operator
    return jelly_beans, jars, crates


start_point = 10000 #! again, why the fuck is the variable syntax all fucked up
beans, jars, crates = secret_formula(start_point)
#! assigning wrong amount of values (i.e., function returns THREE, you have only TWO vars)

## ZS: remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
## ZS: it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.") #! crates not defined above, see cmmt on ln 55

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #! wrong name for startpoint variable
## ZS: this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

FOURTH
people = 20
cats = 30 #! wrong name
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") #! missing both parentheticals

if people > cats: #! both IF are using the same relative operator; this should be >, not < 
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: #! missing colon
    print("The world is dry!")

dogs += 5 

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: #! missing colon
    print("People are less than or equal to dogs.") #! missing final quote


if people == dogs: #! equal should be double equal (i.e., math operator; not the one that assigns)
    print("People are dogs.")