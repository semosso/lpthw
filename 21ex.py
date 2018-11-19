# using = and RETURN to set variable to be a VALUE FROM A FUNCTION
def add(a, b):
    print(f'ADDING {a} + {b}') # this (and other below) doesn't actually do the math because numbers are within a string
    return a + b
    # RETURN "sums up" the "result" of the function being applied to its parameters, in a format that can be used as a variable
    # by other functions; it's as if it said "here OTHER FUNCTION, I did whatever my function told me to, and here's the result,
    # use it as a parameter to do your thing"

def subtract(a, b):
    print(f'SUBTRACTING {a} - {b}')
    return a - b # p. 73, "you can return anything that you can put to the right of an ="

def multiply(a, b):
    print(f'MULTIPLYING {a} * {b}')
    return a * b

def divide(a, b): # I could probably use INPUT here, but it makes sense to leave it out of the function, which should be "holistic"
    print(f'DIVIDING {a} / {b}')
    return a / b


print('Let\'s do some math with just functions!')

age = add(30, 5) # note that the function doesn't only return stuff, but also prints; so it will print the ADDING (...)
height = subtract(78, 4) # also, note that return isn't printed, it's just the result of the function and goes unused unless called upon
weight = multiply(90, 2)
iq = divide(float(input('First number:\n> ')), float(input('Second number:\n> '))) # trying to include input (successful)

print(f'Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}')


# A puzzle for the extra credit, type it anwyway
print('Here\'s a puzzle.')

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # -4391? yep.
# p. 74, this isn't backwards, it's inside out; the difference matters! makes a lot of sense intuitively to me, thank god
# note in particular that this is taking the RETURN of functions as ARGUMENTS of other functions

print('That becomes: ', what, 'Can you do it by hand?') # yep.