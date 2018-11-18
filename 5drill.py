# first exercise
# removing my from the beginning
name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 #inches
weight = 180 #lb
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f'Let\'s talk about {name}.')
print(f'He\'s {height} inches tall.')
print(f'He\'s {weight} pounds heavy.')
print(f"He's got {eyes} eyes and {hair} hair.") # instead of relying on \ before ' to avoid closing the string prematurely
print(f'His teeth are usually {teeth} depending on the coffee.')

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f'If I add {age}, {height}, and {weight} I get {total}.')

# second exercise
# calculating CM and KG
inch = 2.54
lb = 0.45
height_cm = height * inch # alternatively, could have just put the 2.54 here, like I did wigh weight below
weight_kg = weight * 0.45

print(f'In the metric system, he is {height_cm} centimeters tall, and weighs {weight_kg} kilograms.')

# on my own
# so what does the "f" do? f FORMATS the string, i.e., it tells Python to find the variable and put it INSIDE the string
# i.e., without FORMAT, you have to keep breaking the strings to call the variables
# using , inside the string without format is the same; but only works for now (while the true potential of format is not being used)
# also it's way more trouble and not at all skillful, elegant etc.
print('In the metric system, he is', height_cm, 'centimeters tall, and weights', weight_kg, 'kilograms.')