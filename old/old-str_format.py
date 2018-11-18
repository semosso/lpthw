# Let's start learning some more stuff
age = 31 # literal constant; L means you use its value literally; C means value cannot be changed
name = 'Vinicius' # same as above

# Aprendendo format
print("{0} was {1} years old when he started programming Python".format(name,age)) # print is a statement; what is format? what are {}?
print("Why is {0} playing with that python?".format(name)) 

# Same using STRING CONCATENATION, but uglier
print(name + ' is ' + str(age) + ' years old')

# Numbers are optional
print("{} turned {} in 2018".format(name,age))

# Naming the parameters; why would this be useful, if I have to name them "twice"?
print("{name}, who is {age} is about to see if this really works".format(name=name, age=age))

# f-strings: f before str fills in arguments (are they called arguments?)
print(f"{name} was {age} when he decided to learn how to code")

# ".Xf" tells how many decimal places to give to result from format; does "f" stand for float?
print("{0:.2f}".format(1/2))

# fills with underscores with the world centered in the middle; in ^X, X is the width of the whole string, what does ^ do?
print('{0:_^9}'.format('hello'))

# print ends with invisible "\n", so if you don't want new line you should insert end='X' in the end, being X a blank, a space, whatever
print('a', end='')
print('b')

# escape sequences: \ to indicate that ', ", \ should be read as what they are; " or ' does the trick as well, if you're using both " and ' 
print('what\'s my name?')
print("people used to say \"programming is hard\"") # if instead of " I had used ' to begin/end string, no \ would be necessary
print('let\'s try to use \ttab')
print('let\'s try to write in two lines.\nDid it work?')
print('this is the first sentence, \
and this is the second.') # the \ in ln 37 indicates that it should be all the same sentence
print(r'Escape sequences examples are \t, for tabs, or \n, for new line') # raw strings: r in the beginning disabilitates \ escape sequences
print('Escape sequences examples are \\t, for tabs, or \\n, for new line') # prints the same as above, but more burdensome to add all \