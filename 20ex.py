from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read()) # no need to open? actually, there is indeed a need to open, see how current_line is defined in ln 14

def rewind(f):
    f.seek(0) # seek is by bytes, not lines (i.e., seek (1) doesn't go to ln 1, goes to byte 1)

def print_a_line(line_count, f):
    print(f'{line_count}:', f.readline(), end = '') # modified to add end = '' and colon after line count (with format) 
    # READLINE is also a function; reads any given line until the first \n it finds, or end of file (it returns \n as well)
    # however, shouldn't "line_count" be a parameter of readline()? does readline "borrow" line info from within the print?
    # or does each print_a_line below (ln 26-33) "leave" the file opened in each subsequent line (i.e., because it
    # prints only until first \n) and "line_count" doesn't really do anything other than inform me which line is being read?
    ## I'm exactly right, see p. 70

current_file = open(input_file) # opens with no modifiers, so defaults to "r", read

print('First let\'s print the whole file:\n')
print_all(current_file) # read works because file is opened definiton of current_file

print('\nNow let\'s rewind, kind of like a tape.\n')
rewind(current_file)

print('Let\'s print three lines:\n')

current_line = 1 
# what is ln 29 really doing, if it's not fed into READLINE in ln 12? informs which line is being printed? (yep, see above and p. 70)
print_a_line(current_line, current_file)

current_line = current_line + 1 # could have been done with += (x += y means x = x + y); see ln 37
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
current_file.close() # figure out why this doesn't result in an error (unlike 17ex.py, for instance)
## because unlike in ex 17, I actually had saved/assigned the open file to the variable, i.e., kept it open