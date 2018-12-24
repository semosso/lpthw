the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f'This is count {number}')
    # name of variable doesn't mind, you could have whatever; variable is defined by for-loop when it starts each time; same as ln 11 and 16

# same as above
for fruit in fruits:
    print(f'A fruit of type {fruit}')

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f'I got {i}')

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# range skips last number; it's first to last without including the last, that's why it only results in six numbers being added (0 through 5)
for i in range(0, 6):
    print(f'Add {i} to the list.')
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f'Element was: {i}')

# STUDY DRILL
# could you have avoided for-loop in ln 24 entirely and just assigned range directly to elements?
# yes, via LIST COMPREHENSION
# from Python doc: A list comprehension consists of brackets containing an expression followed by a FOR clause, then zero or more FOR or IF clauses.
# The result will be a new list resulting from evaluating the expression in the context of the FOR and IF clauses which follow it.
elements = [i for i in range(0, 6)]
print(elements)