# pretty much what I had done on Ex 11 (i.e., string prompt inside input), so I won't lose too much time here
age = input('How old are you? ')
height = input('How tall are you? ')
weight = input('How much do you weigh? ')

print(f'So, you\'re {age}, {height} tall and {weight} heavy.')

# Drills

# pydoc is a tool to generate python documentation (similar to a "man" in shell)
# can I use it to document my own functions? actually, can I 'create' functions?

# trying to see what comes from using input() inside print, without storing a variable
print('How old are you?', input()) # you don't get a prompt until you insert some data... Why?