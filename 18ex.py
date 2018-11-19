# this one is like your scripts with argv
def print_two(*args): # * tells Python to take all the arguments to the function and put them in a list
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}') # first I forgot to close quotes

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # note that arguments are UNIQUE to the function, not connected to script or other functions
    print(f'arg1: {arg1}, arg2: {arg2}') # first I forgot to close quotes

# this just takes one argument
def print_one(arg1):
    print(f'arg1: {arg1}')

# this one takes no arguments
def print_none():
    print('I got nothin\'.')


print_two('Zed', 'Shaw')
print_two_again('Zed', 'Shaw')
print_one('First!')
print_none()