# Input prompts user to input some data and stores it as whatever variable you assign it to
print('How old are you?', end = ' ')
age = input()
print('How tall are you?', end = ' ')
height = input()
print('How much do you weigh?', end = ' ')
weight = input()

print(f'So you\'re {age} old, {height} tall and {weight} heavy.')

# INPUTs are stored as strings, not numbers; for instance, ln 11 will print both strings
print(age + height)

# we can fix that with int(), which converts the number-string to a number-integer; float works the same (see ln 28)
print('How old are you?', end = ' ')
age2 = int(input())
print('How tall are you?', end = ' ')
height2 = int(input())
print('How much do you weigh?', end = ' ')
weight2 = float(input())

print(age2 + height2 + weight2) # PERFECT! however, if input also has letter, you get an error

# EXTRA
# I don't have to use all the prints, because input itself shows a prompt
name = input('What is your name? ')
age = input(f'Nice to meet you, {name}! How old are you? ')
print(f'Wow, {name}, are you really {age}?')

# interestingly, when I call the variable later it only shows the value that was inputted, not the prompt to input again