# Escape sequences 101
tabby_cat = "\tI'm tabbed in." # \t inserts a tab
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat." # inserts a slash: the first one starts escape sequence, i.e., denies effect of second one

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
''' # in ln 6, the ' doesn't break it (i.e., by ending the string early) because of the triple quotes on ln 5

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# list of ALL escape sequences
# \\ backslash
print('Meus programas estão salvos no diretório vinicius\\lpthw\\')

# \' or \" single quote and double quote
print('I\'m starting to learn this.')
print("I said that \"I'm starting to learn this\".")

# \b ASCII backspace (BS)
print('I\'m starting to learn this\b.') # i.e., inserts a backspace at the end

# \f ASCII formfeed (FF)
print('I\'m starting to\flearn this.') # TIL this is called formfeed

# \n ASCII linefeed (LF)
print('I\'m starting to\nlearn this.') # new line

# \r carriage return (CR)
print('I\'m starting to\rlearn this.') # I can see what it makes, but no idea on the specifics ??

# \t horizontal tab (TAB)
print('\tI\'m starting to\tlearn this.') # in the beginning it inserted TAB, in the middle a single space

# \uxxxx character with 16-bit hex value xxxx
print('\uabcd') # ok, prints the "unicode" value

# \v ASCII vertical tab (VT)
print('I\'m starting to\vlearn this.') # vertical tab, nothing fancy

# \000 character with octal value 000
print('\123') # ok, prints value from some "database" (e.g., unicode reference)

# can't figure these out
# \xhh character with hex value hh
# \N{name} Character named name in the Unicode database (Unicode only)
# \Uxxxxxxxx character with 32-bit hex value xxxxxxxx 
# \a ASCII bell (BEL) 