from sys import argv

script, filename = argv

print(f'We\'re going to erase {filename}.')
print('If you don\'t want that, hit CTRL-C (ˆC).')
print('If you do want that, hit RETURN.')

input('?') # does this make the ? get printed one line down?

print('Opening the file...')
target = open(filename, 'w+') # what is "w"? parameter to open? or string? Is this what creates the file? (NO, see ln 14)
# if you don't have that file, it creates it (w does it, as per doc)
# 'w' tells open that I want to write on the file (can also be r (read) or a (append, i.e., add to something))
## that's why I didn't need 'r' on exercise 15
# SD 5: if you have 'w', no need to add the truncate later, w already does that (i.e., W gets rid of what's in there, A adds)
# using w+, r+ or a+ let's me do both read and write, not just one or the other 

print('Truncating the file. Goodbye!')
target.truncate() # couldn't I use truncate(filename) or filename.truncate())? i.e., do I have to open() it first?

print('Now I\'m going to ask you for three lines.')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('I\'m going to write these to the file.')

target.write(line1)
target.write('\n') # at first I forgot the quotes; I need to input it into a string, to manipulate strings
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

# SD 2: read the file you just created
# print(target.read()) doesn't work, why? Error I get is "unsupported operation: not readable"
## maybe because W tells python that I can only write, not read (target is not only open(filename), but also modifier). let's try with W+
### nope... actually, it worked! but it seems to be reading the '\n', because it prints a blank line
## p. 32 mentions a "seek" command, which implies I can r/w/a different lines of the file; let's try to use this
target.seek(0)
print(target.read()) # IT WORKED! But is there a way I can do both ln 44 and 45 in only one?

print('And finally, we close it.')
target.close()