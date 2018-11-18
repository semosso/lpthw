# BREAKING CODE

types_of_people = 10
x = f'There are {types_of_people} types of people.' # BRK: no FORMAT would print literal {}, not call the variable

binary = 'binary'
do_not = 'don\'t' # BRK: not having \ would end string prematurely
y = f'Those who know {binary} and those who {do_not}.'

print(x) # BRK: having quotes would print literally the name of the variable, not call it
print(y)

print(f'I said: {x}')
print(f'I also said: "{y}"')

hilarious = False
joke_evaluation = 'Isn\'t that joke so funny?! {}'
print(joke_evaluation.format(hilarious)) # BRK: not closing the FORMAT () or the print one

w = 'This is the left side...'
e = 'a string with a right side'

print(w + e)