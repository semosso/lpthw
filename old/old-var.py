# Using variables and literal constants
i = 5 # this line is called a statement
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string. 
This is the second line.'''
print(s)

# Logical and physical lines: Python assumes each physical line corresponds to a logical line
# To get more than one logical line in the same phyisical line, use ;
i = 5; print(i)

# line joining: breaking long logical lines into multiple physical; explicit if \, implicit if line has opening (, [, {, but not closing
s = 'This is a single logical line that I will break \
into multiple \
physical lines' #explicit
print(s)

i =\
5
print(i) #explicit; do I need it? it works without the \ as well

# Numbers are optional
name = 'Vinicius'; age = 31
print("{0} turned {1} in 2018"
.format(name,age)) #implicit, see unclosed '(' in ln 30

# Importance of indentation; statements which go together must have the same indentation; four spaces is recommended indentation
i = 5
 print(i) #leads to error
 