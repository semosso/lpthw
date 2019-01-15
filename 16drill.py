# SD 3: there's too much repetition; use strings, formats and escapes to have only one write

from sys import argv

script, filename = argv

print(f'We\'re going to erase {filename}.')
print('If you don\'t want that, hit CTRL-C (ˆC).')
print('If you do want that, hit RETURN.')

input('?') # does this make the ? get printed one line down?

print('Opening the file...')
target = open(filename, 'w') # what is "w"? parameter to open? or string? Is this what creates the file?
# if you don't have that file, it creates it!

print('Truncating the file. Goodbye!')
target.truncate() # couldn't I use truncate(filename) or filename.truncate())? i.e., do I have to open() it first?
# no to both. truncate() is not a function, it's a method of the object; filename is a string, so it doesn't have that method

print('Now I\'m going to ask you for three lines.')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('I\'m going to write these to the file.')

target.write(f'{line1}\n{line2}\n{line3}\n')

print('And finally, we close it.')
target.close()