# Assigns value "10" variable types_of_people
types_of_people = 10
# Assigns the whole string to the variable x; note the FORMAT in the string, i.e., you can attach it WITHIN the variable
x = f'There are {types_of_people} types of people.'

# Assign the string "binary" to the variable binary, and the same with the string "don't" and the variable do_not
binary = 'binary'
do_not = 'don\'t'
# Same as above, assigns string (with FORMAT) to the variable y
y = f'Those who know {binary} and those who {do_not}.' # Drill 2: 1st and 2nd string inside a string

# Note that there's no need to add quotes or FORMAT because you're not printing a string, but a variable 
print(x)
print(y)

# Difference here is that you're adding some words in a string, so you need quotes and FORMAT to call the variable WITHIN the string
print(f'I said: {x}') # Drill 2: 3rd string inside a string
print(f'I also said: "{y}"') # Drill 2: 4th string inside a string

hilarious = False
joke_evaluation = 'Isn\'t that joke so funny?! {}' # difference between this and X/Y is that variable is open, it can be any one
print(joke_evaluation.format(hilarious)) # FORMAT is what decides which variable to call; if it were "X", it'd call X

# Assigns whole strings on the right to the variables on the left
w = 'This is the left side...'
e = 'a string with a right side'

# Simply printing two strings, in order
print(w + e)