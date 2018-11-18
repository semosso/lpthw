# writing a script (i.e., a .py file) that accepts arguments as inputs
# an example of an argument is, on "python3.7 13ex.py", the 13ex.py - ?i.e., what you feed into the function?
from sys import argv # imports a feature called ARGV from the python feature set SYS; these features are called MODULES or LIBRARIES
script, first, second, third = argv

# argv is the ARGUMENT VARIABLE; it HOLDS the arguments we pass to the script when we run it
# ln 4 unpacks the argument variable, so instead of holding everything in argv, it distributes between all variables that I tell it to
## "take whatever is in argv, unpack it, and assign it to these variables"

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)

# IMPORTANT: I'm giving the ARGUMENTS when I run the script in terminal, not being prompted to include them afterwards
## they'll come in as strings as well as with input; can solve it with int() as well
# also, if I say that argv should expect to unpack the arguments into 4 variables, there'll be an error if I input less or more when I run

# EXTRA
# can I use inputs with argv? so that I don't have to insert all the info when I run the script on terminal? let's try
# the below is interesting, but doesn't get there: it calls for inputs and unpacks them, but all together without spaces
## for instance, if I input 1234, it assigns 1, 2, 3, 4 to each of the variables and prints them out

from sys import argv
script, first, second, third = input(argv)

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)

# EXTRA
## if I assign only one value to argv, it doesn't crash no matter how many variables I feed it; why?
from sys import argv # imports a feature called ARGV from the python feature set SYS; these features are called MODULES or LIBRARIES
script = argv

print('The script is called:', script)
